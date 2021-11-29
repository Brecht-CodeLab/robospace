from classes.Angle import Angle
from classes.Connection import Connection
import numpy as np

L = np.array([1,1])
angle = np.array([np.pi/2, 0.56, 1.58])
pos = np.array([1,1,1])

next_angles = Angle(angle, pos, L)

print(next_angles.newAngles())