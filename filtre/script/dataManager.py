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
from filtre.msg import cup_pos
from std_msgs.msg import Float32
from std_msgs.msg import String
import numpy as np

sendToOpenCR = toOpenCR()



def callbackSpd(msg):
   if(sendToOpenCR.mode== 2):
      sendToOpenCR.ini_spd = msg.data
      publishToOpenCR()
      
def callbackAngle(msg):
   if(sendToOpenCR.mode== 2):
      sendToOpenCR.tilt_angle = msg.data
      publishToOpenCR()
      
#def callbackCam(msg):
  # rospy.loginfo('bit')
   #if(sendToOpenCR.mode == 2):
    #  sendToOpenCR.pan_angle = msg.cup_angle
      #rospy.loginfo('hey')
      #rospy.loginfo(msg)
   
def callbackUI(msg):
    sendToOpenCR.kpSpeed = msg.kpSpeed
    sendToOpenCR.kiSpeed = msg.kiSpeed
    sendToOpenCR.kdSpeed = msg.kdSpeed

    sendToOpenCR.kpTilt = msg.kpTilt
    sendToOpenCR.kiTilt = msg.kiTilt
    sendToOpenCR.kdTilt = msg.kdTilt

    sendToOpenCR.kpPan = msg.kpPan
    sendToOpenCR.kiPan = msg.kiPan
    sendToOpenCR.kdPan = msg.kdPan

    sendToOpenCR.mode = msg.mode
    sendToOpenCR.launch = msg.launch

    sendToOpenCR.pan_angle = msg.pan_angle

    if(sendToOpenCR.mode == 1):
       sendToOpenCR.ini_spd = msg.motor_speed
       sendToOpenCR.tilt_angle = msg.tilt_angle
       
    if(sendToOpenCR.mode == 0):
       sendToOpenCR.ini_spd = 0
       sendToOpenCR.tilt_angle = msg.tilt_angle
    publishToOpenCR()
           
    
   
def publishToOpenCR():
    pub = rospy.Publisher("msgToOpenCR", toOpenCR, queue_size=0)
    pub.publish(sendToOpenCR)
    #rospy.loginfo(sendToOpenCR)


#Main
def main():
   rospy.init_node('dataManager')
   #rate = rospy.Rate(20)
    
   #while not rospy.is_shutdown():
     #rospy.loginfo(mode)
   rospy.Subscriber("launch_parameter",Float32,callbackSpd)
   rospy.Subscriber("launch_angle", Float32, callbackAngle)
     #rospy.Subscriber("cup_pos", cup_pos, callbackCam)
        
   rospy.Subscriber("msgUIParameter", UIParameter, callbackUI)
   #publishToOpenCR()
     #rate.sleep()
  
   rospy.spin()

if __name__ == '__main__':
   main()
