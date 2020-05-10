
import os
import glob
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

method = 'ORB'
lowe_ratio = 0.89
summy = 0
dist = 0
images = []
matchfound = 0

def ORBGROUPMATCHER(imginput, ptno):

  #checkpt = ptno-2
  for i in range(ptno-2, ptno+2):
    checkpt = i
    if checkpt < 10:
      path = '/home/varsh/mapimgs/image00%d.jpeg' % checkpt
    elif checkpt >= 10:
      path = '/home/varsh/mapimgs/image000%d.jpeg' % checkpt

    imgtest = cv.imread(path)
    ORBdetectormatcher(imginput, imgtest, checkpt)


   #head_tail = os.path.split(path)
   #print("Tail of %s is " %path, head_tail[1])
   #imgtest = cv.imread(imgs)

   #imgtest = cv.cvtColor(img, cv.COLOR_BGR2GRAY, 3)
   #images.append(imgtest)
   #ORBdetectormatcher(imginput, imgtest, ptno)

def ORBSINGLEMATCHER(navimage,mapptno):
   # no error case, aka using mappt to search database for image, searched map img matches nav image
   if mapptno < 10:
    fnam_map = r"/home/varsh/mapimgs/image000%d.jpeg" % mapptno
   elif mapptno >= 10:
    fnam_map = r"/home/varsh/mapimgs/image00%d.jpeg" % mapptno
   mapimage = cv.imread(fnam_map,1)
   cv.imshow('map image corresponding to the navigation image',mapimage)
   #cv.waitKey(0)
   #finding orb match
   ORBdetectormatcher(navimage,mapimage,mapptno)

def ORBdetectormatcher(imginput,imgtest,ptno):

   summy = 0
   img3 = []
   list_kp1 = []
   list_kp2 = []
   list_dec = []
   finder = cv.ORB_create()
   kp1, des1 = finder.detectAndCompute(imginput,None)
   kp2, des2 = finder.detectAndCompute(imgtest,None)
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

       list_kp1.append((x1, y1))
       list_kp2.append((x2, y2))


   list_dec = list(np.array(list_kp1) - np.array(list_kp2))
   #print("DECISION LIST", list_dec)

   lengy = len(list_dec)
   lenlist1 = len(kp1)
   lenlist2 = len(kp2)
   print("\nNO. OF FEATURES DETECTED IN IMAGE1 AND IMAGE2",lenlist1,lenlist2)
   #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 1 \n",list_kp1)
   #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 2 \n",list_kp2)


   for k in range(lengy):
       summy+=list_dec[k][0]
   print("\nORB DECISION SCORE",summy)
   if summy < 0:
       print("\nIMAGE DATA SHOWS LEFT SHIFT ERROR")
       print("MOVE RIGHT")
   elif summy > 0:
       print("\nIMAGE DATA SHOWS RIGHT SHIFT ERROR")
       print("MOVE LEFT")
   elif summy == 0:
       print("\nMATCH!")
   good = []

   for m in matches:
       if m.distance < lowe_ratio:
           good.append([m])
   msg2 = 'There are %d good matches HA' % (len(good))
   matchscore = len(good) / (max(lenlist1,lenlist2))

   img3 = cv.drawMatches(imginput,kp1,imgtest,kp2,matches[:(len(good))],None,flags=2)

   font = cv.FONT_HERSHEY_SIMPLEX
   cv.putText(img3,msg2,(10, 270), font, 0.5,(255,255,255),1,cv.LINE_AA)
   fname = 'output_%s_%.2f.png' % (method, lowe_ratio)
   cv.imwrite(fname, img3)

   print("ORB MATCHES", len(good))
   print("MATCH SCORE",matchscore)
   if matchscore > 0.65:
      #print(imgtest)
      global matchfound
      matchfound = 1
      print("YOU are at node", ptno)
      print("\nNO. OF FEATURES DETECTED IN IMAGE1 AND IMAGE2",lenlist1,lenlist2)
      #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 1 \n",list_kp1)
      #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 2 \n",list_kp2)
      cv.imshow('matches',img3)
      cv.waitKey(1000)


mapptno =


navimage = 
cv.imshow('image captured during navigation',navimage)
#cv.waitKey(0)

ORBSINGLEMATCHER(navimage,mapptno)

if matchfound != 1:
   print('hm match not found')
   print('You may not be at node', mapptno)
   print('Checking with nearby nodes')
   ORBGROUPMATCHER(navimage,mapptno)

#if matchfound !=1:
#cv.waitKey(0)
#if matchfound == 0:
#  ORBGROUPMATCHA(imginput,mapptno)
#cv.waitKey(0)
