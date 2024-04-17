#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import yaml

WIDTH = 0.2032  # (m)
WHEEL_LENGTH = 0.0381  # (m)
MAX_STEER =  0.3 # 0.36  # (rad)
MAX_SPEED = 12.0  # (m/s)


def generate_launch_description():
    ld = LaunchDescription()
    print(os.getcwd())
    config = os.path.join(
        'src',
        'pure_pursuit',
        'config',
        'params.yaml'
    )
    config_dict = yaml.safe_load(open(config, 'r'))
    pure_pursuit_node = Node(
        package="pure_pursuit",
        executable="pure_pursuit_node.py",
        name="pure_pursuit_node",
        output="screen",
        emulate_tty=True,
        parameters=[
            # YAML Params
            config_dict,

            # RVIZ Params
            {"visualize": True},
            
            
            {'max_steer': 0.35},


            # interp
            {'minL': 0.5},
            {'maxL': 2.0},
            {'minP': 0.4},
            {'maxP': 0.8},
            {'interpScale': 20},
            {'Pscale': 6.0},
            {'Lscale': 6.0},
            {'D': 2.0},
            {'vel_scale': 0.7},


            # corner
            {'minL_corner': 0.5},
            {'maxL_corner': 2.0},
            {'minP_corner': 0.3},
            {'maxP_corner': 0.3},
            {'Pscale_corner': 7.0},
            {'Lscale_corner': 7.0},


        ]
    )
    ld.add_action(pure_pursuit_node)

    lane_visualize_node = Node(
        package="pure_pursuit",
        executable="lane_visualize.py",
        name="lane_visualize",
        output="screen",
        emulate_tty=True,
        parameters=[
            # YAML Params
            config_dict,

            # RVIZ Params
            {"visualize": True},
        ]
    )
    ld.add_action(lane_visualize_node)

    return ld
