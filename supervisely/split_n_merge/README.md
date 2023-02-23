## Write two scripts: split and merge.
The **split** script takes an image as input and cuts the image into fragments using the sliding window approach:
 - window size (h, w) in pixels or as a percentage
 - x and y offsets
 - the result is saved in a directory
 - all settings should be included in the names of the resulting images. 
  
 The **merge** script takes a directory containing the segmented images and combines them to reconstruct the original image.

It is necessary to **verify** that the **pixels** in the resulting image match the original image exactly.


### Questions
- What should the sliding window behavior be:
  - Add a border when the edges are reached.
  - **Answer:** Shift the window along the axes inside the image to obtain a full fragment that is the same size as the window.


### Implementation
#### Environment
 - Windows 11

#### Packages 
 - <a href="https://pypi.org/project/opencv-python/">opencv-python 4.7.0.72</a>
 - <a href="https://pypi.org/project/numpy/">numpy 1.24.2</a>

#### How split.py works
1. Creates folders "input" and "output_split".
2. Waits for the input data to be placed in the "input" folder.
3. If data exists, the script sets the "input" directory as the current working directory.
4. Gets the names of all image files in this directory and stores them in a list.
5. Receives input of sliding window parameters. All parameters are by default in pixels, but users can define percentages for window size.
6. Checks if the parameters are logically correct; otherwise, brings them to acceptable values. The window size must be lower than the image size, and the offset can't be bigger than the window size.
7. Creates the "output_split" folder and makes it the working directory.
8. For each image file, creates a sub folder in "output_split" with the image name for its pieces and store the file type in its own name to cover intersections of files with the same name but different types.
9. Changes the working directory to the image sub folder.
10. For every window, creates a piece of the image file and saves it with parameters in names according to the following pattern:
    <pre>offs_y_{y}_x_{x}__win_h_{h}_w_{w}__origsize_h_{image_h}_w_{image_w}_{img_file}</pre>
    where:
     - x, y - offsets
     - h, w - window sizes
     - image_h, image_w - sizes of source image
     - img_file - source image name with file type
11. Changes the working directory back to "input" and starts processing the next source image file.

#### How merge.py works
12. Creates a folder "output_merged" if it doesn't exist.
13. Gets the names of all folders in the "output_split" directory and stores them in a list.
14. For every folder, gets the names of all files in the directory and stores them in a list.
15. From the first file name, gets the "constant" parameters by template from step **10**.
16. Using these parameters, creates a canvas with sizes of the source file from "input."
17. Loops through pieces of the image and gets their offsets from file names and pastes these pieces into the canvas.
18. Saves the image and checks the difference between the source file from "input" and the saved one.

### Results and Thoughts
* For the **4**th paragraph, it would be great to add a check for files that OpenCV can handle.
* For the **5**th paragraph, it would be great to add a switch to choose how to use parameters for the rest of the images.
* Add an option to choose the sliding window type (with or without a border) and implement it in both the split and merge scripts.
* Add directory cleanup for the "output_split" folder to avoid errors when merging:
  * On every run of "split.py", make it possible to inspect fragments after merging.
  * After a successful merge, since the images are identical, we don't need their fragments anymore.
  * As an additional option, add the ability to keep the fragments for annotations, for example.


### Development process and spent time
1. Developing/Modifying file processing flowchart: 35 minutes
2. Researching relevant information on libraries that work with images: 60 minutes
3. Code writing: 40 minutes
4. Clarification of questions: 10 minutes
5. Making changes: 20 minutes
6. Debugging/Testing: 40-60 minutes
7. Refactoring: 50 minutes
8. Preparing report: 40 minutes
Overall max: 315 minutes = 5.25 hours

