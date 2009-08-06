import time
import py2ecotect as p2e

#points = [(13600,5300,0)]
#point_1 = Point.create(points)

points = [(0,0,0),(10000,0,0),(10000,0,10000),(0,0,10000)]
wall = p2e.Wall.create(points)

#points = [(1000,5000,1000),(10000,0,1000),(10000,0,10000),(1000,-5000,10000)]
#wn = p2e.Window.create(points)
#wn.trfm.scale([0.5,0.5,0.5])
#wl.mdfy.link(wn)
#wn.child.set_child_extents(1000,1000,0.5,0.8)

v = p2e.View()
v.redraw()

print wall.node.nodes
time.sleep(2)

wall.delete()
v.redraw()
print wall.node.nodes

#points = [(13600,5300,450)]
#point_2 = Point.create(points)

#print floor.modf.link(point_1)

#floor.extrude([0, 0, 2400])
#floor.revolve(0, 180, 10)

#point_1.stat.selected = False

#point_1.stat.selected = True

#selection = Selection()
#print selection.underground

#ray = Ray()
#print ray.get_object(1)


#for i in model._objects:
#    print i.prop.element_type, i.eco_id

#v = View()
#v.redraw()

#time.sleep(2)
