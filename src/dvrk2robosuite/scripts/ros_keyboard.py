#!/usr/bin/env python
import numpy as np
import rospy
from dvrk2robosuite.msg import measured_cp
import robosuite as suite
from robosuite import load_controller_config

def MTMLcallback(data):
    global MTMLaction
    # rospy.loginfo(rospy.get_caller_id() + " L arm: %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf", data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.gripper)
    MTMLaction = [data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.gripper]

def MTMLlistener():
    rospy.init_node('MTMLlistener', anonymous=False)

    rospy.Subscriber("MTML/measured_cp", measured_cp, MTMLcallback)
    # rospy.Subscriber("MTMR/measured_cp", measured_cp, callback)

    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

def MTMRcallback(data):
    global MTMRaction
    # rospy.loginfo(rospy.get_caller_id() + " R arm: %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf", data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.gripper)
    MTMRaction = [data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.gripper]

def MTMRlistener():
    rospy.init_node('MTMRlistener', anonymous=False)

    rospy.Subscriber("MTMR/measured_cp", measured_cp, MTMRcallback)
    # rospy.Subscriber("MTMR/measured_cp", measured_cp, callback)

    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

if __name__ == "__main__":

    controller_name = "JOINT_VELOCITY"
    controller_config = load_controller_config(default_controller=controller_name)

    config = {
        "env_name": "TwoArmLift",
        "robots": ["Panda", "Panda"],
        "controller_configs": controller_config,
    }
    
    # initialize the task
    env = suite.make(
        **config,
        has_renderer=True,
        has_offscreen_renderer=False,
        ignore_done=True,
        use_camera_obs=False,
        control_freq=20,
    )
    env.reset()
    env.viewer.set_camera(camera_id=0)

    # Get action limits
    # low, high = env.action_spec

    # print(low, high)

    # start listening to ROS cmd
    MTMLaction = np.zeros(env.robots[0].dof)
    MTMRaction = np.zeros(env.robots[1].dof)
    MTMLlistener()
    # MTMRlistener()

    # print(env.robots[1].dof)

    # do visualization
    while True:
        action = np.append(MTMLaction, MTMRaction)
        print(action)
        _, _, _, _ = env.step(action)
        env.render()
