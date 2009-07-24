from py2ecotect.object import Object
from py2ecotect.zone import Zone 
from py2ecotect.model import Model 
from py2ecotect.node import Node 
from py2ecotect.select import Select 
from py2ecotect.selection import Selection 
from py2ecotect.view import View 
import time

m = Model()
#m.load_new()

print 'num objects in mode = ', m.get_objects()

z1 = Zone("Test5")

print z1
print z1.id

print 'num objects in mode A= ', m.get_objects()

floor = Object.create_object('floor', 'plane', True)
Node(floor.eco_id, 0, 0,0,0)
Node(floor.eco_id, 1, 10000,0,0)
Node(floor.eco_id, 2, 10000,10000,0)
Node(floor.eco_id, 3, 0,10000,0)
floor.zone = z1.id
floor.done()

print 'num objects in mode B= ', m.get_objects()

wall_1 = Object.create_object('wall', 'plane', True)
Node(wall_1.eco_id, 0, 0,0,0)
Node(wall_1.eco_id, 1, 10000,0,0)
Node(wall_1.eco_id, 2, 10000,0,5000)
Node(wall_1.eco_id, 3, 0,0,5000)
wall_1.zone = z1.id
wall_1.done()

wall_1.duplicate(0, 10000, 0)
wall_1.duplicate(0, 0, 0)
wall_1.rotate(90, 0)

wall_2 = Object.create_object('wall', 'plane', True)
Node(wall_2.eco_id, 0, 10000,0,0)
Node(wall_2.eco_id, 1, 10000,0,5000)
Node(wall_2.eco_id, 2, 10000,10000,5000)
Node(wall_2.eco_id, 3, 10000,10000,0)
wall_2.zone = z1.id
wall_2.done()

roof = Object.create_object('roof', 'plane', True)
Node(roof.eco_id, 0, 0,0,5000)
Node(roof.eco_id, 1, 10000,0,5000)
Node(roof.eco_id, 2, 10000,10000,5000)
Node(roof.eco_id, 3, 0,10000,5000)
roof.zone = z1.id
roof.done()

door = Object.create_object('door', 'plane', True)
Node(door.eco_id, 0, 3000,0,0)
Node(door.eco_id, 1, 6000,0,0)
Node(door.eco_id, 2, 6000,0,2000)
Node(door.eco_id, 3, 3000,0,2000)
door.zone = z1.id
door.done()

light = Object.create_object('light', 'point', True)
Node(light.eco_id, 0, 5000,5000,5000)
Node(light.eco_id, 2, 5000,5000,3000)
light.zone = z1.id
light.done()

window = Object.create_object('window', 'plane', False)
Node(window.eco_id, 0, 0,3000,1000)
Node(window.eco_id, 1, 0,6000,1000)
Node(window.eco_id, 2, 0,6000,2000)
Node(window.eco_id, 3, 0,3000,2000)
window.zone = z1.id
window.done()

print "window = ", window.eco_id

wall_2.delete()
wall_3 = Object.create_object('wall', 'plane', True)
Node(wall_3.eco_id, 0, 10000,0,0)
Node(wall_3.eco_id, 1, 10000,0,5000)
Node(wall_3.eco_id, 2, 10000,10000,5000)
Node(wall_3.eco_id, 3, 10000,10000,0)
wall_3.zone = z1.id
wall_3.done()

print "window = ", window.eco_id

print wall_3.eco_id

print "window = ", window.eco_id

v = View()
v.redraw()

"""
time.sleep(1)
window.nudge(2)
v.redraw()

time.sleep(1)
window.nudge(-3)
v.redraw()

time.sleep(1)
light.extrude(2000, 2000, 2000)
v.redraw()
"""

time.sleep(1)
#wall_1.move(1000, 1000, 1000)
#wall_1.normal_move(0)
#wall_1.orient(45, 45)

#wall_2.revolve(0, 34, 1)
#wall_2.rotate_axis(25, 5, 0)
#window.spin(300)

#v.redraw()



"""
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
"""

#m.save()
