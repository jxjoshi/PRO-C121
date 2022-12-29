# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480


while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([0, 120, 50])
        upper_bound = np.array([10, 255,255])

        #Open and expand the image where there is mask 1 (color)
        mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        mask_2=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    #Selecting only the part that does not have mask one and saving in mask 2
    mask_2=cv2.bitwise_not(mask_1)

    #Keeping only the part of the images without the red color 
    #(or any other color you may choose)
    res_1 = cv2.bitwise_and(img, img, mask=mask_2)

    #Keeping only the part of the images with the red color
    res_2 = cv2.bitwise_and(bg, bg, mask=mask_1)

    #Generating the final output
    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    output_file.write(final_output)
    cv2.imshow('Magic',final_output)

        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
