#!/usr/bin/env python
import numpy as np
import xml.etree.ElementTree as ET

import rospy
from dvrk2robosuite.msg import measured_js, measured_cv, measured_cp

def MTMLcallback(data):
    global MTMLaction
    MTMLaction[0] = data.transform.rotation.x
    MTMLaction[1] = data.transform.rotation.y
    MTMLaction[2] = data.transform.rotation.z
    MTMLaction[3] = data.transform.rotation.w

def MTMLlistener():
    rospy.Subscriber("/MTML/measured_cp", measured_cp, MTMLcallback)

if __name__ == "__main__":
    MTMLaction = np.zeros(7)
    MTMLlistener()
    rospy.spin()