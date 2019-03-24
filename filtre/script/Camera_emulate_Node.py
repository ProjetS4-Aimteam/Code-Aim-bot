#!/usr/bin/env python
# NODE ROS, Kinect emulation
# Project S4 GRO
# Author: CP& Simon Therrien
# Date: February 2019
""" Node that emulate a kinect camera x position output from laserscan"""

# Every part regarding the RosNode is commented and shall be tested later

import rospy
from std_msgs.msg import Float32
import numpy as np

# Constant

# Parameter

def send_msg(xpos):
    pub = rospy.Publisher("cup_pos", Float32, queue_size=0)
    pub.publish(xpos)
   # rospy.loginfo(' xpos =')
    #rospy.loginfo(xpos)

def talker():
    xpos = 0.1
    rospy.init_node('Camera_emulate', anonymous=True)
  #  rospy.loginfo('Camera_emulate started')
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        if xpos >3.4:
            xpos = 0.1
        else:
            xpos += 0.1
        send_msg(xpos)
        rate.sleep()

        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
