# OpenCV-Image-Cartoonization

The process of converting an RGB image into cartoons with **opencv** library.


# Running Process

To convert an image to cartoons, run the following command to run it:
 1. Importing libraries
 2. Defining the function
 - A function that get an image as inputs and produce the cartoon version of it.
 3. Smoothing image
 - downscaling
 - bilateral filter
 - upscaling
 4. Converting into greyscale & applying the medium blur
 - RGB to Grey
 - medianBlur
 5. Detect  edges
 - adaptiveThreshold
 6. Again converting back to RGB format
 
 
#### Running in terminal

To convert an image to cartoons, you only have to replace **dog_image.jpg** in following command, with your image and then run the command in terminal : 

	$ python image_cartoonizer.py dog_image.jpg 
 


## Required packages

- **cv2**  and **numpy** library
> install this package first with pip command

    $ pip install opencv-python
    $ pip install numpy

## Contributing

### Step 1

-   **Option 1**
    
    -    Fork this repo!
-   **Option 2**
    
    -    Clone this repo to your local machine using `https://gitlab.com/ai4fun/image-processing/cartoonizing/opencv_python.git`
### Step 2

-   **HACK AWAY!** 🔨

### Step 3

-   🔃 Create a merge request


## Sample

The following figure shows the project steps on an image :

![plot](https://github.com/aliaminibagh/image-cartoonizing/blob/master/Cartoonization2.png)
