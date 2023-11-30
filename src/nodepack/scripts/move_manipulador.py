#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_robot():
    # Inicializa el nodo ROS
    rospy.init_node('move_manipulador_node', anonymous=True)

    # Crea un publicador en el tópico apropiado
    pub = rospy.Publisher('/manipulador_controller/command', JointTrajectory, queue_size=10)

    # Espera a que los suscriptores se conecten
    rospy.sleep(1)

    # Define la trayectoria del mensaje para el controlador de articulaciones
    traj = JointTrajectory()
    traj.joint_names = ['Joint1', 'Joint1a', 'Joint2', 'Joint2a', 'Joint12a']
    p = JointTrajectoryPoint()
    p.positions = [ 0.02, 0.5, 0.25, 0.0525] # Reemplaza con las posiciones deseadas
    p.velocities = [0.01, 0.01, 0.01, 0.01, 0.01] # Reemplaza con las velocidades deseadas
    p.time_from_start = rospy.Duration(4) # Duración desde el inicio del movimiento
    traj.points = [p]

    # Publica el mensaje
    pub.publish(traj)
    rospy.loginfo("Comando enviado al robot")

    # Espera a que se complete la acción
    rospy.sleep(1)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
