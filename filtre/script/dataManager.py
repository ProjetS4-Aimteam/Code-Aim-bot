#!/usr/bin/env python
# NODE ROS, data manager
# Project S4 GRO
# Author: Olivier Julien
# Date: March 2019
""" Node that manage all data to send on the OpenCR board"""

import time
import json
import rospy
from filtre.msg import toOpenCR
from filtre.msg import UIParameter
from std_msgs.msg import Float32
from std_msgs.msg import String
import numpy as np

sendToOpenCR = toOpenCR()



def callbackSpd(msg):
   sendToOpenCR.ini_spd = msg.data
   
def callbackUI(msg):
    sendToOpenCR.kp = msg.kp
    sendToOpenCR.ki = msg.ki
    sendToOpenCR.kd = msg.kd

def publishToOpenCR():
    pub = rospy.Publisher("msgToOpenCR", toOpenCR, queue_size=0)
    pub.publish(sendToOpenCR)
    #rospy.loginfo(sendToOpenCR)


#Main
def main():
   rospy.init_node('dataManager')
   rate = rospy.Rate(10)
    
   while not rospy.is_shutdown():
     rospy.Subscriber("launch_parameter",Float32,callbackSpd)
     rospy.Subscriber("msgUIParameter", UIParameter, callbackUI)
     publishToOpenCR()
     rate.sleep()
  
   rospy.spin()

if __name__ == '__main__':
   main()
