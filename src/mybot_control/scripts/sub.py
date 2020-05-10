#!/usr/bin/env python
import rospy
from message_filters import ApproximateTimeSynchronizer, Subscriber
from sensor_msgs.msg import Image, CameraInfo
from nav_msgs.msg import Odometry
import std_msgs
from mybot_description.msg import Map
from tf.transformations import euler_from_quaternion
import math

def merge(image, camera, odometry):
    #assert image.header.stamp == odometry.header.stamp
    map = Map()
    map.header = odometry.header
    map.image = image
    map.cameraInfo = camera
    map.position = odometry.pose.pose.position
    orlist = [odometry.pose.pose.orientation.x, odometry.pose.pose.orientation.y, odometry.pose.pose.orientation.z, odometry.pose.pose.orientation.w]
    (r,p,y) = euler_from_quaternion(orlist)
    map.angleOfApproach = math.degrees(y)
    pub = rospy.Publisher('mybot/mapstream', Map, queue_size=10)
    r = rospy.Rate(10)
    pub.publish(map)
    r.sleep()# QUESTION:

rospy.init_node("sub",anonymous=True)
image_sub = Subscriber("/mybot/camera1/image_raw", Image)
camera_sub = Subscriber("mybot/camera1/camera_info", CameraInfo )
odom_sub = Subscriber("/odom", Odometry)

ats = ApproximateTimeSynchronizer([image_sub,camera_sub,odom_sub], queue_size=5, slop=0.1)
ats.registerCallback(merge)
rospy.spin()
