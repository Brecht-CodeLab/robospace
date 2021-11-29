from classes.Angle import Angle
from classes.Connection import Connection
import RPI.GPIO as GPIO
import numpy as np
import time

# PARAMETERS
L = np.array([1,1])
angle = np.array([np.pi/4, 0.56, 1.58])
pos = np.array([0,0,1])

# SETUP
GPIO.setmode(GPIO.BOARD)


next_angles = Angle(angle, pos, L)

print(next_angles.newAngles())