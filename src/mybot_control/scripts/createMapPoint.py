#!/usr/bin/env python
import rospy
import numpy as np
from message_filters import Subscriber
from mybot_description.msg import Map
from mybot_description.msg import MapPoint
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist



def insertMapPoint(map):
    global mapPointID
    output = []
    bridge = CvBridge()
    # cv_image = bridge.imgmsg_to_cv2(map.image,"bgr8")
    # for i in cv_image:
    #     for j in i:
    #         output.append(j)
    mapPoint = MapPoint()
    mapPointImg = Image()
    mapPoint.mapPointID = mapPointID
    mapPointID = mapPointID + 1
    mapPoint.position = map.position
    mapPoint.angleOfApproach = map.angleOfApproach
    mapPointImg = map.image

    pub = rospy.Publisher('mybot/map_points', MapPoint, queue_size=5)
    pub1 = rospy.Publisher('mybot/map_point_images', Image, queue_size=5)
    pub2 = rospy.Publisher('mybot/camera_info', CameraInfo, queue_size=5 )
    pub.publish(mapPoint)
    pub1.publish(mapPointImg)

def callback(map_sub):
    global timeRef
    if map_sub.header.stamp.secs-timeRef>2.5:
        timeRef = map_sub.header.stamp.secs
        insertMapPoint(map_sub)

def startmap(vel_sub):
    if vel_sub.linear.x!=0 or vel_sub.angular.z!=0:
        rospy.Subscriber("/mybot/mapstream", Map, callback)


timeRef =0;
mapPointID =0;
rospy.init_node("createMapNode",anonymous=True)
rospy.Subscriber("/cmd_vel", Twist, startmap)
rospy.spin()
