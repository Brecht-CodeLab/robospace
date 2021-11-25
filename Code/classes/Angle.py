import numpy as np
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


    def calcJacob(self, a):
        a0 = a[0]
        a1 = a[1]
        a2 = a[2]

        l1 = self.l1
        l2 = self.l2

        J = np.array([
            [-l1*sin(a0)*cos(a1)-l2*sin(a0)*cos(a1+a2), -l1*cos(a0)*sin(a1)-l2*cos(a0)*sin(a1+a2), -l2*cos(a0)*sin(a1+a2)],
            [-l1*sin(a0)*cos(a1)+l2*cos(a0)*sin(a1+a2), -l1*sin(a0)*sin(a1)-l2*cos(a0)*cos(a1+a2), l2*cos(a2)*cos(a1+a2)],
            [0, l1*cos(a1)+l2*cos(a1+a2), l2*cos(a1+a2)]
        ])

        return J


    def newAngle(self, eps=1e-9, max_iter=1000):
        l1 = self.l1
        l2 = self.l2
        new_a = self.a
        for i in range(max_iter):
            a0 = new_a[0]
            a1 = new_a[1]
            a2 = new_a[2]
            J = self.calcJacob(new_a)
            f = np.array([l1*cos(a0)*cos(a1)+l2*cos(a0)*cos(a1+a2), l1*sin(a0)*cos(a1)+l2*cos(a0)*sin(a1+a2), l1*sin(a1)+l2*sin(a1+a2)])
        
        
        return


    



















