#!/usr/bin/env python
# NODE ROS, Kinect emulation
# Project S4 GRO
# Author: Carl-Philippe Cyr & Simon Therrien & Olivier Julien
# Date: February 2019
""" Node that do the communication between the arduino and the RPI"""

# Every part regarding the RosNode is commented and shall be tested later

import serial
import time
import json
import rospy
from std_msgs.msg import Float32
import numpy as np

#Defining the serial port and speed
port = '/dev/ttyACM0'
speed = 9600

#If serial connection failed generate an error
try:
  arduino = serial.Serial(port, speed)
  time.sleep(2)
  print("connection to" + port + "Reussi\n")
  
except Exception as e:
  print(e)

#TODO: Get the key and the value from a ROS Node
#key = 'test'
#value = 77

#Function to read serial message from arduino
def updateState():
  msgArduino = arduino.readline()
  print(msgArduino)
  #TODO: ADD code to detect json key and value

#Function to send serial message 
def send_msg(key,value):
  data = {key :value}
  arduino.write(str(data).encode())
  rospy.loginfo(data)

def callback(msg):
   ini_spd = msg.data
   send_msg('ini_spd',ini_spd)


#Main
def main():
   rospy.init_node('Serial_comm')
   rospy.Subscriber("launch_parameter",Float32,callback)
   #rate = rospy.Rate(1)
   rospy.spin()
   #while not rospy.is_shutdown():
      #updateState()
    #rate.sleep()
   

if __name__ == '__main__':
   main()


