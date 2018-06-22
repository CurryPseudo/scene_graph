from PIL import Image, ImageColor, ImageDraw
from .vectors import *
def testDrawFunc(pos):
    return ImageColor.getrgb("rgb(255,255,0)")

def genDrawColor(color):
    def draw(pos):
        return color
    return draw

def v3ToColor(v):
    nv = v.do(lambda x: int(x * 255))
    x, y, z = nv.tuple
    return ImageColor.getrgb("rgb({0:d},{1:d},{2:d})".format(x,y,z))

def getImage(size, drawFunc):
    width, height = size
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image, "RGB")
    last = None
    for i in range(width):
        for j in range(height):
            now = int((j + i * height) * 100 / (width * height))
            if last == None or last < now :
                print("{0:d}/100".format(now))
                last = now
            cv3 = drawFunc((i,j))
            c = v3ToColor(cv3)
            draw.point((i,j),c)
    return image

    
