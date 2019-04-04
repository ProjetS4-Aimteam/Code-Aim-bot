#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from sensor_msgs.msg import LaserScan
from filtre.msg import cup_pos
import numpy
from collections import deque
#import cv2
#from disutils.version import LooseVersion


Cup_pos = cup_pos()

def callback(data):
        assert min_index > 0, "Minimum wasnt found"
        
        cup_angle = angle_avg(cup_angle)
        cup_distance = dist_avg(cup_distance)
        
        Cup_pos.cup_angle = cup_angle*(180/3.141592)
        Cup_pos.cup_distance = cup_distance
        #Cup_pos.cup_distance = left_boundary    #to see the length of data.ranges   
        send_msg(Cup_pos)
        rospy.loginfo(Cup_pos)

def send_msg(Cup_pos):

    pub = rospy.Publisher("cup_pos", cup_pos, queue_size=10)
    pub.publish(Cup_pos)
		
def main():
	rospy.init_node('shot_target', anonymous=True)
	rospy.Subscriber('cup_pos', cup_pos, callback)
	rospy.spin()

if __name__ == '__main__':
    #try:
        main()
    #except rospy.ROSInterruptException:
     #   pass

