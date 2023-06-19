#!/usr/bin/env python
import rospy
# from std_msgs.msg import String
# from dvrk2robosuite.msg import measured_js, measured_cp, measured_cv
import tf2_ros
from geometry_msgs.msg import TransformStamped as t

def MTMLcallback(data):
    rospy.loginfo(rospy.get_caller_id() + " L arm: %lf, %lf, %lf, %lf, %lf, %lf, %lf", 
        data.transform.translation.x, data.transform.translation.y, data.transform.translation.z, 
        data.transform.rotation.x, data.transform.rotation.y, data.transform.rotation.z, data.transform.rotation.w)
    # rospy.loginfo(rospy.get_caller_id() + " L arm: %lf, %lf, %lf, %lf, %lf, %lf", 
    #     data.twist.linear.x, data.twist.linear.y, data.twist.linear.z, 
    #     data.twist.angular.x, data.twist.angular.y, data.twist.angular.z)

def MTMLGrippercallback(data):
    rospy.loginfo(rospy.get_caller_id() + " L gripper: %lf", data.position[0])
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber("MTML/measured_cp", measured_cp, MTMLcallback)
    rospy.Subscriber("/MTML/measured_cp", t, MTMLcallback)
    # rospy.Subscriber("MTML/gripper/measured_js", measured_js, MTMLGrippercallback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()