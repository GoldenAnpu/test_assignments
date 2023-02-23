import logging
import urllib.request
import zipfile
import cv2
import numpy as np
import os
from PIL import Image


logging.basicConfig(level=logging.INFO)


# ------------------------- OPTIONAL -------------------------
# Download file
def download_and_show_progress(davis_url: str) -> str:
    """
    Downloads archive using predefined URL

    :params:
        :param davis_url: url of archive
        :return: print process info and return file_name for extracting
    """
    file_name = davis_url.split('/')[-1]
    logging.info(f' Starting to download file "{file_name}"')
    with urllib.request.urlopen(davis_url) as response, open(file_name, 'wb') as out_file:
        length = response.getheader('content-length')
        if length:
            length = int(length)
        downloaded = 0
        block_size = 1024
        while True:
            buffer = response.read(block_size)
            if not buffer:
                break
            downloaded += len(buffer)
            out_file.write(buffer)
            if length:
                progress = downloaded / length
                percent = int(progress * 100)
                print(f"\r{percent}% downloaded", end='')

    logging.info(f' Downloading complete!')
    return file_name


# Extract file
def extract_all(file_name: str, output_path: str):
    """
    Extracts data from archive on specified directory

    :params:
        :param file_name: archive name
        :param output_path: where to place extracted data
    """
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(path=output_path)


