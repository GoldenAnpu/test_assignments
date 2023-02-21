import logging
import cv2
import os
import numpy as np

logging.basicConfig(level=logging.DEBUG)


def create_dir(dir_name: str) -> str:
    """
    Checks existence of directory, creates if it doesn't exist.

    :params:
        :param dir_name: name for dir.
        :return: dir_name:  name of created dir for the following usage.
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name


def get_image_size(image_name: str) -> tuple[int, int, np.ndarray]:
    """
    Gathers height and width of source image

    :params:
        :param image_name: source file name
        :return: tuple of (height, width, image)
    """
    image_ndarray = cv2.imread(image_name)
    height, width, _ = image_ndarray.shape
    return height, width, image


def input_and_prepare_values(img_h: int, img_w: int) -> list[int]:
    """
    Generates input for sliding window values and prepares them for the following usage.
    Window sizes "h" and "w" able to input as pixels or percents.
    Offset "y" and "x" values able to input as pixels.

    :params:
        :param img_h: height of original image
        :param img_w: width of original image
        :return: list of prepared values ['h', 'w', 'y', 'x']
    """
    input_values = ['h', 'w', 'y', 'x']
    output_values = []
    for value_name in input_values:
        if value_name == 'h' or value_name == 'w':
            value = input(f'Define value "{value_name}" as integer with ending "px" or "%" ')
        else:
            value = input(f'Define value "{value_name}" as integer  ')

        if type(value) == str and value[-1] == '%':
            if value_name == 'h':
                image_value = img_h
            elif value_name == 'w':
                image_value = img_w
            else:
                raise ValueError
            value = float(value[:-1]) / 100.0
            value = round(image_value * value)
        elif type(value) == str and value[-2:] == 'px':
            value = int(value[:-2])
        else:
            value = int(value)

        output_values.append(value)
    return output_values


# optional
def sliding_window_with_pad(height: int, width: int, x_offset: int, y_offset: int, read_image: np.ndarray):
    """
    Slides a window of given height and width over the image with given x and y offsets.

    :params:
        :param height: sliding window height
        :param width: sliding window width
        :param x_offset: offset step for the next window relative to the previous one along the x-axis
        :param y_offset: offset step for the next window relative to the previous one along the y-axis
        :param read_image: object given by cv2.imread(img_file)
        :return: yield piece of image
    """

    for y_axis_pos in range(0, read_image.shape[0] + 1, y_offset):
        for x_axis_pos in range(0, read_image.shape[1] + 1, x_offset):
            yield height, \
                  width, \
                  x_axis_pos, \
                  y_axis_pos, \
                  read_image[y_axis_pos:y_axis_pos + height, x_axis_pos:x_axis_pos + width]


def sliding_window_with_offset(height: int, width: int, x_offset: int, y_offset: int, read_image: np.ndarray):
    """
    Slides a window of given height and width over the image with given x and y offsets.

    :params:
        :param height: sliding window height
        :param width: sliding window width
        :param x_offset: offset step for the next window relative to the previous one along the x-axis
        :param y_offset: offset step for the next window relative to the previous one along the y-axis
        :param read_image: object given by cv2.imread(img_file)
        :return: yield piece of image
    """

    for y_axis_pos in range(0, read_image.shape[0] + 1, y_offset):
        # slide back along y-axis if window cross the border
        if (y_axis_pos + height) > read_image.shape[0]:
            y_axis_pos = read_image.shape[0] - height
        for x_axis_pos in range(0, read_image.shape[1] + 1, x_offset):
            # slide back along x-axis if window cross the border
            if (x_axis_pos + width) > read_image.shape[1]:
                x_axis_pos = read_image.shape[1] - width
            image_window = read_image[y_axis_pos:y_axis_pos + height, x_axis_pos:x_axis_pos + width]
            yield height, width, x_axis_pos, y_axis_pos, image_window


def tidy_up_window_params(win_h: int, win_w: int, y_offset: int, x_offset: int, img_h: int, img_w: int) -> tuple:
    """
    Reduces input sizes in two steps.
    Sliding window sizes can't be more than input image sizes, so them reduces up to input image sizes.
    Offsets can't be more than window sizes, so them reduces up to window sizes.

    :params:
        :param win_h: window height
        :param win_w: window width
        :param y_offset: offset by y-axis
        :param x_offset: offset by x-axis
        :param img_h: input image height
        :param img_w: input image width
        :return: tuple of window sizes (win_h, win_w, y_offset, x_offset)
    """
    if win_h > img_h:
        logging.info(f' Parameter "h={win_h}" is reduced to {img_h} according to the image size')
        win_h = img_h
    if win_w > img_w:
        logging.info(f' Parameter "w={win_w}" is reduced to {img_w} according to the image size')
        win_w = img_w
    if y_offset > win_h:
        logging.info(f' Parameter "y={y_offset}" is reduced to {win_h} according to the sliding window size')
        y_offset = win_h
    if x_offset > win_w:
        logging.info(f' Parameter "x={x_offset}" is reduced to {win_w} according to the sliding window size')
        x_offset = win_w

    return win_h, win_w, y_offset, x_offset


input_dir = 'input'
output_dir = 'output_split'
one_back_to_dir = '../'

if __name__ == "__main__":
    # check images with different types and the same names
    os.chdir(input_dir)
    file_names = os.listdir()
    for img_file in file_names:
        image_h, image_w, image = get_image_size(img_file)
        logging.info(f' Starting to split image "{img_file}" with {image_w}x{image_h} sizes')
        h, w, y, x = input_and_prepare_values(image_h, image_w)
        h, w, y, x = tidy_up_window_params(h, w, y, x, image_h, image_w)
        image_folder_name = img_file.replace('.', '__')  # saves type of image in the output folder name
        os.chdir(one_back_to_dir + output_dir)
        picture_split_dir = create_dir(image_folder_name)
        os.chdir(picture_split_dir)
        for h, w, x, y, window in sliding_window_with_offset(h, w, x, y, image):
            output_name = f'offs_y_{y}_x_{x}__win_h_{h}_w_{w}__origsize_h_{image_h}_w_{image_w}_{img_file}'
            cv2.imwrite(output_name, window)
        logging.info(f' splitting of image "{img_file}" complete\n')
        os.chdir(one_back_to_dir * 2 + input_dir)
