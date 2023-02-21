### Write two scripts: split and merge.
The **split** script takes an image as input and cuts the image into fragments using the sliding window approach:
 - window size (h, w) in pixels or as a percentage
 - x and y offsets
 - the result is saved in a directory
 - all settings should be included in the names of the resulting images. 
  
 The **merge** script takes a directory containing the segmented images and combines them to reconstruct the original image.

It is necessary to **verify** that the **pixels** in the resulting image match the original image exactly.

#### Questions
- What should the sliding window behavior be:
  - Add a border when the edges are reached.
  - **Answer:** Shift the window along the axes inside the image to obtain a fragment that is the same size as the window.

#### Thoughts
- Provide the option to process with or without a border: implement this in both split and merge.
- Different file extensions need to be handled differently in split.
  - Either create a handler for different file types.
  - Or convert all files to a single type, such as png.
- Clear the output_split folder to avoid errors when merging.
  - Do this during the split phase so that we can inspect the fragments after merging.
  - Do this after a successful merge since the images are identical, and we don't need the fragments anymore.
  - Do this with a separate command since we may need the fragments for annotations, for example.