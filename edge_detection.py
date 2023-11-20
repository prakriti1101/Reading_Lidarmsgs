#!/usr/bin/env python

import rospy
import cv2
import os   
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt  
import numpy as np          

# first load images - path to the image 

img_path= os.path.join('/home/prakriti/nav_ws/src/quaternion/Task2/images/image1.jpg')
img1= cv2.imread(img_path)

# cv2.imshow('view image 1', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

blur=cv2.GaussianBlur(img1, (5,5), 0)
canny=cv2.Canny(blur, threshold1=50, threshold2=150)    #apply canny edge detection algorithm
cv2.imshow('view image 1', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


h1=img1.shape[0]    #174
w1=img1.shape[1]    #175
print(h1,w1)

# Find lines using Hough Transform
lines = cv2.HoughLinesP(canny, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

if lines is not None:
     
    for line in lines:
        x1, y1, x2, y2 = line[0]

        # if 20 <= x1 < 164 and 10 <= x2 < 170 and 20 <= y1 < 164 and 20 <= y2 < 164:

        print(line)
        cv2.line(canny, (87, 87), (87, 87), (0, 255, 0), 2)

    cv2.imshow('view image 2', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #  Calculate offset and angle of deviation for a straight line from the center of an image
    offset = img1.shape[1] / 2 - (x1 + x2) / 2

    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi

    print(img1, angle)

else:
    # If no lines are detected, assume the robot is at a junction
    print(img1, None, None)

