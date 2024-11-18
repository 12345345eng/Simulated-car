import launch
import launch.launch_description_sources
import launch_ros
from ament_index_python.packages import get_package_share_directory
import os

import launch_ros.parameter_descriptions


def generate_launch_description():
     
    urdf_package_path=get_package_share_directory('fishbot_description')

    default_xacro_path=os.path.join(urdf_package_path,'urdf','fishbot/fishbot.urdf.xacro')
    default_rviz_config_path =os.path.join(urdf_package_path,'config','display_robot_model.rviz')
    #default_gazebo_world_path =os.path.join(urdf_package_path,'world','simple_city.world')
    action_declare_arg_mode_path =launch.actions.DeclareLaunchArgument(
         name='model',default_value=str(default_xacro_path),description='jia zai de mo xing wen jian lu jing'
    )

    substitutions_command_result = launch.substitutions.Command(['xacro ',launch.
    substitutions.LaunchConfiguration('model')] )
    robot_description_vaule = launch_ros.parameter_descriptions.ParameterValue(substitutions_command_result,value_type=str)
    
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description':robot_description_vaule}]
    )

    # action_launch_gazebo = launch.actions.IncludeLaunchDescription(
    #      launch.launch_description_sources.PythonLaunchDescriptionSource(
    #          [get_package_share_directory('gazebo_ros'),'/launch','/gazebo.launch.py']
    #      ),
    #      launch_arguments=[('world',default_gazebo_world_path),('verbose','true')]
    # )


   # action_rviz_node = launch_ros.actions.Node(
    #    package='rviz2',
    #    executable='rviz2',
    #    arguments=['-d',default_rviz_config_path] 
   # )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        action_robot_state_publisher,
        #action_launch_gazebo,
        #action_rviz_node, 
    ])