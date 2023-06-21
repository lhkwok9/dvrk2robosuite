#!/usr/bin/env python
import numpy as np
import xml.etree.ElementTree as ET

import rospy
from geometry_msgs.msg import TransformStamped as t

def MTMLcallback(data):
    global MTMLTranslation
    MTMLTranslation[0] = data.transform.translation.x
    MTMLTranslation[1] = data.transform.translation.y
    MTMLTranslation[2] = data.transform.translation.z

def MTMLlistener():
    rospy.Subscriber("/MTML/measured_cp", t, MTMLcallback)

def MTMLDifferencecallback(data):
    global MTMLCurrentTranslation
    global MTMLPreviousTranslation
    global MTMLDeltaTranslation
    MTMLDeltaTranslation = MTMLCurrentTranslation - MTMLPreviousTranslation
    MTMLPreviousTranslation = MTMLCurrentTranslation
    
def MTMLDifferencelistener():
    rospy.Subscriber("/MTML/measured_cp", t, MTMLcallback)
    

def simulatorLcallback(data):
    global simulatorLTranslation
    simulatorLTranslation[0] = data.transform.translation.x
    simulatorLTranslation[1] = data.transform.translation.y
    simulatorLTranslation[2] = data.transform.translation.z

def simulatorLlistener():
    rospy.Subscriber("/simulator/Left/measured_cp", t, simulatorLcallback)

def MTML2simulatorLTranslationTalker():
    global MTMLTranslation
    global simulatorLTranslation

    pub = rospy.Publisher('/simulator/Left/relativeTranslation', t, queue_size=10)

    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        diff = MTMLTranslation - simulatorLTranslation
        rospy.loginfo(diff)
        tDiff = t()
        tDiff.transform.translation.x = 3*diff[0] if abs(diff[0]) > 0.0001 else 0
        tDiff.transform.translation.y = 3*diff[1] if abs(diff[1]) > 0.0001 else 0
        tDiff.transform.translation.z = 3*diff[2] if abs(diff[2]) > 0.0001 else 0
        pub.publish(tDiff) 
        rate.sleep()


if __name__ == "__main__":
    rospy.init_node('translationDifference', anonymous=False)

    MTMLTranslation = np.zeros(3)
    simulatorLTranslation = np.zeros(3)

    MTMLlistener()
    simulatorLlistener()
    MTML2simulatorLTranslationTalker()
    rospy.spin()