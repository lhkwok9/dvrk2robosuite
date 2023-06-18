#!/usr/bin/env python
import numpy as np
import xml.etree.ElementTree as ET

import rospy
from dvrk2robosuite.msg import measured_js, measured_cv, measured_cp

import robosuite as suite
from robosuite import load_controller_config
from robosuite.utils.camera_utils import CameraMover

def MTMLcallback(data):
    global MTMLaction
    MTMLaction[0] = data.transform.translation.x
    MTMLaction[1] = data.transform.translation.y
    MTMLaction[2] = data.transform.translation.z
    MTMLaction[3] = data.transform.rotation.x
    MTMLaction[4] = data.transform.rotation.y
    MTMLaction[5] = data.transform.rotation.z
    # MTMLaction[6] = data.transform.rotation.w
    # MTMLaction[0] = data.twist.linear.x
    # MTMLaction[1] = data.twist.linear.y
    # MTMLaction[2] = data.twist.linear.z
    # MTMLaction[3] = data.twist.angular.x
    # MTMLaction[4] = data.twist.angular.y
    # MTMLaction[5] = data.twist.angular.z



def MTMLlistener():
    rospy.Subscriber("/MTML/measured_cp", measured_cp, MTMLcallback)
    # rospy.Subscriber("/MTML/measured_cv", measured_cv, MTMLcallback)

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

# def robosuiteLeftTalker():
    # 32 float64: 14 arm joint positions (encoded using 7 sin and 7 cos), 7 arm joint velocities, 3+4 end effector pose, 2 gripper finger positions, and 2 gripper finger velocities
    # pub = rospy.Publisher('/simulator/L/', String, queue_size=10)
    # rate = rospy.Rate(20) # 10hz
    # while not rospy.is_shutdown():
    #     hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        # rate.sleep()

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
        has_offscreen_renderer=True,
        ignore_done=True,
        use_camera_obs=True,
        use_object_obs=False,
        camera_names=["robot0_eye_in_hand", "robot1_eye_in_hand", "customfrontview", "custombirdview"],
        camera_heights=480,
        camera_widths=640,
        control_freq=20,
    )
    env.reset()

    # set up camera
    inp = "birdview"
    # 'frontview' 'birdview' 'agentview' 'sideview' 
    # '<camera mode="fixed" name="customfrontview" pos="0.5029184206441294 -4.461397182381478e-07 1.0513675831326001" quat="0.582611083984375 0.40070417523384094 0.40070414543151855 0.5826116800308228" />'
    # '<camera mode="fixed" name="custombirdview" pos="-1.3877787807814457e-17 0.0 1.400000000000003" quat="0.7071067690849304 0.0 0.0 0.7071067690849304" />'
    from_tag = '<' in inp
    cam_tree = ET.fromstring(inp) if from_tag else ET.Element("camera", attrib={"name": inp})
    CAMERA_NAME = cam_tree.get("name")

    # Create the camera mover
    camera_mover = CameraMover(
        env=env,
        camera=CAMERA_NAME,
        # init_camera_pos= (0.5029184206441294, 0, 1.0513675831326001),
        # init_camera_quat=np.array([0.582611083984375, 0.40070417523384094, 0.40070414543151855, 0.5826116800308228]) #xyzw?
    )

    # Make sure we're using the camera that we're modifying
    camera_id = env.sim.model.camera_name2id(CAMERA_NAME)
    env.viewer.set_camera(camera_id=camera_id)
    # env.viewer.set_camera(camera_id=0)

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
    for i in range(2):
    # while True:
        MTMLlistener()
        action = np.append(MTMLaction, MTMRaction)
        # print(action)
        obs, reward, done, info = env.step(action)
        # print(f"{obs['robot0_joint_pos_cos']=}")
        # print(f"{obs['robot0_joint_pos_sin']=}")
        # print(f"{obs['robot0_joint_vel']=}")
        # print(f"{obs['robot0_eef_pos']=}")
        # print(f"{obs['robot0_eef_quat']=}")
        # print(f"{obs['robot0_gripper_qpos']=}")
        # print(f"{obs['robot0_gripper_qvel']=}")
        # print(f"{obs['robot0_gripper_qpos']=}")
        # print(obs["robot0_eye_in_hand_image"].shape)
        env.render()
