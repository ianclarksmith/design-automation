from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import Wall
from py2ecotect.view import View

zn1 = Zone.create_zone("TEST")
zn1.set_current()

points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
#wall_1 = Wall()
wall_1 = Wall.create_point(points)

#wall_1.set_zone(zn1.eco_id)

v = View()
v.redraw()