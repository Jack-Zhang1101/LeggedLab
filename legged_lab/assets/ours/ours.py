# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for Unitree robots.

The following configurations are available:

* :obj:`G1_MINIMAL_CFG`: G1 humanoid robot with minimal collision bodies

Reference: https://github.com/unitreerobotics/unitree_ros
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from legged_lab.assets import ISAAC_ASSET_DIR




ATOM_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/ours/atom/atom.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=1
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52),
        joint_pos={
            'left_hip_roll_joint': 0.,
            'left_hip_yaw_joint': 0.,
            'left_hip_pitch_joint': -0.25,
            'left_knee_joint': 0.7,
            'left_ankle_joint': -0.45,
            'left_shoulder_pitch_joint': 0.0,
            'left_shoulder_roll_joint': 0.0,
            'left_shoulder_yaw_joint': 0.0,
            'left_elbow_joint': 0.0,



            'right_hip_roll_joint': 0.,
            'right_hip_yaw_joint': 0.,
            'right_hip_pitch_joint': -0.25,
            'right_knee_joint': 0.7,
            'right_ankle_joint': -0.45,
            'right_shoulder_pitch_joint': 0.0,
            'right_shoulder_roll_joint': 0.0,
            'right_shoulder_yaw_joint': 0.0,
            'right_elbow_joint': 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.90,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_roll_joint",
                ".*_hip_yaw_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint",
                
                
            ],
            effort_limit_sim={
                ".*_hip_roll_joint":20.0,
               ".*_hip_yaw_joint":20.0,
                ".*_hip_pitch_joint": 20.0,
                ".*_knee_joint": 20.0,
            },
            velocity_limit_sim={
                ".*_hip_roll_joint":25.0,
               ".*_hip_yaw_joint":25.0,
                ".*_hip_pitch_joint": 25.0,
                ".*_knee_joint": 25.0,
            },
            stiffness={
                ".*_hip_roll_joint":40,
               ".*_hip_yaw_joint":40,
                ".*_hip_pitch_joint": 40.0,
                ".*_knee_joint": 40.0,
        
            },
            damping={
                ".*_hip_roll_joint":1.5,
               ".*_hip_yaw_joint":1,
                ".*_hip_pitch_joint": 1.25,
                ".*_knee_joint": 1.25,
            },
            armature=0.01,
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[ ".*_ankle_joint"],
            effort_limit_sim={
                 ".*_ankle_joint": 12.0,
            },
            velocity_limit_sim={
                ".*_ankle_joint": 25.0,
            },
            stiffness=35.0,
            damping=0.25,
            armature=0.01,
        ),
        "shoulders": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_pitch_joint",
                ".*_shoulder_roll_joint",
            ],
            effort_limit_sim={
                ".*_shoulder_pitch_joint": 5.0,
                ".*_shoulder_roll_joint": 5.0,
            },
            velocity_limit_sim={
                ".*_shoulder_pitch_joint": 10.0,
                ".*_shoulder_roll_joint": 10.0,
            },
            stiffness=8.0,
            damping=0.2,
            armature=0.01,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_yaw_joint",
                ".*_elbow_joint",
            ],
            effort_limit_sim={
                ".*_shoulder_yaw_joint": 5.0,
                ".*_elbow_joint": 5.0,
            },
            velocity_limit_sim={
                ".*_shoulder_yaw_joint": 10.0,
                ".*_elbow_joint": 10.0,
            },
            stiffness=8.0,
            damping=0.2,
            armature=0.1,
        ),

        #no wrist joints for atom

        # "wrist": ImplicitActuatorCfg(
        #     joint_names_expr=[
        #         ".*_wrist_.*",
        #     ],
        #     effort_limit_sim={
        #         ".*_wrist_yaw_joint": 5.0,
        #         ".*_wrist_roll_joint": 25.0,
        #         ".*_wrist_pitch_joint": 5.0,
        #     },
        #     velocity_limit_sim={
        #         ".*_wrist_yaw_joint": 22.0,
        #         ".*_wrist_roll_joint": 37.0,
        #         ".*_wrist_pitch_joint": 22.0,
        #     },
        #     stiffness=40.0,
        #     damping=2.0,
        #     armature=0.01,
        # ),
    },
)


