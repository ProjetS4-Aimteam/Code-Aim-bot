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

class Simplemovingaverage():
    def __init__(self, period):
        assert period == int(period) and period > 0, "Period must be an integer >0"
        self.period = period
        self.stream = deque()
 
    def __call__(self, n):
        stream = self.stream
        stream.append(n)    # appends on the right
        streamlength = len(stream)
        if streamlength > self.period:
            stream.popleft()
            streamlength -= 1
        if streamlength == 0:
            average = 0
        else:
            average = sum( stream ) / streamlength
 
        return average

read_angle = 20 * 3.141592 / 180 # read angle in radians

cup_radius = 0.045		#radius of a cup in m
front_offset = 0.00	#distance between the zero of the kinect and the launcher
cheat_offset = 0.00	#a positive or negative offset to tune the launcher
Cup_pos = cup_pos()
dist_avg = Simplemovingaverage(75) #moving average of 10 data
angle_avg = Simplemovingaverage(75) #moving average of 10 data

def callback(data):

        mid_index = len(data.ranges)/2-1 #center of the data array (640/2 by default)
        left_boundary = int(mid_index -  (read_angle/2)/data.angle_increment) # data index to analyse from
        right_boundary = int(mid_index + (read_angle/2)/data.angle_increment) # data index to analyse to
        min_index = 0
        #data_avg(data.ranges)
        min_ = data.range_max
        for x in range(left_boundary, right_boundary):
                if min_ > data.ranges[x]:
                        min_ = data.ranges[x]
                        min_index = x
        assert min_index > 0, "Minimum wasnt found"
        
        cup_angle = data.angle_min + data.angle_increment*min_index
        cup_angle = angle_avg(cup_angle)
        cup_distance = min_ + front_offset + cup_radius + cheat_offset
        cup_distance = dist_avg(cup_distance)
        
        Cup_pos.cup_angle = cup_angle*(180/3.141592)
        Cup_pos.cup_distance = cup_distance
        #Cup_pos.cup_distance = left_boundary    #to see the length of data.ranges   
        send_msg(Cup_pos)
        rospy.loginfo(Cup_pos)

def send_msg(Cup_pos):

    pub = rospy.Publisher("cup_pos", cup_pos, queue_size=0)
    pub.publish(Cup_pos)

		
def main():

	rospy.init_node('target_filtre', anonymous=True)
	rospy.Subscriber('depth_scan', LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
    #try:
        main()
    #except rospy.ROSInterruptException:
     #   pass

