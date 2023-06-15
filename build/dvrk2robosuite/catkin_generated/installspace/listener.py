#!/usr/bin/env python3
import rospy
# from std_msgs.msg import String
from dvrk2robosuite.msg import measured_js

def MTMLcallback(data):
    rospy.loginfo(rospy.get_caller_id() + data.velocity)

def MTMLGrippercallback(data):
    rospy.loginfo(rospy.get_caller_id() + data.velocity)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("MTML/measured_js", measured_js, MTMLcallback)
    rospy.Subscriber("MTML/gripper/measured_js", measured_js, MTMLGrippercallback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()