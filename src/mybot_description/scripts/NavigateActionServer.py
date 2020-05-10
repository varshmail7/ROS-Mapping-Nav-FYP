#! /usr/bin/env python
import rospy
import actionlib
from mybot_description.msg import NavigateAction, NavigateActionFeedback, NavigateActionResult, NavigateActionGoal, NavigateResult
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from sensor_msgs.msg import Image
from math import pow, atan2, sqrt
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import cv2 as cv
from cv_bridge import CvBridge, CvBridgeError
import time

lowe_ratio = 100
matchfound =0
summy_x = 0

class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        # rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/odom',
                                                Odometry, self.update_pose)

        self.pose = Pose()
        self.thetaerror = 0
        self.integralError = 0
        self.error = 0
        self.image_x = 0
        self.image_y = 0
        self.goal_pose = Pose()
        self.rate = rospy.Rate(10)

    def set_image_dimensions(self,image):
        self.image_x = image.width
        self.image_y = image.height

    def get_image_dimensions(self):
        return self.image_x,self.image_y

    def navigateImageCheck(self,image):

        self.set_image_dimensions(image)
        mapptno = mapPointID
        bridge = CvBridge()
        navimage = bridge.imgmsg_to_cv2(image, desired_encoding="passthrough")
        # navpath = r"/home/varsh/mapimgs/nav000%d.jpeg" % mapptno
        # cv.imwrite(navpath,navimage)
        #cv.waitKey(0)

        res = ORBSINGLEMATCHER(self,navimage,mapptno)
        global matchfound
        if matchfound > 0.65:
            print("Match!")
            return 1
        else:
            return 0

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.calc_error(data)
        self.pose.x = data.pose.pose.position.x
        self.pose.y = data.pose.pose.position.y
        orlist = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (r,p,y) = euler_from_quaternion(orlist)
        self.thetaerror = self.pose.theta - y
        self.pose.theta = y
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        self.pose.theta = round(self.pose.theta, 4)

        self.pose.linear_velocity = data.twist.twist.linear.x
        self.pose.angular_velocity = data.twist.twist.angular.z

    def calc_error(self,data):
        data.pose.pose.position.x = round(data.pose.pose.position.x, 4)
        data.pose.pose.position.y = round(data.pose.pose.position.y, 4)
        self.error = sqrt(pow((self.goal_pose.x - self.pose.x), 2) + pow((self.goal_pose.y - self.pose.y), 2)) - sqrt(pow((self.goal_pose.x - data.pose.pose.position.x), 2) + pow((self.goal_pose.y - data.pose.pose.position.y), 2))


    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        self.integralError += sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, kp=0.07, kd=0.005, ki=0.01):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return ((kp * self.euclidean_distance(goal_pose)) + (kd*self.error)) + (ki*self.integralError)

    def set_angle(self,angle):
        if math.degrees(abs(self.pose.theta-angle)) <= 180:
            return angle
        else:
            return math.radians(math.degrees(angle)-360)

    def steering_angle(self, goal_pose, aoa=0):
        """See video: https://www.youtube.com/watch?v=Qh1s5Nol5htM."""
        if aoa==0:
            return self.set_angle(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x))
        else:
            return self.set_angle(goal_pose.theta)

    def angular_vel(self, goal_pose, aoa =0, kp=0.5 ,kd=0.01):
        """See video: https://www.yyoutube.com/watch?v=Qh15Nol5htM."""
        if aoa==0:
            return kp * (self.steering_angle(goal_pose) - self.pose.theta) + kd*self.thetaerror
        else:
            return kp * (self.steering_angle(goal_pose,1) - self.pose.theta) + kd*self.thetaerror


    def move2goal(self,x,y,angleOfApproach,steerOnly=0):
        """Moves the turtle to the goal."""
        goal_pose = Pose()
        # Get the input from the user.
        goal_pose.x = x
        goal_pose.y = y
        goal_pose.theta = angleOfApproach
        goal_pose.theta = math.radians(goal_pose.theta)
        self.goal_pose = goal_pose
        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = 0.05 #input("Set your tolerance: ")
        angle_tolerance = math.radians(1)
        vel_msg = Twist()
        max_linear_velocity = 0.1
        max_angular_velocity = 5
        if steerOnly == 0:
            while abs(self.pose.theta - self.steering_angle(goal_pose))>=angle_tolerance:
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                # Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)
                if vel_msg.angular.z > max_angular_velocity:
                    vel_msg.angular.z = max_angular_velocity

                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                print math.degrees(self.steering_angle(goal_pose))

                # Publish at the desired rate.
                self.rate.sleep()

            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            rospy.sleep(3.)
            print "Initial steerign complete"


            while self.euclidean_distance(goal_pose) >= distance_tolerance:

                # Porportional controller.
                # https://en.wikipedia.org/wiki/Proportional_control

                # Linear velocity in the x-axis.
                vel_msg.linear.x = self.linear_vel(goal_pose)
                if vel_msg.linear.x > max_linear_velocity:
                    vel_msg.linear.x = max_linear_velocity
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                # Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)
                if vel_msg.angular.z > max_angular_velocity:
                    vel_msg.angular.z = max_angular_velocity

                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)

                # Publish at the desired rate.
                self.rate.sleep()

            # Stopping our robot after the movement is over.
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            print "translation complete"

        #steer to angleOfApproach

        while abs(self.steering_angle(goal_pose,1)-self.pose.theta) >= angle_tolerance:
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose,1)
            if vel_msg.angular.z > max_angular_velocity:
                vel_msg.angular.z = max_angular_velocity

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            print math.degrees(self.steering_angle(goal_pose))

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.sleep(3.)
        print "Reached angleOfApproach"
        msg=rospy.wait_for_message('/mybot/camera1/image_raw', Image)

        # xyz =rospy.wait_for_message('/odom', Odometry)
        # orlist = [xyz.pose.pose.orientation.x, xyz.pose.pose.orientation.y, xyz.pose.pose.orientation.z, xyz.pose.pose.orientation.w]
        # (r,p,y) = euler_from_quaternion(orlist)
        # print xyz
        # print 'OREINTATION'
        # print math.degrees(y)
        res = self.navigateImageCheck(msg)
        return res
        # If we press control + C, the node will stop.
        # rospy.spin()

