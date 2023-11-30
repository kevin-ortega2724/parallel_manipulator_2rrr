#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
import urdfpy
urdf = urdfpy.URDF.from_parameter_server()
from urdf_parser_py.urdf import URDF

def publish_joint_states():
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10)  # Frecuencia de publicación

    urdf = URDF.from_parameter_server()

    joint_names = []
    joint_positions = []

    while not rospy.is_shutdown():
        for joint_name, joint in urdf.joints.items():
            if joint.type == 'revolute':
                joint_names.append(joint_name)
                joint_positions.append(0.0)  # Cambia esto para obtener la posición real de la articulación

        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = joint_names
        joint_state_msg.position = joint_positions

        joint_state_publisher.publish(joint_state_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        joint_state_publisher = rospy.Publisher('/joint_states', JointState, queue_size=10)
        publish_joint_states()
    except rospy.ROSInterruptException:
        pass

