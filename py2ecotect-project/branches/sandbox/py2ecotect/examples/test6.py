from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import *
from py2ecotect.view import View
from py2ecotect import model
from py2ecotect.model import Model
from py2ecotect.results import Results
from py2ecotect.select import Select
import time

m = Model()
m.load_new()

zones = model._zones
#print len(zones)
#print m.number_of_nodes
#print m.zones


zn1 = Zone.create_zone("TEST")
#zn1.set_current()


points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
floor = Floor.create(points)

points = [(0,0,0),(10000,0,0),(10000,0,5000),(0,0,5000)]
wall_1 = Wall.create(points)

#print wall_1.get_area()
#wall_1.add_node((10000,10000,10000))
#print "Next object:" , m.get_next_object(-1, -1, -1, -1, zn1)

wall_2 = wall_1.duplicate([0, 0, 0])
wall_2.rotate(90, 0)

wall_3 = wall_1.duplicate([0, 10000, 0])

points = [(10000,0,0),(10000,10000,0),(10000,10000,5000),(10000,0,5000)]
wall_4 = Wall.create(points)


points = [(0,0,5000),(10000,0,5000),(10000,10000,5000),(0,10000,5000)]
roof = Roof.create(points)

points = [(3000,0,0),(6000,0,0),(6000,0,2000),(3000,0,2000)]
door = Door.create(points)

points = [(5000,5000,5000),(5000,5000,3000)]
light = Light.create(points)

points = [(0,3000,1000),(0,6000,1000),(0,6000,2000),(0,3000,2000)]
door = Door.create(points)

#wall_2.delete()

points = [(13600,5300,0)]
point_1 = Point.create(points)

sel = Select()
sel.index([wall_1, point_1])


#res = Results()
#print res.get_gains_conduction(zn1, 3)



"""
objects = zn1.objects
nodes = []
for i in objects:
    nodes.append(i.nodes)

print nodes
"""
#zn1.delete()


v = View()
v.redraw()


nodes = wall_4.nodes
for i in nodes:
    print i.position
wall_4.reverse()
v.redraw()
print "----------------------------"
nodes = wall_4.nodes
for i in nodes:
    print i.position


