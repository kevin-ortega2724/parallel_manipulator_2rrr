#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Pose, Twist

def publish_link_state():
    rospy.init_node('link_state_publisher', anonymous=True)
    pub = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=10)
    
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        state_msg = LinkState()
        state_msg.link_name = "nombre_del_link_que_quieres_mover"
        state_msg.pose = Pose()  # Configura la pose (posición y orientación) aquí
        state_msg.twist = Twist()  # Configura la velocidad (lineal y angular) aquí
        state_msg.reference_frame = "world"  # o el marco de referencia que estés utilizando

        pub.publish(state_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_link_state()
    except rospy.ROSInterruptException:
        pass

