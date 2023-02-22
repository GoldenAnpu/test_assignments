import logging
import cv2
import os
import numpy as np
import shutil
from split import create_dir

logging.basicConfig(level=logging.DEBUG)


def clean_output_dirs():
    os.chdir('supervisely/split_n_merge')
    for directory in os.listdir(input_dir):
        shutil.rmtree(input_dir + directory)
    for file_name in os.listdir(output_dir):
        os.remove(output_dir + file_name)


def get_params(params: str, value_type: str) -> tuple[int, int]:
    """
    Gets sizes from file name for the following calculations.

    :params:
        :param params: name of the first piece file from original image which contain parameters (sizes)
        :param value_type: defines for what we get parameters from scope
        :return: tuple of height and width size or y-axis and x-axis  point
    """
    if value_type == 'window':
        obj = 1
    elif value_type == 'orig':
        obj = 2
    elif value_type == 'offset':
        obj = 0
    else:
        raise ValueError(f"value_type = '{value_type}' can't be used")
    sizes = params.split('__')[obj]
    size_h_y = int(sizes.split('_')[2])
    size_w_x = int(sizes.split('_')[4])
    return size_h_y, size_w_x


# in case of using sliding_window_with_pad
def create_canvas_from_pieces(file_list: list) -> np.ndarray:
    """
    Gets parameters from pieces and create empty canvas for merged output image.

    :params:
        :param file_list: list of image pieces
        :return: canvas: empty image canvas to fill in pieces
    """
    rows = cols = 0
    for img_file in file_list:
        y_axis_point, x_axis_point = get_params(img_file, 'offset')
        rows = max(rows, y_axis_point + window_size_h)
        cols = max(cols, x_axis_point + window_size_w)

    canvas = np.zeros((rows, cols, 3), dtype=np.uint8)
    return canvas


def create_canvas_from_orig(folder_name: str) -> np.ndarray:
    """
    Gets input folder name and converts it to path of original file.
    Gather parameters from original image and create empty canvas for merged output image.

    :params:
        :param folder_name: input folder name
        :return: canvas: empty image canvas to fill in pieces
    """

    image_name = folder_name.replace('__', '.')
    path_to_file = source_dir + image_name
    height, width, channels = cv2.imread(path_to_file).shape
    canvas = np.zeros((height, width, channels), dtype=np.uint8)
    return canvas


def diff_input_output_merged(image_name):
    """
        Read source and final image and compare them by pixel.

        :params:
            :param image_name: name of source image
        """

    image_name = image_name.replace('__', '.')
    source = cv2.imread(source_dir + image_name)
    final = cv2.imread(output_dir + image_name)

    h, w, _ = source.shape
    diff = cv2.subtract(source, final)
    error = np.sum(diff ** 2)
    mse = error / (float(h * w))

    if mse == 0.0:
        logging.info(f' Image "{image_name}" restored perfectly')
    else:
        logging.error(f' Image "{image_name}" restored unsuccessful: {mse}')


# in case of using sliding_window_with_pad
def crop_black_border(image_name):
    """
    Read output image and crop up to original size.

    :params:
        :param image_name: image name
    """
    orig_img = cv2.imread(f'{source_dir + image_name}.png')
    img_to_crop = cv2.imread(f'{output_dir + image_name}.png')
    cropped_img = img_to_crop[:orig_img.shape[0], :orig_img.shape[1]]
    cv2.imwrite(output_dir + folder + '.png', cropped_img)


def merge_pieces_and_save(folder_name: str, file_name: str):
    """
    Read prepared pieces of files and add them to canvas.

    :params:
        :param folder_name: name of folder where stored pieces
        :param file_name: name of piece file
    """
    output_image = output_dir + folder_name.replace('__', '.')  # path + name and type
    piece = cv2.imread(input_dir + folder_name + '/' + file_name)
    # piece = piece[:min(window_size_h, orig_img_h - y_axis), :min(window_size_w, orig_img_w - x_axis), :]
    output_canvas[y_axis:y_axis + piece.shape[0], x_axis:x_axis + piece.shape[1]] = piece
    cv2.imwrite(output_image, output_canvas)


def prepare_split_sub_folders() -> list:
    """
    Checks empty folders in output_split, log it and delete.

    :return: sub_dirs - list of prepared folders
    """
    sub_dirs = os.listdir(input_dir)
    for sub_dir in sub_dirs:
        sub_dir_path = input_dir + sub_dir
        if not os.listdir(sub_dir_path):
            os.rmdir(sub_dir_path)
            logging.warning(f' Directory "{sub_dir}" deleted due to emptiness')
    sub_dirs = os.listdir(input_dir)
    return sub_dirs


source_dir = 'input/'
input_dir = 'output_split/'
output_dir = 'output_merged/'

if __name__ == "__main__":
    create_dir(output_dir)
    prepared_folders = prepare_split_sub_folders()
    for folder in prepared_folders:
        logging.info(f' Starting to merge pieces of image "{folder}"')
        files = os.listdir(input_dir + folder)
        first_file = files[0]
        window_size_h, window_size_w = get_params(first_file, 'window')
        orig_img_h, orig_img_w = get_params(first_file, 'orig')
        output_canvas = create_canvas_from_orig(folder)
        # Load each image piece and paste it onto the canvas at the corresponding position
        for file in files:
            y_axis, x_axis = get_params(file, 'offset')
            merge_pieces_and_save(folder, file)
        diff_input_output_merged(folder)
