from scene_graph.camera import * 
from scene_graph.scene import *
from scene_graph.vectors import *
from scene_graph.objects import *
from scene_graph.node import *
from scene_graph.light import *
from scene_graph.drawPicture import *
from scene_graph.raycast import *

box = Box(vector3(1,1,1), vector3(1, 2, 3), 0.8, 0.1, 0.3)
ball = Sphere(vector3(1,0,0), 1, 0.8, 0.1, 0.3)
candy = Candy(vector3(0,0,1), vector2(1,1), 0.8, 0.1, 0.3)
light = ParallelLight(vector3(1, 1, 0), vector3(-0.7,-0.2,-1))
root = Node()
boxTransNode = Node()
root.addNode(boxTransNode)
boxTransNode.addNode(box)
boxTransNode.addTrans(scale(0.9))
boxTransNode.addTrans(moveOffset(vector3(1,0,0)))
ballTransNode = Node()
root.addNode(ballTransNode)
ballTransNode.addNode(ball)
ballTransNode.addTrans(scale(0.5))
ballTransNode.addTrans(moveOffset(vector3(2.6,0,3)))
ballSub = Node()
ballSub.addNode(ball)
ballSub.addTrans(scale(0.5))
ballSub.addTrans(moveOffset(vector3(0, 0, -2)))
candyTrans = Node()
candyTrans.addNode(candy)
candyTrans.addTrans(scale(1.2))
candyTrans.addTrans(rotate(vector3(0, 0, 1), 30))
candyTrans.addTrans(moveOffset(vector3(2, 0, -7)))
ballTransNode.addNode(candyTrans)
ballTransNode.addNode(ballSub)
scene = Scene(root, [light], vector3(0,0,0))
cameraPos = vector3(6, 7, 8)
dir = -cameraPos
up = vector3(0, 0, 1)
right = -norm(dir).cross(norm(up))
up = -right.cross(dir)
camera = Camera(cameraPos, up, right, 2, vector2(1, 1))
camera.pos = camera.pos - norm(dir).mulF(5)

screenSize = (500, 500)
im = getImage(screenSize, raytracing(screenSize, camera, scene))
im.save("willSuccess5.png")
