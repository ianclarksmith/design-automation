from py2ecotect.object import Object
from py2ecotect.zone import Zone 
from py2ecotect.model import Model 
from py2ecotect.node import Node 
from py2ecotect.select import Select 
from py2ecotect.selection import Selection 
from py2ecotect.view import View 
import random

points2 = []
for i in range(10):
    points2.append((random.randint(1000, 10000),random.randint(1000, 10000),0))


points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
floor = Object.create_object_by_points('floor', 'plane', points2, True)

v = View()
v.redraw()