# --------------------------- MAIN ---------------------------
def create_dir(dir_name: str) -> str:
    """
    Checks existence of directory, creates if it doesn't exist

    :params:
        :param dir_name: name for dir
        :return: dir_name for the following operations
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name


def remove_black_background_in_annotation(input_dir: str, output_dir: str):
    """
    Deletes black background in annotation files and saves with transparent one in new place

    :params:
        :param input_dir: directory with annotation images
        :param output_dir: new directory where output file will be saved
    """
    logging.info(f' Removing of black background in annotations started')
    save_dir = create_dir(output_dir)
    for directory in os.listdir(input_dir):
        save_subdir = create_dir(f'{save_dir}{directory}/')
        for file in os.listdir(f'{input_dir}{directory}'):
            file_path = f'{annotations_dir}{directory}/{file}'
            img_mask = cv2.imread(file_path)
            # convert BGR в RGBA
            alpha = np.ones(img_mask.shape[:2], dtype=img_mask.dtype) * 255
            rgba = cv2.merge((img_mask, alpha))
            # create mask for black background
            gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
            # apply mask
            rgba[:, :, 3] = mask
            save_name = f'{save_subdir}{file}'
            cv2.imwrite(save_name, rgba)
    logging.info(f' Removing of black background in annotations finished')


def merge_image_and_annotation_opencv(intput_image_dir: str, input_mask_dir: str, output_dir: str):
    """
    Merges source image from sequence with prepared mask and saves as new image

    :params:
        :param intput_image_dir: directory with source images
        :param input_mask_dir: directory with annotation images
        :param output_dir: new directory where annotated images will be saved
    """
    logging.info(f' Merging of images and annotations started')
    save_dir = create_dir(output_dir)
    for directory in os.listdir(intput_image_dir):
        save_subdir = create_dir(f'{save_dir}{directory}/')
        for file in os.listdir(f'{intput_image_dir}{directory}'):
            jpg_image = cv2.imread(f'{intput_image_dir}{directory}/{file}')
            png_image = cv2.imread(f'{input_mask_dir}{directory}/{file.split(".")[0]}.png')
            overlay = cv2.addWeighted(jpg_image, 1, png_image, 1, 0)
            save_name = f'{save_subdir}{file}'
            cv2.imwrite(save_name, overlay)
    logging.info(f' Merging of images and annotations finished')


def create_contour_for_annotation(input_dir: str, output_dir: str):
    """
    Draws contour for object in image file with transparent background

    :params:
        :param input_dir: directory with annotation images
        :param output_dir: new directory where contour images will be saved
    """
    logging.info(f' Merging of images and annotations started')
    save_dir = create_dir(output_dir)
    for directory in os.listdir(input_dir):
        save_subdir = create_dir(f'{save_dir}{directory}/')
        for file in os.listdir(f'{input_dir}{directory}'):
            mask = f'{input_dir}{directory}/{file}'
            image = cv2.imread(mask, cv2.IMREAD_UNCHANGED)
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Apply thresholding to obtain a binary image
            _, thresh = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
            # Find contours in the binary image
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Create a new blank image with the same size as the original image
            image[:, :, :3] = 0  # set the RGB channels to 0
            image[:, :, 3] = 0  # set the alpha channel to 0
            # Draw the black contour on the blank image
            cv2.drawContours(image, contours, -1, (0, 0, 0, 255), 1)
            # Save the black contour as a PNG image
            save_name = f'{save_subdir}{file}'
            cv2.imwrite(save_name, image)
    logging.info(f' Merging of images and annotations finished')


def merge_image_and_contour_pil(intput_image_dir: str, input_contour_dir: str, output_dir: str):
    """
    Merges masked image from sequence with contour for its mask and saves as new image

    :params:
        :param intput_image_dir: directory with masked images
        :param input_contour_dir: directory with contour images
        :param output_dir: new directory where contoured images will be saved
    """
    logging.info(f' Merging of annotated images and contours started')
    save_dir = create_dir(output_dir)
    for directory in os.listdir(intput_image_dir):
        save_subdir = create_dir(f'{save_dir}{directory}/')
        for file in os.listdir(f'{intput_image_dir}{directory}'):
            jpg_image = Image.open(f'{intput_image_dir}{directory}/{file}')
            png_image = Image.open(f'{input_contour_dir}{directory}/{file.split(".")[0]}.png')
            jpg_image.paste(png_image, (0, 0), png_image)
            save_name = f'{save_subdir}{file}'
            jpg_image.save(save_name)
    logging.info(f' Merging of annotated images and contours finished')


def get_min_width_of_images(source_catalog: str) -> int:
    """
    Checks width in all source images

    :params:
        :param source_catalog: catalog with source images
        :return: min_width - the smallest width of all images
    """
    directories = os.listdir(source_catalog)
    min_width = set()
    for directory in directories:
        file = os.listdir(source_catalog + directory)[0]
        img = cv2.imread(f'{source_catalog}{directory}/{file}')
        _, width, _ = img.shape
        min_width.add(width)
    min_width = min(min_width)
    return min_width


def resize_prepared_jpgs(source_dir: str, output_dir: str, min_width: int):
    """
    Resizes all images that are ready for creating video from sequence

    :params:
        :param source_dir: source dir
        :param output_dir: output dir
        :param min_width: the smallest width of all images
    """
    dir_list = os.listdir(source_dir)
    output_dir_name = create_dir(output_dir)
    logging.info(f' Resizing of prepared images started')
    # Load image
    for directory in dir_list:
        create_dir(output_dir_name + directory)
        for file in os.listdir(source_dir + directory):
            img = cv2.imread(f'{source_dir}{directory}/{file}')
            # Get original image width and height
            h, w = img.shape[:2]
            # Calculate target height to maintain aspect ratio
            target_height = int(h / w * min_width)
            # Resize image using calculated target dimensions
            resized_img = cv2.resize(img, (min_width, target_height))
            # Add black padding to fit the same height as smaller image
            padding_top = int((h - target_height) / 2)
            padding_bottom = h - target_height - padding_top
            pads = ((padding_top, padding_bottom), (0, 0), (0, 0))
            resized_img = np.pad(resized_img, pads, mode='constant', constant_values=0)
            # Save resized image
            cv2.imwrite(f'{output_dir_name}{directory}/{file}', resized_img)
    logging.info(f' Resizing of prepared images finished')


def does_input_data_exist(source_dir: str) -> bool:
    """
    Checks input directory for data existence

    :params:
    :param source_dir: input directory with data
    :return: "True" if it exists, "False" if it doesn't
    """
    return bool(os.listdir(source_dir))


def check_input_data_consistency():
    """
    Checks consistency of input data

    :return: raises error FileNotFoundError if not consistent
    """
    if os.listdir(annotations_dir) != os.listdir(source_images_dir):
        raise FileNotFoundError


def convert_sequence_to_video(input_dir: str, output_dir: str):
    """
    Creates videos from images

    :params:
        :param input_dir: dir with resized images
        :param output_dir: dir where videos will be saved
    """
    save_dir = create_dir(output_dir)
    for catalog in os.listdir(input_dir):
        process = f'ffmpeg -i {input_dir}{catalog}/000%02d.jpg -framerate 20 {save_dir}{catalog}.mp4 -y'
        os.system(process)


def merge_videos_ffmpeg(input_dir: str, output_dir: str):
    """
    Creates final video from videos

    :params:
        :param input_dir: dir with videos
        :param output_dir: output dir where final video will be saved
    """
    list_of_files = os.listdir(input_dir)
    num_of_files = len(list_of_files)
    input_string = ''
    for file in list_of_files:
        input_string += f'-i {input_dir}{file} '
    process = f'ffmpeg {input_string} -filter_complex concat=n={num_of_files}:v=1:a=0 -an {output_dir}result.mp4 -y'
    os.system(process)


# Replace with the URL of the archive you want to download
url = "https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-Unsupervised-trainval-480p.zip"

# --------------------------- DIRECTORIES ---------------------------
input_directory = 'input/'
annotations_dir = 'input/DAVIS/Annotations_unsupervised/480p/'  # depends on the hierarchy in the archive
source_images_dir = 'input/DAVIS/JPEGImages/480p/'  # depends on the hierarchy in the archive
output_main_dir = 'output/'
prepared_annotations_dir = 'output/prepared_annotations/'
masked_images_dir = 'output/masked_images/'
contours_dir = 'output/contours/'
contoured_images_dir = 'output/contoured_images/'
resized_images_dir = 'output/resized_images/'
videos_dir = 'output/videos/'


# ---------------------------- EXECUTION ----------------------------
if __name__ == "__main__":
    for folder in [input_directory, output_main_dir]:
        create_dir(folder)

    while not does_input_data_exist(input_directory):
        input("There is no data to process. Place 'DAVIS' folder from archive in 'input' folder and press Enter.")

    check_input_data_consistency()
    remove_black_background_in_annotation(annotations_dir, prepared_annotations_dir)
    merge_image_and_annotation_opencv(source_images_dir, prepared_annotations_dir, masked_images_dir)
    create_contour_for_annotation(prepared_annotations_dir, contours_dir)
    merge_image_and_contour_pil(masked_images_dir, contours_dir, contoured_images_dir)
    min_width_px = get_min_width_of_images(contoured_images_dir)
    resize_prepared_jpgs(contoured_images_dir, resized_images_dir, min_width_px)
    convert_sequence_to_video(resized_images_dir, videos_dir)
    merge_videos_ffmpeg(videos_dir, output_main_dir)
