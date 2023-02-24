import os
import numpy as np
from kitti_util import Calibration, Object3d, read_label, load_velo_scan
import logging

logging.basicConfig(level=logging.INFO)


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


def does_input_data_exist(input_directory: str) -> bool:
    """
    Checks input directory for data existence

    :params:
    :param input_directory: input directory with data
    :return: "True" if it exists, "False" if it doesn't
    """
    return bool(os.listdir(input_directory))


# not used
def get_points_cloud_array(file_name: str) -> np.ndarray:
    """
    Loads all points in scene from the LiDAR .bin file
    :params:
        :param file_name: .bin file name
        :return: array with all points
    """
    # Open the file in binary mode
    with open(file_name, "rb") as file:
        # Read the data as a byte stream
        byte_data = file.read()
        # Calculate the expected number of points and bytes
        expected_num_points = len(byte_data) // 16  # 4 values per point (x, y, z, intensity), each 4 bytes
        expected_num_bytes = expected_num_points * 16

        if len(byte_data) != expected_num_bytes:
            raise ValueError(f"Invalid file size: expected {expected_num_bytes} bytes but found {len(byte_data)} bytes")

        # Unpack the data into a numpy array of floats
        point_cloud = np.frombuffer(byte_data, dtype=np.float32).reshape(expected_num_points, 4)

    # The resulting array has four columns: x, y, z, and intensity
    return point_cloud


def is_point_inside_cuboid(point: np.ndarray, cuboid: np.ndarray) -> bool:
    """
    Check all point coordinates inside a given cuboid

    :params:
        :param point: one point coordinates
        :param cuboid: cuboid corners
        :return: check all coordinates inside a given cuboid, if yes returns True
    """
    cuboid_min = np.min(cuboid, axis=0)
    cuboid_max = np.max(cuboid, axis=0)
    return np.all(point[:3] >= cuboid_min) and np.all(point[:3] <= cuboid_max)


def extract_points_inside_cuboids(point_cloud: np.ndarray, cuboids: list[np.ndarray]) -> np.ndarray:
    """
    Extracts the points inside the cuboid one at a time and stores it in the output array

    :params:
        :param point_cloud: cloud of points
        :param cuboids: cuboids for all cars
        :return: new cloud as array with points for one "Car"
    """
    output_point_cloud = []
    for cuboid in cuboids:
        cuboid_corners = np.array(cuboid)
        for point in point_cloud:
            if is_point_inside_cuboid(point, cuboid_corners):
                output_point_cloud.append(point)
    return np.array(output_point_cloud)


def rotation_y(t: float) -> np.ndarray:
    """ Rotation about the y-axis

    :params:
        :param t: Rotation ry around Y-axis in camera coordinates [-pi..pi]
    """
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def compute_box_3d(obj: Object3d) -> np.ndarray:
    """ Takes an object and projects the 3d bounding box into the image plane.
    :params:
    :param obj: labeled object with parameters from 'label_2'
    :return: corners_3d - (8,3) array in rect camera coord.
    """
    # compute rotational matrix around yaw axis
    r = rotation_y(obj.ry)

    # 3d bounding box dimensions
    l = obj.l
    w = obj.w
    h = obj.h

    # 3d bounding box corners
    x_corners = [l / 2, l / 2, -l / 2, -l / 2, l / 2, l / 2, -l / 2, -l / 2]
    y_corners = [0, 0, 0, 0, -h, -h, -h, -h]
    z_corners = [w / 2, -w / 2, -w / 2, w / 2, w / 2, -w / 2, -w / 2, w / 2]

    # rotate and translate 3d bounding box
    corners_3d = np.dot(r, np.vstack([x_corners, y_corners, z_corners]))
    # print corners_3d.shape
    corners_3d[0, :] = corners_3d[0, :] + obj.t[0]
    corners_3d[1, :] = corners_3d[1, :] + obj.t[1]
    corners_3d[2, :] = corners_3d[2, :] + obj.t[2]

    return np.transpose(corners_3d)


def write_car_points_bin(point_cloud: np.ndarray, car_number: int | str, output_path: str):
    """
    Saves points as .bin file

    :params:
        :param point_cloud: array with points
        :param car_number: id for file naming
        :param output_path: output dir
    """

    # Open the file in binary mode
    file_name = f'car_{car_number}.bin'
    os.chdir(output_path)
    with open(file_name, "wb") as f:
        # Convert the array to a binary string and write it to the file
        f.write(point_cloud.tobytes())
    os.chdir('../')


input_dir = 'input/'
label_2_path = 'input/training/label_2/000010.txt'
calib_path = 'input/training/calib/000010.txt'
velodyne_path = 'input/training/velodyne/000010.bin'
output_dir = 'output/'

if __name__ == "__main__":
    [create_dir(folder) for folder in [input_dir, output_dir]]

    while not does_input_data_exist(input_dir):
        input("There is no data to process. Place data in 'input' folder and press Enter.")

    points_cloud = load_velo_scan(velodyne_path)  # loads all points in scene from the LiDAR .bin file
    calib = Calibration(calib_path)  # loads calibration data from .txt file in 'calib'
    objects = read_label(label_2_path)  # loads objects using .txt file from 'label_2'
    n = 1
    cars_points = np.empty(4, dtype=np.float32)  # one row ndarray for saving points of all cars into one cloud
    for label_object in objects:
        if label_object.type == 'Car':
            logging.info(f'Collecting points for car #{n}')
            box3d_pts_3d = compute_box_3d(label_object)
            box3d_pts_3d_velo = calib.project_rect_to_velo(box3d_pts_3d)
            extracted_points = extract_points_inside_cuboids(points_cloud, [box3d_pts_3d_velo])
            write_car_points_bin(extracted_points, n, output_dir)
            n += 1
            cars_points = np.vstack((cars_points, extracted_points))
    cars_points = np.delete(cars_points, 0, axis=0)  # delete first row from array which is not a part of source points
    write_car_points_bin(cars_points, '_all', output_dir)  # to check visually
    logging.info(f'Collecting points finished')
