from math import *
from .vectors import *
class Node:
    def __init__(self):
        self.allTrans = lambda x:x 
        self.childs = []
    def addTrans(self, trans):
        oldTrans = self.allTrans
        newTrans = lambda x:trans(oldTrans(x))
        self.allTrans = newTrans
    def addNode(self, node):
        self.childs.append(node)
    def removeNode(self, node):
        self.childs.remove(node)
    def minDis(self, pos, trans):
        finalDis = float("inf")
        finalO = None
        newTrans = lambda x:trans(self.allTrans(x))
        finalTrans = None
        for c in self.childs:
            dis, o, newtrans = c.minDis(pos, newTrans)
            if dis < finalDis:
                finalDis = dis
                finalO = o
                finalTrans = newtrans
        return (finalDis, finalO, finalTrans)
    
def moveOffset(v):
    def trans(sdf):
        return lambda v2: sdf(v2-v)
    return trans
def rotate(axis, angle):
    angle = radians(angle)
    def trans(sdf):
        cosAngle = cos(angle)
        posTrans = lambda v2: v2.mulF(cosAngle) + axis.cross(v2).mulF(sin(angle)) + axis.mulF(dot(axis, v2) * (1 - cosAngle))
        return lambda v2: sdf(posTrans(v2))
    return trans
def scale(s):
    def trans(sdf):
        return lambda v2: s * (sdf(v2.mulF(1/s)))
    return trans
