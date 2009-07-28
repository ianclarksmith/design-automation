from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import Wall
from py2ecotect.view import View
from py2ecotect.model import Model
import time

m = Model()
m.load_new()

zn1 = Zone.create_zone("TEST")
#zn1.set_current()

points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
wall_1 = Wall.create_point(points)

objects = zn1.get_objects()
nodes = []
for i in objects:
    nodes.append(i.get_nodes())

print nodes

zn1.delete()


v = View()
v.redraw()