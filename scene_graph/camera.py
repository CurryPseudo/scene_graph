from .vectors import *

class Camera:
    def __init__(self, pos, up, right, dis, size):
        self.pos = pos
        self.up = norm(up)
        self.right = norm(right)
        self.dis = dis
        self.size = size
    def uvToWorld(self, uvPos):  # uvPos : leftBottom 0  rightTop 1   
        dir = self.right.cross(self.up)
        dir = norm(dir)
        center = self.pos + dir.mulF(self.dis)
        uvPos = uvPos - vector2(0.5, 0.5)
        screenPosCenterOffset = uvPos.do2(self.size, lambda uv,s: uv * s)
        spx, spy = screenPosCenterOffset.tuple
        offset = self.right.do(lambda x:x*spx) + self.up.do(lambda x:x*spy)
        return center + offset



        
