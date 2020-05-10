
import os
import glob
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

method = 'ORB'
lowe_ratio = 100
summy = 0
dist = 0
images = []
matchfound = 0




def ORBdetectormatcher(imginput,imgtest):

   summy = 0
   img3 = []
   list_kp1 = []
   list_kp2 = []
   list_dec = []
   finder = cv.ORB_create()
   gr1=cv.cvtColor(imginput,cv.COLOR_BGR2GRAY)
   gr2=cv.cvtColor(imgtest,cv.COLOR_BGR2GRAY)
   kp1, des1 = finder.detectAndCompute(gr1,None)
   kp2, des2 = finder.detectAndCompute(gr2,None)
   bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
   matches = bf.match(des1,des2)
   for mat in matches:

       # Get the matching keypoints for each of the images
       imginput_idx = mat.queryIdx
       imgtest_idx = mat.trainIdx

       # x - columns
       # y - rows
       # Get the coordinates
       (x1,y1) = kp1[imginput_idx].pt
       (x2,y2) = kp2[imgtest_idx].pt
       if mat.distance < lowe_ratio:
           list_kp1.append((x1, y1))
           list_kp2.append((x2, y2))


   cam = [[426.05754,0.00000 ,256.50000],[0.00000, 426.05754 ,256.50000],[0.00000 ,0.00000 ,1.00000]]
   list_dec = list(np.array(list_kp1) - np.array(list_kp2))
   E, mask = cv.findEssentialMat(np.array(list_kp1), np.array(list_kp2), focal=426.05754, pp=(256.50000,256.50000), method=cv.RANSAC, prob=0.999, threshold=1.0)
   points, R, t, maskRP = cv.recoverPose(E,np.array(list_kp1),np.array(list_kp2),mask=mask)
   R1, R2, t = cv.decomposeEssentialMat(E)
   print "Translation in x:"
   print t[0], " " ,t[1]
   print "Translation in y"
   print t[2]

fnam_nav = r"/home/varsh/image1.png"
fnam_map = r"/home/varsh/image2.png"
navimage = cv.imread(fnam_nav,1)
mapimage = cv.imread(fnam_map,1)
#cv.waitKey(0)

ORBdetectormatcher(navimage,mapimage)


#if matchfound !=1:
#cv.waitKey(0)
#if matchfound == 0:
#  ORBGROUPMATCHA(imginput,mapptno)
#cv.waitKey(0)
