from .vectors import *
class Box:
    def __init__(self, color, size, diffuse, ambient, specular):
        def sdf(v):
            dir = v
            absDir = dir.do(lambda x:abs(x))
            return vecLen((absDir - size).do(lambda x:max(x, 0)))
        self.sdf = sdf
        self.color = color
        self.diffuse = diffuse
        self.ambient = ambient
        self.specular = specular
    def minDis(self, pos, trans):
        return (trans(self.sdf)(pos), self, trans)

class Sphere:
    def __init__(self, color, radius, diffuse, ambient, specular):
        def sdf(v):
            dir = v
            return vecLen(dir) - radius
        self.sdf = sdf
        self.color = color
        self.diffuse = diffuse
        self.ambient = ambient
        self.specular = specular
    def minDis(self, pos, trans):
        return (trans(self.sdf)(pos), self, trans)

def getNormal(o, p, trans):
    x, y, z = p.tuple
    epsilon = 0.0001
    sdf = trans(o.sdf)
    nx = sdf(vector3(x + epsilon, y, z)) - sdf(vector3(x - epsilon, y, z))
    ny = sdf(vector3(x, y + epsilon, z)) - sdf(vector3(x, y - epsilon, z))
    nz = sdf(vector3(x, y, z + epsilon)) - sdf(vector3(x, y, z - epsilon))
    return norm(vector3(nx, ny, nz))

class Candy:
    def __init__(self, color, size, diffuse, ambient, specular):
        def sdf(v):
            x, y, z = v.tuple
            sizex, sizey = size.tuple
            q = vector2(vecLen(vector2(x, z)) - sizex, y)
            return vecLen(q) - sizey
        self.sdf = sdf
        self.color = color
        self.diffuse = diffuse
        self.ambient = ambient
        self.specular = specular
    def minDis(self, pos, trans):
        return (trans(self.sdf)(pos), self, trans)
        




