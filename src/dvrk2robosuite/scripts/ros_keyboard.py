#!/usr/bin/env python
import numpy as np
import rospy
from dvrk2robosuite.msg import measured_js
import robosuite as suite
from robosuite import load_controller_config

def MTMLcallback(data):
    global MTMLaction
    for i in range(7):
        MTMLaction[i] = data.velocity[i]

def MTMLlistener():
    rospy.Subscriber("MTML/measured_js", measured_js, MTMLcallback)

def MTMLGrippercallback(data):
    global MTMLaction
    MTMLaction[-1] = data.velocity[0]

def MTMLGripperlistener():
    rospy.Subscriber("MTML/gripper/measured_js", measured_js, MTMLGrippercallback)

def MTMRcallback(data):
    global MTMRaction
    for i in range(7):
        MTMRaction[i] = data.velocity[i]

def MTMRlistener():
    rospy.Subscriber("MTMR/measured_js", measured_js, MTMRcallback)

def MTMRGrippercallback(data):
    global MTMRaction
    MTMRaction[-1] = data.velocity[0]

def MTMRGripperlistener():
    rospy.Subscriber("MTMR/gripper/measured_js", measured_js, MTMRGrippercallback)


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
    rospy.init_node('DVRKlistener', anonymous=False)
    MTMLaction = np.zeros(env.robots[0].dof)
    MTMRaction = np.zeros(env.robots[1].dof)
    MTMLlistener()
    MTMRlistener()
    MTMLGripperlistener()
    MTMRGripperlistener()

    # print(env.robots[1].dof)

    # do visualization
    for i in range(3000):
        action = np.append(MTMLaction, MTMRaction)
        print(action)
        _, _, _, _ = env.step(action)
        env.render()
