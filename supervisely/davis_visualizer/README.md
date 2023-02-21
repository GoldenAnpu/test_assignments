### Write a visualizer for a dataset <a href="https://davischallenge.org/">DAVIS</a>
The script should work as follows:
 - Take N videos and concatenate them into one video
 - Concatenate them <a href="https://davischallenge.org/images/DAVIS-2017-TrainVal.mp4">either sequentially</a> or in <a href="https://davischallenge.org/images/teaser/montage-2017.jpg">a grid</a>

#### Questions
 - Which dataset from the possible ones in DAVIS should be processed?
   - **Answer:** at my discretion
   - Specific: write which of the three
   - There should be the possibility to process any dataset
 - What should be the size of the output video if the sizes of the images in the input dataset are different?
   - **Answer:** at my discretion
   - Based on the image with lower resolution
   - Based on the image with higher resolution
   - Strictly like in the example
   - Other: specify in the answer
 - For visualization in a grid of x4, how should the videos be grouped?
   - Random
   - **Answer:** sequentially along X and row by row
   - Video fragments should be composed so that the lengths of the videos in each cell are as close as possible
 - If videos in all cells should end synchronously, can this be achieved through different frame rates?
   - Yes
   - No
   - **Answer:** They can end asynchronously, and in that case, we leave black space for short videos until the longest one finishes.

#### Implementation:
1. Load the dataset into the input.
   1. by hands
   2. write downloader and unzipper
2. Check the presence of annotations for each image.
3. Remove the black background from the source annotations and save to a new folder.
4. Create internal contour files for all annotations and save to a new folder.
5. Apply annotations to images and save to a new folder.
6. Overlay contours on annotated images from step 4 and save to a new folder.
7. Resize all images with contours to the same width while maintaining aspect ratios and add black borders at the top/bottom. Save to a new folder.
8. Combine all images into videos.
9. Merge all videos into one stream.

#### Thoughts:
 - Annotations can be segmented by color and contours can be created for each color.
 - The image size can be adjusted to the smallest size since JPEG loses quality when enlarged.
 - The resulting video can be assembled by merging separately created clips since this approach is the simplest for the user.
 - The input directories can be set automatically by reading the hierarchy in the archive.
 - Directories for unnecessary output files should be removed.