#!/usr/bin/env python

import sys
from swarm.msg import Detection
import rospy
import receiver
import Json


#while(True):

class Listener_det(object):
    def init_det(self):
        topic_detection             = "/swarm/data/det"
        self._detectionPublisher     = rospy.Publisher(topic_detection, Detection,  queue_size = 50)
        
    def _publishDetection(self, json_msg):
        detectionMsg = Json.detInput2Detection(json_msg)
        self._detectionPublisher.publish(detectionMsg)

    def run_det(self):
        receiver.background_controller(detection_data)
        self._publishDetection(detection_data)