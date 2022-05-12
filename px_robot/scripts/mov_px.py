from turtle import position
import rospy
import time
# from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand
from jointSrv import jointCommand
import termios, sys, os
TERMIOS = termios
import numpy as np


LIM_MIN = 0 #Mínimo valor para la posición de la articulación
LIM_MAX = 1023 #Máximo valor para la posicion de las articuaciones

DELTA_POS = 15 #Variación del ángulo de las articulaciones


def getKey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def actions(tecla,joint):
    if tecla == b'w':
        if joint >= 5:
            joint = 1
        else:
            joint+= 1
        print("Junta", joint, "seleccionada.", "Oprima A para llevar la junta a home o D para llevarla a un valor específico") 
    elif tecla == b's': 
        if joint <= 1:
            joint = 5
        else:
            joint-= 1

        print("Junta", joint, "seleccionada","Oprima A para llevar la junta a home o D para llevarla a un valor específico") 

    elif tecla == b'a':
        jointCommand('', joint, 'Goal_Position', 512, 0.5)

    elif tecla == b'd':
        new_position = int(input("Ingrese la posición deseada de la junta en bits: min 0, max 1023 :"))
        jointCommand('', joint, 'Goal_Position', new_position,0.5)
    else:
        print("Error, oprima W/S para cambiar la junta, A para llevar la junta seleccionada a home y D para llevarla a una posición expecífica")
    
    return joint
if __name__ == '__main__':
    try:
        print("Presione Q para salir")
        print("Presione W/S para cambiar la junta, A para llevar la junta seleccionada a home y D para llevarla a una posición expecífica")
        jointCommand('', 1, 'Torque_Limit', 600, 0)
        jointCommand('', 2, 'Torque_Limit', 500, 0)
        jointCommand('', 3, 'Torque_Limit', 400, 0)
        jointCommand('', 4, 'Torque_Limit', 400, 0)

        current_joint = 1
        while(1):
            tecla = getKey()
            current_joint = actions(tecla,current_joint)
            if tecla == b'q':
                break
        
    except rospy.ROSInterruptException:
        pass



        