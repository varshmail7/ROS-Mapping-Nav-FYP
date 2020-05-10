#!/usr/bin/env python
import rospy
from message_filters import ApproximateTimeSynchronizer, Subscriber
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from mybot_description.msg import Record
import std_msgs
import math

def merge(inputt, outputt):
    #assert image.header.stamp == odometry.header.stamp
    record = Record()
    record.time = rospy.get_time()
    record.input = inputt.linear.x
    record.output = outputt[1].linear.x
    print record
    pub = rospy.Publisher("mybot/record", Record, queue_size=10)
    r = rospy.Rate(10)
    pub.publish(record)
    r.sleep()

rospy.init_node("recorder",anonymous=True)
input_sub = Subscriber("/mybot/mobile_base_controller/cmd_vel", Twist)
output_sub = Subscriber("/gazebo/model_states/twist", Twist)

ats = ApproximateTimeSynchronizer([input_sub, output_sub], queue_size=5, slop=0.1)
ats.registerCallback(merge)
rospy.spin()