DUCK_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/ours/atom/atom.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=1
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.42),
        joint_pos={
            'left_hip_yaw_joint': 0.0,
            'left_hip_roll_joint': -0.05,
            'left_hip_pitch_joint': -0.4,
            'left_knee_joint': 0.9,
            'left_ankle_joint': -0.5,

            'right_hip_yaw_joint': 0.,
            'right_hip_roll_joint': 0.05,
            'right_hip_pitch_joint': -0.4,
            'right_knee_joint': 0.9,
            'right_ankle_joint': -0.5,



        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.90,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_roll_joint",
                ".*_hip_yaw_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint",
                
                
            ],
            effort_limit_sim={
                ".*_hip_roll_joint":20.0,
               ".*_hip_yaw_joint":20.0,
                ".*_hip_pitch_joint": 20.0,
                ".*_knee_joint": 20.0,
            },
            velocity_limit_sim={
                ".*_hip_roll_joint":25.0,
               ".*_hip_yaw_joint":25.0,
                ".*_hip_pitch_joint": 25.0,
                ".*_knee_joint": 25.0,
            },
            stiffness={
                ".*_hip_roll_joint":40,
               ".*_hip_yaw_joint":40,
                ".*_hip_pitch_joint": 40.0,
                ".*_knee_joint": 40.0,
        
            },
            damping={
                ".*_hip_roll_joint":2.0,
               ".*_hip_yaw_joint":2.0,
                ".*_hip_pitch_joint": 2.0,
                ".*_knee_joint": 2.0,
            },
            armature=0.01,
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[ ".*_ankle_joint"],
            effort_limit_sim={
                 ".*_ankle_joint": 18.0,
            },
            velocity_limit_sim={
                ".*_ankle_joint": 25.0,
            },
            stiffness=25.0,
            damping=0.5,
            armature=0.01,
        ),
        #no shoulder and arm for duck
        # "shoulders": ImplicitActuatorCfg(
        #     joint_names_expr=[
        #         ".*_shoulder_pitch_joint",
        #         ".*_shoulder_roll_joint",
        #     ],
        #     effort_limit_sim={
        #         ".*_shoulder_pitch_joint": 5.0,
        #         ".*_shoulder_roll_joint": 5.0,
        #     },
        #     velocity_limit_sim={
        #         ".*_shoulder_pitch_joint": 10.0,
        #         ".*_shoulder_roll_joint": 10.0,
        #     },
        #     stiffness=8.0,
        #     damping=0.2,
        #     armature=0.01,
        # ),
        # "arms": ImplicitActuatorCfg(
        #     joint_names_expr=[
        #         ".*_shoulder_yaw_joint",
        #         ".*_elbow_joint",
        #     ],
        #     effort_limit_sim={
        #         ".*_shoulder_yaw_joint": 5.0,
        #         ".*_elbow_joint": 5.0,
        #     },
        #     velocity_limit_sim={
        #         ".*_shoulder_yaw_joint": 10.0,
        #         ".*_elbow_joint": 10.0,
        #     },
        #     stiffness=8.0,
        #     damping=0.2,
        #     armature=0.1,
        # ),

        #no wrist joints for atom

        # "wrist": ImplicitActuatorCfg(
        #     joint_names_expr=[
        #         ".*_wrist_.*",
        #     ],
        #     effort_limit_sim={
        #         ".*_wrist_yaw_joint": 5.0,
        #         ".*_wrist_roll_joint": 25.0,
        #         ".*_wrist_pitch_joint": 5.0,
        #     },
        #     velocity_limit_sim={
        #         ".*_wrist_yaw_joint": 22.0,
        #         ".*_wrist_roll_joint": 37.0,
        #         ".*_wrist_pitch_joint": 22.0,
        #     },
        #     stiffness=40.0,
        #     damping=2.0,
        #     armature=0.01,
        # ),
    },
)

