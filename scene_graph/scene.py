from .vectors import *
from .ray import *
from .objects import *
class Scene:
    def __init__(self, nodes, lights, skyColor):
        self.nodes = nodes
        self.lights = lights
        self.skyColor = skyColor
    def raycastColor(self, ray):
        dis, hitPos, o, trans = self.raycast(ray)
        if o == None:
            return self.skyColor
        
        corSum = vector3(0,0,0)
        for i in range(len(self.lights)):
            lt = self.lights[i]
            ltDir = lt.getDir(hitPos)
            ltRay = Ray(hitPos, -ltDir)
            _, _, no, _ = self.raycast(ltRay)
            if no != None:
                continue
            normal = getNormal(o, hitPos, trans)
            diffuseC = max(dot(normal, norm(-ltDir)), 0)
            specularC = max(dot(norm(-ray.dir), ltDir.reflect(normal)), 0)
            diffuse = lt.color * o.color.mulF(o.diffuse).mulF(diffuseC)
            specular = lt.color * o.color.mulF(o.specular * specularC)
            cor = diffuse + specular
            corSum = corSum + cor
        
        corSum = corSum + o.color.mulF(o.ambient)
        return corSum
    def raycast(self, ray):
        minDis = 0.001
        point = ray.start.copy()
        maxMoveDis = vecLen(ray.dir)
        dis, o, trans = self.nodes.minDis(point, lambda x:x)
        while dis >= minDis and vecLen(point - ray.start) <= maxMoveDis:
            lastPoint = point.copy()
            point = point + norm(ray.dir).mulF(dis)
            dis, o, trans = self.nodes.minDis(point, lambda x:x)
        if vecLen(point - ray.start) > maxMoveDis:
            return (None, None, None, None)
        return (dis, lastPoint, o, trans)


        
            
