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


#### How extractor.py works


#### Results and Thoughts:



### Development process and spent time
1. Developing/Modifying file processing flowchart: 
2. Researching relevant information on libraries that work with images: 
3. Code writing: 
4. Clarification of questions: 
5. Making changes: 
6. Debugging/Testing: 
7. Refactoring: 
8. Preparing report: 

Overall max: 