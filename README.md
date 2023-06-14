# dvrk2robosuite

conda activate robosuite
roscore
roscd dvrk2robosuite/
source devel/setup.bash
rosrun dvrk2robosuite ros_keyboard.py



chmod +x ....py

rostopic pub -r 20 /MTML/measured_cp dvrk2robosuite/measured_cp 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0
rostopic pub -1 /MTMR/measured_cp dvrk2robosuite/measured_cp 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

After changing:
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3
source ./devel/setup.bash