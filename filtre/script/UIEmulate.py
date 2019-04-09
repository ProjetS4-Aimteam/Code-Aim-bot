#!/usr/bin/env python
# NODE ROS, UI emulation
# Project S4 GRO
# Author: Olivier Julien
# Date: March 2019
""" Node that emulate data output form UI"""

# Every part regarding the RosNode is commented and shall be tested later

import rospy
from std_msgs.msg import Float32
import numpy as np
from filtre.msg import UIParameter

sendToDataManager = UIParameter()


# Constant

# Parameter

def send_msg(msg):
    pub = rospy.Publisher("msgUIParameter", UIParameter, queue_size=0)
    pub.publish(msg)
    #rospy.loginfo(msg)

def talker():
    kp = 0.5
    ki = 0.5
    kd = 0.5
    rospy.init_node('UIEmulate', anonymous=True)
  
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        if kp >2:
            kp= 0.5
            ki = 0.5
            kd = 0.5
        else:
            kp += 0.1
            ki += 0.1
            kd += 0.1

        sendToDataManager.kp = kp
        sendToDataManager.ki = ki
        sendToDataManager.kd = kd
        send_msg(sendToDataManager)
        rate.sleep()

    rospy.spin()

        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
