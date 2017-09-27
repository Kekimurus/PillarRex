import cv2
import numpy as np
import math
import argparse
from matplotlib import pyplot as plt

#img = cv2.imread('open_cv_logo.png',0)
img = cv2.imread('testMed.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
ret,thresh = cv2.threshold(img, 200, 255,cv2.THRESH_BINARY)
c2img = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=100,param2=10,minRadius=24,maxRadius=33)

#print(circles)

circlesNumpy = np.array(circles[0])
circles[0] = circlesNumpy[circlesNumpy[:,0].argsort()]
print(circles)

circles = np.uint16(np.around(circles))

prevCircX = 0
prevCircY = 0
iteration = 0

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    #cv2.circle(c2img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    if iteration >= 1 and iteration != 0 and i[1] > prevCircY:
        cv2.line(cimg, (prevCircX, prevCircY), (i[0], i[1]), (255, 0, 0), 5)
    prevCircX = i[0]
    prevCircY = i[1]
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    #cv2.circle(c2img, (i[0], i[1]), 2, (0, 0, 255), 3)
    iteration = iteration + 1

cv2.imwrite('detection.png', cimg)
#cv2.imshow('detected circles',cimg)

titles = ['Orig Img','Thresh Img']
images = [cimg, c2img]

#plt.imshow(cimg, cmap = 'gray', interpolation = 'bicubic')
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
