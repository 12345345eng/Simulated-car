# Simulated-car

cd XXXXXXXXX/Simulated-car-main/chapt6/chapt6_ws
source install/setup.bash
colcon build
ros2 launch fishbot_description display_robot.launch.py model:=XXXXXXX/Simulated-car-main/chapt6/chapt6_ws/src/fishbot_description/urdf/fishbot/fishbot.urdf.xacro
