#!/usr/bin/env python
# NODE ROS, Dynamic controller Ball Launcher
# Project S4 GRO
# Author: Simon Therrien
# Date: February 2019
""" Node that get the X position of the target and define the Initial speed of the launcher"""

# Every part regarding the RosNode is commented and shall be tested later

import rospy
import math
from std_msgs.msg import Float32
import numpy as np
#from sensor_msgs.msg import LaserScan

# Constant
MAX_ITERATION = 100
Cd = 0.47       # Ball's coefficient of drag
Rho = 1.1123    # kg/m^3, Air density in Sherbrooke, 25C
G = 9.806       # m/s^2, Gravitational acceleration
Rb = 0.02       # m, Ball's radius
Mb = 0.0027     # Kg, Ball's weight
R = 0.054
# Parameter
Yi = 0.3        # m, Distance between Launcher and top of the glass
Theta = 1.0472  # rad, Angle of launch

def Fy(Vi,t,K):
    """1st Equation for Newton-Raphson"""
    return ((-Vi * math.sin(Theta) - G / K) * math.exp(-K * t)) / K - (G * t) / K + Yi + (Vi * math.sin(Theta)) / K + G / (math.pow(K ,2))

def Dfy(Vi,t,K):
    """ Derivative of the 1st Equation for Newton-Raphson"""
    return (Vi*math.sin(Theta)+G/K)*math.exp(-K*t)-G/K

def Drag_Coeff():
    """ Calculation of the coefficient of drag"""
    a = math.pi * math.pow(Rb, 2)
    k = (Cd*Rho*a)/(2*Mb)
    return k


def NR_Dyn(x):
    """ Newton-Raphson resolution for non-linear Dynamic system
    will return the initial speed required or false if it did not converge
    x needs to be between 0 and 3.5 m.
    """
    assert x > 0.0, " X distance error; too small"
    assert x < 3.50, " X distance unreachable "

    K = Drag_Coeff()
    tf = 2
    for ii in range(MAX_ITERATION):
        ini_speed = (x * K) / (math.cos(Theta) * (1 - math.exp(-K * tf)))
        tf = tf - (Fy(ini_speed, tf, K) / Dfy(ini_speed, tf,K))
        if math.fabs(Fy(ini_speed,tf,K)) < 0.00005:
            return ini_speed
    return False

def Test_Dynamic():
    test1 = NR_Dyn(2.4)
    assert math.fabs(test1 - 5.243) < 0.01, " Dynamic test 1 Failed"
    print("Dynamic Test 1 Succeeded, Inital speed = ", test1)
    test2 = NR_Dyn(1.3)
    assert math.fabs(test2 - 3.72) < 0.01, " Dynamic test 2 Failed"
    print("Dynamic Test 2 Succeeded, Inital speed = ", test2)
    #test3 = NR_Dyn(-0.1)   # Test for Value too small
    #test4 = NR_Dyn(3.6)    # Test for Value too large
    return

def send_msg(ini_speed):
    pub = rospy.Publisher("launch_parameter", Float32, queue_size=0)
    pub.publish(ini_speed)


def callback(msg):
    pos = msg.data
    ini_spd = NR_Dyn(pos)
    send_msg(ini_spd/R)
    #rospy.loginfo(ini_spd)

def main():
    #Test_Dynamic()
    rospy.init_node('Dynamic_controller', anonymous=True)
    rospy.Subscriber("cup_pos",Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    #try:
        main()
    #except rospy.ROSInterruptException:
     #   pass
