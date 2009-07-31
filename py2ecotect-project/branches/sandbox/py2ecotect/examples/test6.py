from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import Wall
from py2ecotect.view import View
from py2ecotect import model
from py2ecotect.model import Model
from py2ecotect.results import Results

m = Model()
#m.load_new()

zones = model._zones
print len(zones)
print m.number_of_nodes
print m.zones


zn1 = Zone.create_zone("TEST")
#zn1.set_current()


points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
wall_1 = Wall.create(points)
#print wall_1.get_area()
#wall_1.add_node((10000,10000,10000))
#print "Next object:" , m.get_next_object(-1, -1, -1, -1, zn1)

res = Results()
print res.get_gains_conduction(zn1, 3)




objects = zn1.objects
nodes = []
for i in objects:
    nodes.append(i.nodes)

print nodes

#zn1.delete()


v = View()
v.redraw()


