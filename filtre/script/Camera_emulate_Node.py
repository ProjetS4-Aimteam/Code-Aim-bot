#!/usr/bin/env python
# NODE ROS, Kinect emulation
# Project S4 GRO
# Author: CP& Simon Therrien
# Date: February 2019
""" Node that emulate a kinect camera x position and angle output from laserscan"""

# Every part regarding the RosNode is commented and shall be tested later

import rospy
import numpy as np
from filtre.msg import cup_pos
# Constant
Cup_pos = cup_pos()
# Parameter

def send_msg(xpos,angle):
    pub = rospy.Publisher("cup_pos", cup_pos, queue_size=0)
    Cup_pos.cup_distance = xpos
    Cup_pos.cup_angle = angle
    pub.publish(Cup_pos)
   # rospy.loginfo(' xpos =')
    #rospy.loginfo(xpos)

def talker():
    xpos = 0.1
    angle = -10
    rospy.init_node('Camera_emulate', anonymous=True)
  #  rospy.loginfo('Camera_emulate started')
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        if xpos >3:
            xpos = 0.1
        else:
            xpos += 0.1
        if angle > 10:
            angle = -10
        else:
            angle += 0.5
        send_msg(xpos,angle)
        rate.sleep()

        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
