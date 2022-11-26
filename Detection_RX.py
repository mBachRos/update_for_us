#!/usr/bin/env python

import sys
import os

import rospy

from Classes.Detection_input import Listener_det



def main():
    #initialize ROS node
    rospy.init_node('detection_node', anonymous=True)
    rospy.logdebug("Started detection node")

    #initiate listener socket
    pub = Listener_det()

    #Start listening and handling data from multicast
    rospy.loginfo("Starting run")
    pub.run_det()
    rospy.loginfo("Shutting down")

if __name__ == '__main__':
    main()
