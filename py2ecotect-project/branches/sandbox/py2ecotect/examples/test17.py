import py2ecotect as p2e

points = (
          (0,0,0),
          (10,0,0),
          (10,0,10),
          (0,0,10),
          )

wall = p2e.obj.Wall.create(points)
wall2 = wall.dupl.copy_move_by_vec((0,10,0))

n = wall2.nodes.first_node_index()
print "node index = ", n

p2e.app.view.redraw()
print p2e.model._objects
print "wall1 id is", wall._eco_id
print "wall2 id is", wall2._eco_id
print "num objects before delete", p2e.model.scan.num_objects()
wall.modf.delete()
print "wall2 id is", wall2._eco_id
print "num objects after delete", p2e.model.scan.num_objects()

n = wall2.nodes.first_node_index()
print "node index = ", n
n = wall2.nodes.first_node()
n.trfm.move_by_vec((5,0,0))

p2e.app.view.redraw()

print "num objects", p2e.model.scan.num_objects()
print p2e.model.scan.objects()
for i in range(p2e.model.scan.num_objects() - 1, -1, -1):
    print "deleting ", i
    o = p2e.model.scan.object_by_id(i)
    print o._eco_id
    o.modf.delete()

p2e.app.view.redraw()
print "done"