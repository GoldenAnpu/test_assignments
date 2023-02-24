## Write extractor of annotated points from 3D cloud 
Take any public dataset with 3D point clouds that have annotated cars on them (for example, Waymo, NuScenes, or KITTI3D). 

The script should work as follows:
* using the car annotations in the form of cuboids, will points from the source point cloud 
* save them as separate point clouds

### Questions
* Should it be extracted from a single scene or do we need to process a sequence of scenes?
  * From a single scene
  * From a sequence of N scenes
  * **Answer:** on my own 
* Do we need to keep the coordinate system of the main scene for the extracted point clouds upon saving, or will it just be a point cloud in a new scene with a volume equal to the cuboid?
  * Attach to the main scene
  * **Answer:** Attach to the cuboid

### Implementation


#### Environment
 - Windows 11
 - <a href="https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d">KITTY3D dataset</a>
 - <a href="https://github.com/kuixu/kitti_object_vis">kitti_object_vis</a> for visualization 

#### Packages 
 - <a href="https://pypi.org/project/numpy/">numpy 1.24.2</a>
 - <a href="https://github.com/kuixu/kitti_object_vis/blob/12ce0a2348f6e1405c502bf32e51d76d3a970396/kitti_util.py">kitty_util.py</a>


#### How extractor.py works
1. Creates folders named "input" and "output".
2. Waits for input data to be placed in the "input" folder from the archives of the KITTI3D dataset. **NOTE:** Please, define the scene files in variables.
3. Loads source points from .bin, calibration information, and labeling information from .txt as a list of Object3D.
4. Creates an empty array to store the output result cloud with all cars that will be visualized in the chosen scene.
5. Computes cuboids for all 'Car' in the list of Object3D.
6. Converts every cuboid from camera coordinates into velocity coordinates.
7. Extracts all 'Car' points that are inside the cuboids and saves them in the output .bin file for that 'Car'.

Checkout file kitty_utils.py into main dir using link from **Packages**
To check the results, you can replace input "{scene_number}.bin" with output "car_n.bin", rename it with the scene number, and visualize it. 


#### Results and Thoughts:
 - External tools were used to work with the KITTI3D dataset to solve tasks related, for example, to matrices and correct extracting of points relative to the calib parameters.
 - The result is checked through visualization, which does not guarantee that all points are found or that there are no extra points found.
 - When saving all car points to a common output file, some points outside the cuboids may be visible during visualization.


### Development process and spent time
1. Developing/Modifying file processing flowchart: 25 minutes
2. Researching relevant information on libraries that work with LiDAR clouds: 300 minutes
3. Code writing: 60 minutes
4. Clarification of questions: 10 minutes
5. Making changes: -
6. Debugging/Testing: 75 minutes
7. Refactoring: 30 minutes
8. Preparing report: 30 minutes

Overall max: 530 minutes ~ 8.8 hours