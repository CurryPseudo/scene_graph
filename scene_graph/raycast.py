from .camera import *
from .vectors import *
from .ray import *
def raytracing(screenSize, camera, scene):
    def genDir(screenPos):
        def uv(pos):
            x,y = pos.tuple
            w,h = screenSize
            x /= w
            y /= h
            return vector2(x,1 - y)
        screenPosWorld = camera.uvToWorld(uv(screenPos))
        return (camera.pos, screenPosWorld - camera.pos)
    maxDis = 100
    def draw(pos):
        x, y = pos
        start, dir = genDir(vector2(x, y))
        color = scene.raycastColor(Ray(start, norm(dir).do(lambda x:x * maxDis)))
        return color
    return draw

    
    