def ORBdetectormatcher(self,imginput,imgtest,ptno):

   summy = 0
   # imginput = cv.blur(imginput,(5,5))
   # imgtest = cv.blur(imgtest,(5,5))
   img3 = []
   list_kp1 = []
   list_kp2 = []
   list_dec = []
   good = []
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
   row1 = len(list_kp1)
   col1 = len(list_kp1[0])
   row2 = len(list_kp2)
   col2 = len(list_kp2[0])

   summa = 0
   denom = 0
   denom1 = 0
   denom2 = 0
   for m in range(row1):
     deltx =  (list_kp1[m][0]-list_kp2[m][0])**2
     delty =  (list_kp1[m][1]-list_kp2[m][1])**2
     #cornerscore =
     summa+=math.sqrt((deltx + delty))
     denom1=findworstdist(self,list_kp1,m)
     denom2=findworstdist(self,list_kp2,m)
     denom+=(denom1 + denom2)/4

   position_unmatchscore = summa/denom
   position_matchscore = 1 - position_unmatchscore
   #positionmaxscore = row1 * posmaxrowsum

   lengy = len(list_dec)
   lenlist1 = len(kp1)
   lenlist2 = len(kp2)


   print("\nNO. OF FEATURES DETECTED IN IMAGE1 AND IMAGE2",lenlist1,lenlist2)
   #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 1 \n",list_kp1)
   #print("\nX,Y COORDINATES OF KEYPOINTS IN IMAGE 2 \n",list_kp2)


   for k in range(lengy):
       summy+=list_dec[k][0]

   # global summy_x = summy
   print("ORB DECISION SCORE",summy)
   if summy < 0:
       print("IMAGE DATA SHOWS LEFT SHIFT ERROR")
       print("MOVE RIGHT")
   elif summy > 0:
       print("IMAGE DATA SHOWS RIGHT SHIFT ERROR")
       print("MOVE LEFT")
   elif summy == 0:
       print("MATCH!")
   good = []

   #for m in matches:
       #if m.distance < 100:
        #   good.append([m])2
   for i,m in enumerate(matches):
     #if m.distance < 100:
      #  good.append(m)
    if i < len(matches) and m.distance < 100 * matches[i-1].distance: #and m.distance < 10000 * matches[i+1].distance:
      good.append([m])

   #print("match length",len(matches))
   msg2 = 'There are %d good matches HA' % (len(good))
   feature_matchscore = float(len(good)) / (min(lenlist1,lenlist2))

   #img3 = cv.drawMatches(imginput,kp1,imgtest,kp2,matches[:(len(good))],None,flags=2)

   #font = cv.FONT_HERSHEY_SIMPLEX
   #cv.putText(img3,msg2,(10, 270), font, 0.5,(255,255,255),1,cv.LINE_AA)
   #fname = 'output_%s_%.2f.png' % (method, lowe_ratio)
   #cv.imwrite(fname, img3)

   print('\nORB MATCHES', len(good))
   print('FEATURE MATCH SCORE',feature_matchscore)
   print('POSITION MATCH SCORE', position_matchscore)
   matchscore = 0.85 * feature_matchscore + 0.15 * position_matchscore
   print('FINAL MATCH SCORE', matchscore)
   global matchfound
   matchfound = matchscore

   if matchscore > 0.60:
      #print(imgtest)
      print('\nYOU are at node', ptno)




