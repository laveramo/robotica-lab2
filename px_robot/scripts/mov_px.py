from turtle import position
import rospy
import time
# from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand
from jointSrv import jointCommand
import termios, sys, os
TERMIOS = termios


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

def select_joint(tecla,joint):
    if tecla == b'w':
        if joint >= 5:
            joint = 1
        else:
            joint+= 1 
    elif tecla == b's': 
        if joint <= 1:
            joint = 5
        else:
            joint-= 1

    return joint

def change_jposition(tecla,joint):
    if tecla == b'a':
        if position <= (LIM_MAX-DELTA_POS):
            position+= DELTA_POS
            jointCommand('', joint, 'Goal_Position', position, 0.5)
        elif position > (LIM_MAX- DELTA_POS):
            position = LIM_MAX
            jointCommand('', joint, 'Goal_Position', position, 0.5)
        else:
            pass # Qué hacer cuando esta fuera de rango (MIN_LIM, MAX_LIM) NO debería pasar nunca, sirve para evitar bugs, creería yo
        
    elif tecla == b'd':
            if position <= (LIM_MIN + DELTA_POS):
                position = LIM_MIN
                jointCommand('', joint, 'Goal_Position', position, 0.5)
            elif position <= LIM_MAX:
                position -=DELTA_POS
                jointCommand('', joint, 'Goal_Position', position, 0.5)
            else:
                pass # Qué hacer cuando este fuera de rango (MIN_LIM, MAX_LIM) NO debería pasar nunca, sirve para evitar bufs, creería yo




        