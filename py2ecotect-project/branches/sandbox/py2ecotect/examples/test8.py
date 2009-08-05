from py2ecotect.zone import Zone
from py2ecotect.object import _Object
from py2ecotect.object import *
from py2ecotect.view import View
from py2ecotect import model
from py2ecotect.model import Model
from py2ecotect.results import Results
from py2ecotect.select import Select
from py2ecotect.selection import Selection
import time

points = [(0,0,0),(10000,0,0),(10000,10000,0),(0,10000,0)]
floor = Floor.create(points)

points = [(13600,5300,0)]
point_1 = Point.create(points)

points = [(13600,5300,450)]
point_2 = Point.create(points)

#print floor.modf.link(point_1)

#floor.extrude([0, 0, 2400])
floor.revolve(0, 180, 10)

point_1.stat.selected = False

#point_1.stat.selected = True

selection = Selection()
print selection.underground


for i in model._objects:
    print i.prop.element_type, i.eco_id

v = View()
v.redraw()
