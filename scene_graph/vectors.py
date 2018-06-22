import math as m
class vector2:
    def __init__(self, x, y):
        self.tuple = (x, y)
    def doTuple(self, f):
        t = f(self.tuple)
        x, y = t
        return vector2(x, y)
    def do(self, f):
        def d(t):
            x, y = t
            return (f(x), f(y))
        return self.doTuple(d)
    def do2(self, v, f):
        def d(t):
            x1, y1 = t
            x2, y2 = v.tuple
            return (f(x1, x2), f(y1, y2))
        return self.doTuple(d)
    def toList(self):
        x, y = self.tuple
        return [x, y]
    
    def __add__(self, v):
        return self.do2(v, lambda x,y:x+y)
    def __sub__(self, v):
        return self.do2(v, lambda x,y:x-y)
    def __mul__(self, v):
        return self.do2(v, lambda x,y:x*y)
    def __div__(self, v):
        return self.do2(v, lambda x,y:x/y)
    def __neg__(self):
        return self.do(lambda x:-x)
    

class vector3:
    def __init__(self, x, y, z):
        self.tuple = (x, y, z)
    def doTuple(self, f):
        t = f(self.tuple)
        x, y, z = t
        return vector3(x, y, z)
    def do(self, f):
        def d(t):
            x, y, z= t
            return (f(x), f(y), f(z))
        return self.doTuple(d)
    def do2(self, v, f):
        def d(t):
            x1, y1, z1 = t
            x2, y2, z2 = v.tuple
            return (f(x1, x2), f(y1, y2), f(z1, z2))
        return self.doTuple(d)
    def toList(self):
        x, y, z = self.tuple
        return [x, y, z]

    def __add__(self, v):
        return self.do2(v, lambda x,y:x+y)
    def __sub__(self, v):
        return self.do2(v, lambda x,y:x-y)
    def __mul__(self, v):
        return self.do2(v, lambda x,y:x*y)
    def __div__(self, v):
        return self.do2(v, lambda x,y:x/y)
    def __neg__(self):
        return self.do(lambda x:-x)
    def cross(self, v):
        x1, y1, z1 = self.tuple
        x2, y2, z2 = v.tuple
        return vector3(y1 * z2 - y2 * z1, z1 * x2 - z2 * x1, x1 * y2 - x2 * y1)
    def copy(self):
        x, y, z = self.tuple
        return vector3(x, y, z)
    def mulF(self, f):
        return self.do(lambda x:x*f)
    def reflect(self, n):
        n = norm(n)
        return self - n.mulF(2 * dot(self, n))
    def div(self, v):
        return self.do2(v, lambda x,y:x/y)

def vecLen(v):
    return m.sqrt(sumV(v, lambda x: x**2))
def sumV(v, f):
    l = v.toList()
    sum = 0
    for i in range(len(l)):
        sum = sum + f(l[i])
    return sum


def norm(v):
    l = vecLen(v)
    if l == 0:
        return v.do(lambda x:0)
    return v.do(lambda x: x/l)

def id(x):
    return x

def dot(v1, v2):
    v3 = v1 * v2
    return sumV(v3, id)


