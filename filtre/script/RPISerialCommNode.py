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
from filtre.msg import toOpenCR
from filtre.msg import fromOpenCR
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
#Variable a envoyer vers OpenCR


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
  #Get les valeurs du msg recu
   kp = msg.kp
   ki = msg.ki
   kd = msg.kd
   ini_spd = msg.ini_spd

   #Construction de la liste a envoyer
   msgOpenCR = {'kp' :kp, 'ki' :ki, 'kd' :kd, 'ini_spd' :ini_spd}

   #Envoie du message vers OpenCR
   arduino.write(str(msgOpenCR).encode())
   rospy.loginfo(msgOpenCR)
      
def send_msg_topic(msg_ardu):
    pub1 = rospy.Publisher("Ardu", String, queue_size=0)
    pub1.publish(msg_ardu)

def send_msg_pi(msg_pi):
    pub2 = rospy.Publisher("pi_msg", Float32, queue_size=0)
    pub2.publish(msg_pi)
    


#Main
def main():
   rospy.init_node('Serial_comm')
   rate = rospy.Rate(10)
   
 
   while not rospy.is_shutdown():
     rospy.Subscriber("msgToOpenCR",toOpenCR,callback)
     rate.sleep()
  
   rospy.spin()

if __name__ == '__main__':
   main()
