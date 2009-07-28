from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import Wall
from py2ecotect.view import View
from py2ecotect import model
from py2ecotect.model import Model

m = Model()
#m.load_new()

zones = model._zones
print len(zones)
print m.get_nodes()
print m.get_zones()

"""
zn1 = Zone.create_zone("TEST")
#zn1.set_current()

points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
wall_1 = Wall.create_point(points)
#print wall_1.get_area()
#wall_1.add_node((10000,10000,10000))



objects = zn1.get_objects()
nodes = []
for i in objects:
    nodes.append(i.get_nodes())

print nodes

#zn1.delete()


v = View()
v.redraw()
"""

