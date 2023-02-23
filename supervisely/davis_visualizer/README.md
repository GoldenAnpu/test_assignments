## Write a visualizer for a dataset <a href="https://davischallenge.org/">DAVIS</a>
The script should work as follows:
 - Create N videos using dataset
 - Concatenate them <a href="https://davischallenge.org/images/DAVIS-2017-TrainVal.mp4">either sequentially</a> or in <a href="https://davischallenge.org/images/teaser/montage-2017.jpg">a grid</a>

### Questions
 - Which dataset from the possible ones in DAVIS should be processed?
   - **Answer:** on my own
   - Specific: write which of the three
   - There should be the possibility to process any dataset
 - What should be the size of the output video if the sizes of the images in the input dataset are different?
   - **Answer:** on my own
   - Based on the image with lower resolution
   - Based on the image with higher resolution
   - Strictly like in the example
   - Other: specify in the answer
 - For visualization in a grid of 2x2, how should the videos be grouped?
   - Random
   - **Answer:** sequentially along X and row by row
   - Video fragments should be composed so that the lengths of the videos in each cell are as close as possible
 - If videos in all cells should end synchronously, can this be achieved through different frame rates?
   - Yes
   - No
   - **Answer:** They can end asynchronously, and in that case, we leave black space for short videos until the longest one finishes.

### Implementation

#### Environment
 - Windows 11
 - <a href="https://github.com/GyanD/codexffmpeg/releases/tag/2023-02-19-git-2aec86695a">ffmpeg 2023-02-19-git-2aec86695a<a>

#### Packages 
 - <a href="https://pypi.org/project/opencv-python/">opencv-python 4.7.0.72</a>
 - <a href="https://pypi.org/project/numpy/">numpy 1.24.2</a>
 - <a href="https://pypi.org/project/Pillow/">Pillow 9.4.0</a>

#### How visualizer.py works
1. Creates folders "input" and "output".
2. Waits for the input data to be placed in the "input" folder.
   * **current:** by hands 
   * using downloader and unzipper
3. Checks input data consistency(annotations for each image) by existence of relevant subdirs
4. Removes the black background from the source annotations and save to "output/prepared_annotations".
5. Creates internal contour files for all annotations and save them to "output/contours".
6. Applies annotations to source images and save to "output/masked_images".
7. Applies contour for every annotated images and save to "output/contoured_images".
8. Gets min width in px of all images.
9. Resizes all images with contours to this width while maintaining aspect ratios and add black borders at the top/bottom. Saves to "output/resized_images".
10. Combines image sequences from subdirs into videos and save in "output/videos".
11. Merge all videos into one stream and save to "output" as "result.mp4".

#### Results and Thoughts:
* For the **3**rd paragraph, it would be great to check file by file in subdirs
* It would be better for annotations to be segmented by color,then contours can be created for each color.
* The image size adjusted to the smallest size since some types loses quality when enlarged.
* The resulting video assembled by merging separately created clips 
since this approach better than creation from summ of image sequences for example.
* The input directories can be set automatically by reading the hierarchy in the archive.
* Directories for unnecessary output files should be removed.
* Using the pre-installed ffmpeg in the working environment is not the best approach, but it was used because the system was already configured. If the script was running from Docker, it could be left as is, otherwise it would be more convenient to implement it through the Python package ffmpeg.
* The contour is only drawn for the external area of the mask, and on objects where there are empty areas inside the mask, the outline is absent.
* Visualization with grid 2x2 wasn't implemented due to the inability to achieve the required result. For now  :) 


### Development process and spent time
1. Developing/Modifying file processing flowchart: 65 minutes
2. Researching relevant information on libraries that work with images: 90 minutes
3. Code writing: 90 minutes
4. Clarification of questions: 10 minutes
5. Making changes: 20 minutes
6. Debugging/Testing: 90 minutes
7. Refactoring: 65 minutes
8. Preparing report: 40 minutes

Overall max: 470 minutes ~ 7.8 hours