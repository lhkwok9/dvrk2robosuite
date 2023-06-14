# dvrk2robosuite

## Prerequisite
Ubuntu 20.04
[Robosuite](https://robosuite.ai/docs/installation.html)  
[ROS desktop-full](http://wiki.ros.org/noetic/Installation/Ubuntu)  
[catkin_tools](https://catkin-tools.readthedocs.io/en/latest/installing.html) (for catkin build)  

## For each terminal  
conda activate robosuite  
roscd dvrk2robosuite/    
source devel/setup.bash  

## First terminal  
roscore  

## Second terminal  
rosrun dvrk2robosuite ros_keyboard.py  

## Third terminal (Example cmd)
rostopic pub -r 20 /MTML/measured_cp dvrk2robosuite/measured_cp 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0  
rostopic pub -1 /MTMR/measured_cp dvrk2robosuite/measured_cp -- -0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0  

After changing:  
chmod +x ....py  
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3  
source ./devel/setup.bash  