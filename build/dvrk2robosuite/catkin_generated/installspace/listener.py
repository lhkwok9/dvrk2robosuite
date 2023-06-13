#!/usr/bin/env python3
import rospy
# from std_msgs.msg import String
from dvrk2robosuite.msg import measured_cp

def MTMLcallback(data):
    global MTMLaction
    rospy.loginfo(rospy.get_caller_id() + " L arm: %lf, %lf, %lf, %lf, %lf, %lf, %lf", data.a, data.b, data.c, data.d, data.e, data.f, data.g)
    MTMLaction = [data.a, data.b, data.c, data.d, data.e, data.f, data.g]
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("MTML/measured_cp", measured_cp, MTMLcallback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()