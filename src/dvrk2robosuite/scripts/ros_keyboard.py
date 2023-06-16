#!/usr/bin/env python
import numpy as np
import rospy
from dvrk2robosuite.msg import measured_js, measured_cv, measured_cp
import robosuite as suite
from robosuite import load_controller_config

def MTMLcallback(data):
    global MTMLaction
    # MTMLaction[0] = data.transform.translation.x
    # MTMLaction[1] = data.transform.translation.y
    # MTMLaction[2] = data.transform.translation.z
    # MTMLaction[3] = data.transform.rotation.x
    # MTMLaction[4] = data.transform.rotation.y
    # MTMLaction[5] = data.transform.rotation.z
    # MTMLaction[6] = data.transform.rotation.w
    MTMLaction[0] = data.twist.linear.x
    MTMLaction[1] = data.twist.linear.y
    MTMLaction[2] = data.twist.linear.z
    MTMLaction[3] = data.twist.angular.x
    MTMLaction[4] = data.twist.angular.y
    MTMLaction[5] = data.twist.angular.z



def MTMLlistener():
    # rospy.Subscriber("/MTML/measured_cp", measured_cp, MTMLcallback)
    rospy.Subscriber("/MTML/measured_cv", measured_cv, MTMLcallback)

def MTMLGrippercallback(data):
    global MTMLaction
    MTMLaction[6] = data.position[0]

def MTMLGripperlistener():
    rospy.Subscriber("/MTML/gripper/measured_js", measured_js, MTMLGrippercallback)

def MTMRcallback(data):
    global MTMRaction
    for i in range(7):
        MTMRaction[i] = data.velocity[i]

def MTMRlistener():
    rospy.Subscriber("/MTMR/measured_cv", measured_cv, MTMRcallback)

def MTMRGrippercallback(data):
    global MTMRaction
    MTMRaction[-1] = data.velocity[0]

def MTMRGripperlistener():
    rospy.Subscriber("/MTMR/gripper/measured_cv", measured_cv, MTMRGrippercallback)

if __name__ == "__main__":

    controller_name = "OSC_POSE" # JOINT_VELOCITY IK_POSE
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
    # print(low, high)for i in range(3000):

    # start listening to ROS cmd
    rospy.init_node('DVRKlistener', anonymous=False)
    # MTMLaction = np.zeros(env.robots[0].dof)
    # MTMRaction = np.zeros(env.robots[1].dof)
    MTMLaction = np.zeros(7) # 6 dof + gripper?
    MTMRaction = np.zeros(7)
    
    # MTMRlistener()
    # MTMLGripperlistener()
    # MTMRGripperlistener()

    # print(env.robots[1].dof)

    # do visualization
    while True:
        MTMLlistener()
        action = np.append(MTMLaction, MTMRaction)
        print(action)
        _, _, _, _ = env.step(action)
        env.render()
