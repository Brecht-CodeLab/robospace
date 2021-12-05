import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
from mpl_toolkits import mplot3d
import time
cos = np.cos
sin = np.sin


class Angle:

    def __init__(self, a, pos, l):
        self.a = a
        self.a0 = a[0]
        self.a1 = a[1]
        self.a2 = a[2]

        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        
        self.l = l
        self.l1 = l[0]
        self.l2 = l[1]
        self.l3 = l[2]
        self.l4 = l[3]


    def calcJacob(self, a):
        a0 = a[0]
        a1 = a[1]
        a2 = a[2]

        l1 = self.l1
        l2 = self.l2

        J = np.array([
            [-l1*sin(a0)*cos(a1)-l2*sin(a0)*cos(a1+a2), -l1*cos(a0)*sin(a1)-l2*cos(a0)*sin(a1+a2), -l2*cos(a0)*sin(a1+a2)],
            [l1*cos(a0)*cos(a1)+l2*cos(a0)*cos(a1+a2), -l1*sin(a0)*sin(a1)-l2*sin(a0)*sin(a1+a2), -l2*cos(a2)*sin(a1+a2)],
            [0, l1*cos(a1)+l2*cos(a1+a2), l2*cos(a1+a2)]
        ])

        return J

    def f0(self):
        return np.array([0,0,self.l3 + self.l4])

    def f1(self, a):
        l1 = self.l1
        l2 = self.l2
        a0 = a[0]
        a1 = a[1]
        a2 = a[2]
        return np.array([l1*cos(a0)*cos(a1), l1*sin(a0)*cos(a1), l1*sin(a1)])


    def f2(self, a):
        l1 = self.l1
        l2 = self.l2
        a0 = a[0]
        a1 = a[1]
        a2 = a[2]
        return np.array([l2*cos(a0)*cos(a1+a2), l2*sin(a0)*cos(a1+a2), l2*sin(a1+a2)])


    def newAngles(self, eps=1e-9, max_iter=1000):
        l1 = self.l1
        l2 = self.l2
        new_a = self.a
        for i in range(max_iter):
            J = self.calcJacob(new_a)
            f = self.f0() + self.f1(new_a) + self.f2(new_a)
        
            e = self.pos - f
            new_a = new_a + np.dot(np.linalg.inv(J),e)
            # print(J)
            # print(new_a)
            if(np.linalg.norm(e) < eps):
                # print(f)
                # print(np.cos(new_a[0]))
                break
        
        return new_a


    def armVectors(self, angles):
        arm0 = [0, 0, 0, 0, 0, self.l4]
        arm1 = [arm0[0] + arm0[3], arm0[1] + arm0[4], arm0[2] + arm0[5], 0, 0, self.l3]

        f1 = self.f1(angles)
        f2 = self.f2(angles)

        arm2 = [arm1[0] + arm1[3], arm1[1] + arm1[4], arm1[2] + arm1[5], f1[0], f1[1], f1[2]]
        arm3 = [arm2[0] + arm2[3], arm2[1] + arm2[4], arm2[2] + arm2[5], f2[0], f2[1], f2[2]]
        return np.array([arm0, arm1, arm2, arm3])


    def makeSimpleAngle(self,angles):
        i=0
        for angle in angles:
            while abs(angle) > np.pi:
                if(angle > 0):
                    angle = angle - 2*np.pi
                else:
                    angle = angle + 2*np.pi
            angles[i] = angle
            i+=1
        return angles


    def checkAngles(self,angles,e=1e-2):
        arms = self.armVectors(angles)
        arm3 = arms[3]
        x = arm3[0] + arm3[3]
        y = arm3[1] + arm3[4]
        z = arm3[2] + arm3[5]
        vec = np.array([x, y, z])
        print("Position: ", vec)
        
        if(np.linalg.norm(vec-self.pos) > e):
            return False
        else:
            return True

    
    def vectorSeries(self,diff_angle,original_angle,steps=100):
        step = abs(diff_angle/steps)
        series = [original_angle]
        if(diff_angle < 0):
            while steps != 0:
                series.append(series[-1] - step)
                steps -= 1
        else:
            while steps != 0:
                series.append(series[-1] + step)
                steps -= 1
        return series


    def moveRobot(self,new_angles,ax):
        diff_angles = new_angles - self.a
        v1_series = self.vectorSeries(diff_angles[0],self.a[0])
        v2_series = self.vectorSeries(diff_angles[1],self.a[1])
        v3_series = self.vectorSeries(diff_angles[2],self.a[2])
        for i in range(len(v1_series)):
            arms = self.armVectors([v1_series[i], v2_series[i], v3_series[2]])
            X, Y, Z, U, V, W = zip(*arms)
            ax.quiver(X, Y, Z, U, V, W, colors=['Red','Blue','Yellow','Blue','Red','Red','Blue','Blue','Yellow','Yellow','Blue','Blue'])
            # print(X, Y, Z, U, V, W)
            plt.show(block=False)
        return




    