def ORBSINGLEMATCHER(self,navimage,mapptno):
   # no error case, aka using mappt to search database for image, searched map img matches nav image
   if mapptno < 10:
    fnam_map = r"/home/varsh/newmap/image000%d.jpg" % mapptno
   elif mapptno >= 10:
    fnam_map = r"/home/varsh/newmap/image00%d.jpg" % mapptno
   mapimage = cv.imread(fnam_map,1)
   # cv.imshow('map image corresponding to the navigation image',mapimage)
   #cv.waitKey(0)
   #finding orb match
   ORBdetectormatcher(self,navimage,mapimage,mapptno)

def findTranslation():
    return 0

def findworstdist(self,list_kp,m):

     #point 1 - 0,512 ; 2 - 512,512 ; 3 - 512,0 ; 4 - 0,0
     #image for first
     x_dim,y_dim = self.get_image_dimensions()
     worstdist1x = (list_kp[m][0])**2
     worstdist1y = (list_kp[m][1] - (y_dim))**2
     worstdist1 = math.sqrt(worstdist1x + worstdist1y)
     worstdist2x = (list_kp[m][0] - (x_dim))**2
     worstdist2y = (list_kp[m][1] - (y_dim))**2
     worstdist2 = math.sqrt(worstdist2x + worstdist2y)
     worstdist3x = (list_kp[m][0] - (x_dim))**2
     worstdist3y = (list_kp[m][1])**2
     worstdist3 = math.sqrt(worstdist3x + worstdist3y)
     worstdist4x = (list_kp[m][0])**2
     worstdist4y = (list_kp[m][1])**2
     worstdist4 = math.sqrt(worstdist4x + worstdist4y)
     worstdist = max(worstdist1,worstdist2,worstdist3,worstdist4)
     return worstdist
    # else:
    #    print('hm match not found')
    #    print('You may not be at node', mapptno)
    #    print('Checking with nearby nodes')
       # ORBGROUPMATCHER(navimage,mapptno)

class NavigateServer:

# create messages that are used to publish feedback/result
  _feedback = NavigateActionFeedback()
  _result = NavigateActionResult()

  def __init__(self):
    self.server = actionlib.SimpleActionServer('navigate', NavigateAction, self.execute, False)
    self.server.start()

  def set_result(self,status):
      global matchfound
      self._result.result.decision_score = matchfound
      self._result.result.status = status


  def execute(self, goal):
    # Do lots of awesome groundbreaking robot stuff here
    X = goal.goal_pose.position.x
    Y = goal.goal_pose.position.y
    Z = goal.goal_pose.position.z
    angleOfApproach = goal.goal_pose.angleOfApproach
    global mapPointID
    mapPointID = goal.goal_pose.mapPointID
    print "[----------Server Message ----------]"
    x = TurtleBot()
    res = x.move2goal(X,Y,angleOfApproach,Z)
    self.set_result(res)
    self.server.set_succeeded(self._result.result)
    # else:


if __name__ == '__main__':
  rospy.init_node('navigate_server')
  rospy.wait_for_message('/mybot/camera1/image_raw', Image)
  server = NavigateServer()
  rospy.spin()
