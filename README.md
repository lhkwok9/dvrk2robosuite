# dvrk2robosuite

## Prerequisite
Ubuntu 20.04  
[Anaconda](https://docs.anaconda.com/free/anaconda/install/linux/) (to install robosuite in virtual environment)  
[Robosuite](https://robosuite.ai/docs/installation.html)  
[ROS desktop-full](http://wiki.ros.org/noetic/Installation/Ubuntu)  
[catkin_tools](https://catkin-tools.readthedocs.io/en/latest/installing.html) (for catkin build)  

## For each terminal  
```bash
conda activate robosuite  
source devel/setup.bash  
```

## First terminal  
```bash
roscore
```  

## Second terminal  
```bash
rosrun dvrk2robosuite ros_keyboard.py  
```

## Third terminal (Example cmd)
```bash
rostopic pub -1 /MTML/measured_js dvrk2robosuite/measured_js '{position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}'  
rostopic pub -1 /MTML/gripper/measured_js dvrk2robosuite/measured_js '{position: [0.0], velocity: [0.0]}'  
```

## Building the packages (don't use catkin_make)
```bash
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3  
source ./devel/setup.bash  
```

## Useful cmd
```bash
roscd dvrk2robosuite/   
rostopic type /MTML/measured_js | rosmsg show
rostopic echo /MTMR/gripper/measured_js
```