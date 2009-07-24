import py2ecotect as p2e
print "done"

for i in p2e.__dict__.keys():
    print i

import time

z1 = p2e.Zone("Test5")

print z1
print z1.id

#m = Model()
#m.load_new()

floor = p2e.Object.create_object('floor', 'plane', True)
p2e.Node(floor.eco_id, 0, 0,0,0)
p2e.Node(floor.eco_id, 1, 10000,0,0)
p2e.Node(floor.eco_id, 2, 10000,10000,0)
p2e.Node(floor.eco_id, 3, 0,10000,0)
floor.zone = z1.id
floor.done()


#floor.delete()

v = p2e.View()
v.redraw()