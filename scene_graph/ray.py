from .vectors import *
class Ray:
    def __init__(self, start, dir):
        self.start = start
        self.dir = dir
    def end(self):
        return self.start + self.dir
