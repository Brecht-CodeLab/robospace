from numpy.lib.polynomial import polysub
from classes.Angle import Angle
from classes.Connection import Connection
import matplotlib.pyplot as plt
import matplotlib.animation as an
from mpl_toolkits import mplot3d
# import RPI.GPIO as GPIO
import numpy as np
import time

## PARAMETERS
L = np.array([20,20,20,20])
angles = np.array([np.pi/4, 0.56, 1.58])
pos = np.array([0,0,1])
print(pos)

## SETUP
# GPIO.setmode(GPIO.BOARD)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([0, 80])



## LOOP
go = True
while go:
    posx = float(input('Pos x: '))
    posy = float(input('Pos y: '))
    posz = float(input('Pos z: '))
    pos = np.array([posx,posy,posz])
    print("Given postition: ", pos)
    
    robot = Angle(angles, pos, L)
    nextAngles = robot.newAngles()
    print("Angles before: ", nextAngles)
    nextAngles = robot.makeSimpleAngle(nextAngles)
    print("Angles after: ", nextAngles)
    check = robot.checkAngles(nextAngles)
    print("Check position: ", check)


    if(check == False):
        print("Unreachable position, please try again")
    else:
        robot.moveRobot(nextAngles,ax)
        angles = nextAngles

    













