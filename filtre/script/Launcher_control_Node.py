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
from filtre.msg import cup_pos
from filtre.msg import UIParameter
import numpy as np
#from sensor_msgs.msg import LaserScan

# Constant
R = 0.054
MAX_SPEED = 100*R # Maximum motor speed, rad/s equivalent of 960 rpm motor
MAX_ITERATION = 100
THETA_MIN = 0.5236 # Minimum launch angle, equivalent of 30 deg
THETA_45 = 0.785398163 # Angle rad equivalent of 45 deg (max shooting range)
THETA_INI = 1.0472  # Initial launch angle, equivalent of 60 deg
THETA_MAX = 1.396 # Maximum launch angle, equivalent of 80 deg
Cd = 0.47       # Ball's coefficient of drag
Rho = 1.1123    # kg/m^3, Air density in Sherbrooke, 25C
G = 9.806       # m/s^2, Gravitational acceleration
Rb = 0.02       # m, Ball's radius
Mb = 0.0027     # Kg, Ball's weight
# Parameter
Yi = 0.3        # m, Distance between Launcher and top of the glass

Mode = 0

def Fy(Vi,theta,t,K):
    """1st Equation for Newton-Raphson"""
    return ((-Vi * math.sin(theta) - G / K) * math.exp(-K * t)) / K - (G * t) / K + Yi + (Vi * math.sin(theta)) / K + G / (math.pow(K ,2))

def Dfy(Vi,theta,t,K):
    """ Derivative of the 1st Equation for Newton-Raphson"""
    return (Vi*math.sin(theta)+G/K)*math.exp(-K*t)-G/K



def Drag_Coeff():
    """ Calculation of the coefficient of drag"""
    a = math.pi * math.pow(Rb, 2)
    k = (Cd*Rho*a)/(2*Mb)
    return k

def NR_Dyn_theta(x,ini_speed):
    """ Newton-Raphson resolution for non-linear Dynamic system
    will return the initial speed required or false if it did not converge
    x needs to be between 0 and 3.5 m.
    """
    assert x > 0.0, " X distance error; too small"
    assert x < 3.0, " X distance unreachable "

    K = Drag_Coeff()
    tf = 2
    for ii in range(MAX_ITERATION):
        theta = math.acos((x * K/ini_speed)/(1 - math.exp(-K * tf)))
        tf = tf - (Fy(ini_speed, theta, tf, K) / Dfy(ini_speed, theta, tf,K))
        if math.fabs(Fy(ini_speed,theta,tf,K)) < 0.00005:
            return theta
    return False

def NR_Dyn_vi(x,theta):
    """ Newton-Raphson resolution for non-linear Dynamic system
    will return the initial speed required or false if it did not converge
    x needs to be between 0 and 3.5 m.
    """
    assert x > 0.0, " X distance error; too small"
    assert x < 3.0, " X distance unreachable "

    K = Drag_Coeff()
    tf = 2
    for ii in range(MAX_ITERATION):
        ini_speed = (x * K) / (math.cos(theta) * (1 - math.exp(-K * tf)))
        tf = tf - (Fy(ini_speed, theta, tf, K) / Dfy(ini_speed, theta, tf,K))
        if math.fabs(Fy(ini_speed,theta,tf,K)) < 0.00005:
            return ini_speed
    return False

def limited_Dynamic(x):
    
    theta = THETA_45
    
    speed_max = NR_Dyn_vi(x,theta)
    if(speed_max > 0.85 * MAX_SPEED):
        return speed_max, theta
    else:
        adjusted_speed = speed_max + (MAX_SPEED - speed_max)/2
        theta = NR_Dyn_theta(x,adjusted_speed)
        if(theta > THETA_MAX):
            theta = THETA_MAX
            adjusted_speed = NR_Dyn_vi(x,theta)
    return adjusted_speed, theta

def Test_Dynamic():
    Theta = 1.0472  # rad, Angle of launch
    test1 = NR_Dyn_vi(2.4)
    assert math.fabs(test1 - 5.243) < 0.01, " Dynamic test 1 Failed"
    print("Dynamic Test 1 Succeeded, Inital speed = ", test1)
    test2 = NR_Dyn_vi(1.3)
    assert math.fabs(test2 - 3.72) < 0.01, " Dynamic test 2 Failed"
    print("Dynamic Test 2 Succeeded, Inital speed = ", test2)
    #test3 = NR_Dyn(-0.1)   # Test for Value too small
    #test4 = NR_Dyn(3.6)    # Test for Value too large
    return

def send_msg(ini_speed,theta):
    pub = rospy.Publisher("launch_parameter", Float32, queue_size=0)
    pub2 = rospy.Publisher("launch_angle", Float32, queue_size=0)
    pub.publish(ini_speed)
    launch_angle = theta*180/np.pi
    pub2.publish(launch_angle)
    
def callback(msg):
    if(Mode == 0):
        pos = msg.cup_distance
        ini_spd, theta = limited_Dynamic(pos)
        rospy.loginfo(theta)
        rospy.loginfo(ini_spd/R)
        send_msg(ini_spd/R,theta)
    else:
        pos = msg.cup_distance
        ini_spd, theta = limited_Dynamic(pos)
        rospy.loginfo(theta)
        rospy.loginfo(ini_spd/R)
        
def callback_height(msg):
    Yi = msg.data

def callback_UIParameter(msg):
    Mode = msg.mode

def main():
    #Test_Dynamic()
    rospy.init_node('Dynamic_controller', anonymous=True)
    rospy.Subscriber("cup_pos",cup_pos, callback)
    rospy.Subscriber("cup_height", Float32, callback_height)
    rospy.Subscriber("msgUIParameter", UIParameter, callback_UIParameter)
    rospy.spin()


if __name__ == '__main__':
    #try:
        main()
    #except rospy.ROSInterruptException:
     #   pass
