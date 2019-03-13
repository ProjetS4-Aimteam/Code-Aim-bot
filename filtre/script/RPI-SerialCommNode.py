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
from std_msgs.msg import String
import numpy as np

#Defining the serial port and speed
port = '/dev/ttyACM0'
speed = 115200

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
  send_msg_topic(msgArduino)
 # rospy.loginfo(msgArduino)
  #TODO: ADD code to detect json key and value

#Function to send serial message 
def send_msg(key,value):
  data = {key :value}
  arduino.write(str(data).encode())
  rospy.loginfo(data)

def callback(msg):
   ini_spd = msg.data
   send_msg('ini_spd',ini_spd)
   send_msg_pi(ini_spd)
   updateState()

def send_msg_topic(msg_ardu):
    pub1 = rospy.Publisher("Ardu", String, queue_size=0)
    pub1.publish(msg_ardu)

def send_msg_pi(msg_pi):
    pub2 = rospy.Publisher("pi_msg", Float32, queue_size=0)
    pub2.publish(msg_pi)


#Main
def main():
   rospy.init_node('Serial_comm')
   rospy.Subscriber("launch_parameter",Float32,callback)
  # rate = rospy.Rate(2)
  # rate.sleep()
   rospy.spin()
   #while not rospy.is_shutdown():
      #updateState()
    #rate.sleep()
   

if __name__ == '__main__':
   main()