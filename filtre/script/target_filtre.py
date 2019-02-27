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
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

cup_radius = 0.045		#radius of a cup in m
front_offset = 0.15	#distace betwen the zero of the kinect and the launcher
cheat_offset = 0.00	#a positive or negative offset to tune the launcher

def callback(data):
	
	pos_raw = data.ranges[320] 
	pos = pos_raw + front_offset + cup_radius + cheat_offset
	send_msg(pos,pos_raw)
	#rospy.loginfo(pos)

def send_msg(center_distance, raw_distance):
    pub1 = rospy.Publisher("raw_pos", Float32, queue_size=10)
    pub = rospy.Publisher("cup_pos", Float32, queue_size=0)
    pub1.publish(raw_distance)
    pub.publish(center_distance)
		
def main():

	rospy.init_node('target_filtre', anonymous=True)
	rospy.Subscriber('depth_scan', LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
    #try:
        main()
    #except rospy.ROSInterruptException:
     #   pass

