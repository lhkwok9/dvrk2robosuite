# dvrk2robosuite

## Prerequisite
Ubuntu 20.04  
[Anaconda](https://docs.anaconda.com/free/anaconda/install/linux/) (to install robosuite in virtual environment)  
[Robosuite](https://robosuite.ai/docs/installation.html)  
[ROS desktop-full](http://wiki.ros.org/noetic/Installation/Ubuntu)  
[catkin_tools](https://catkin-tools.readthedocs.io/en/latest/installing.html) (for catkin build)  

## Building the packages b4 using (don't use catkin_make)
```bash
conda activate robosuite  
catkin clean
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3  
source ./devel/setup.bash  
```

## For each terminal  
```bash
cd ~/dvrk2robosuite
conda activate robosuite  
export ROS_MASTER_URI=http://192.168.3.200:11311  
export ROS_IP=192.168.3.199  
source devel/setup.bash  
```

## First terminal  
```bash
cd ~/dvrk2robosuite
conda activate robosuite  
export ROS_MASTER_URI=http://192.168.3.200:11311  
export ROS_IP=192.168.3.199  
source devel/setup.bash  
export MUJOCO_GL="osmesa"
rosrun dvrk2robosuite simulator.py  
```

## Second terminal
```bash
cd ~/dvrk2robosuite  
conda activate robosuite  
export ROS_MASTER_URI=http://192.168.3.200:11311  
export ROS_IP=192.168.3.199  
source devel/setup.bash  
rosrun dvrk2robosuite leftTranslation.py  
```

## Third terminal (Example cmd)
```bash
rostopic pub -1 /MTML/measured_cp geometry_msgs/TransformStamped
```

## Useful cmd
```bash
roscd dvrk2robosuite/   
rostopic type /MTML/measured_js | rosmsg show
rostopic echo /MTMR/gripper/measured_js
conda activate robosuite  
source devel/setup.bash  
rosrun dvrk2robosuite simulator.py  
```