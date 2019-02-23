import serial
import time
import json

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
key = 'test'
value = 77

#Function to read serial message from arduino
def updateState():
  msgArduino = arduino.readline()
  print(msgArduino)
  #TODO: ADD code to detect json key and value

#Function to send serial message 
def sendMsg():
  data = {'key' :value}
  arduino.write(str(data).encode())


while True :
  currentTime = time.time()
  updateState()
  sendMsg()   
  
  time.sleep(0.15)
