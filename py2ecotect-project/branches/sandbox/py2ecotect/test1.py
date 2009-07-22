from py2ecotect.object import Object
from py2ecotect.zone import Zone 
from py2ecotect.model import Model 
from py2ecotect.node import Node 
from py2ecotect.select import Select 
from py2ecotect.selection import Selection 
from py2ecotect.view import View 
import time

z1 = Zone("Test5")

print z1
print z1.id

m = Model()
m.load_new()

o1 = Object('floor', 'zone', True)
Node(o1.id, 0, 0,0,0)
Node(o1.id, 1, 10000,0,0)
Node(o1.id, 2, 10000,10000,0)
Node(o1.id, 3, 0,10000,0)
o1.zone = z1.id
o1.done()

v = View()
v.redraw()




s = Select()
s.none()

o1.selected
time.sleep(2)

se = Selection()
se.move(0.0, 6000.0, 0.0)
se.extrude(0.0, 0.0, 5000)


v.redraw()

time.sleep(2)
v.fit()

print o1.id

#m.save()
