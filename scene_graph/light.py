from .vectors import *
class ParallelLight:
    def __init__(self, color, dir):
        self.color = color
        self.dir = dir
    def getDir(self, pos):
        return self.dir
    
