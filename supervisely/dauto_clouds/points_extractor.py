import os
import numpy as np
from kitti_util import Calibration, read_label, load_velo_scan
import logging

logging.basicConfig(level=logging.INFO)


def get_points_cloud_array(file_name: str) -> np.ndarray:
    # Open the file in binary mode
    with open(file_name, "rb") as f:
        # Read the data as a byte stream
        byte_data = f.read()

        # Calculate the expected number of points and bytes
        expected_num_points = len(byte_data) // 16  # 4 values per point (x, y, z, intensity), each 4 bytes
        expected_num_bytes = expected_num_points * 16

        if len(byte_data) != expected_num_bytes:
            raise ValueError(f"Invalid file size: expected {expected_num_bytes} bytes but found {len(byte_data)} bytes")

        # Unpack the data into a numpy array of floats
        point_cloud = np.frombuffer(byte_data, dtype=np.float32).reshape(expected_num_points, 4)

    # The resulting array has four columns: x, y, z, and intensity
    return point_cloud


def is_point_inside_cuboid(point, cuboid):
    cuboid_min = np.min(cuboid, axis=0)
    cuboid_max = np.max(cuboid, axis=0)
    return np.all(point[:3] >= cuboid_min) and np.all(point[:3] <= cuboid_max)


def extract_points_inside_cuboids(point_cloud, cuboids):
    output_point_cloud = []
    for cuboid in cuboids:
        cuboid_corners = np.array(cuboid)
        for point in point_cloud:
            if is_point_inside_cuboid(point, cuboid_corners):
                output_point_cloud.append(point)
    return np.array(output_point_cloud)


def roty(t):
    """ Rotation about the y-axis. """
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def compute_box_3d(obj):
    """ Takes an object and projects the 3d bounding box into the image plane.
        Returns:
            corners_3d: (8,3) array in in rect camera coord.
    """
    # compute rotational matrix around yaw axis
    R = roty(obj.ry)

    # 3d bounding box dimensions
    l = obj.l
    w = obj.w
    h = obj.h

    # 3d bounding box corners
    x_corners = [l / 2, l / 2, -l / 2, -l / 2, l / 2, l / 2, -l / 2, -l / 2]
    y_corners = [0, 0, 0, 0, -h, -h, -h, -h]
    z_corners = [w / 2, -w / 2, -w / 2, w / 2, w / 2, -w / 2, -w / 2, w / 2]

    # rotate and translate 3d bounding box
    corners_3d = np.dot(R, np.vstack([x_corners, y_corners, z_corners]))
    # print corners_3d.shape
    corners_3d[0, :] = corners_3d[0, :] + obj.t[0]
    corners_3d[1, :] = corners_3d[1, :] + obj.t[1]
    corners_3d[2, :] = corners_3d[2, :] + obj.t[2]

    return np.transpose(corners_3d)


def write_car_points_bin(point_cloud, car_number, output_dir):
    # Open the file in binary mode
    file_name = f'car{car_number}.bin'
    os.chdir(output_dir)
    with open(file_name, "wb") as f:
        # Convert the array to a binary string and write it to the file
        f.write(point_cloud.tobytes())
    os.chdir('../')


label_2_path = 'data/object/training/label_2/000010.txt'
calib_path = 'data/object/training/calib/000010.txt'
velodyne_path = 'data/object/training/velodyne/000010.bin'
output = 'output/'

if __name__ == "__main__":
    points_cloud = load_velo_scan(velodyne_path)
    calib = Calibration(calib_path)
    objects = read_label(label_2_path)
    n = 1
    cars_points = np.empty(4, dtype=np.float32)
    for label_object in objects:
        if label_object.type == 'Car':
            logging.info(f'Collecting points for car №{n}')
            box3d_pts_3d = compute_box_3d(label_object)
            box3d_pts_3d_velo = calib.project_rect_to_velo(box3d_pts_3d)
            extracted_points = extract_points_inside_cuboids(points_cloud, [box3d_pts_3d_velo])
            write_car_points_bin(extracted_points, n, output)
            n += 1
            cars_points = np.vstack((cars_points, extracted_points))
    write_car_points_bin(cars_points, '_all', output)
    logging.info(f'Collecting points finished')
