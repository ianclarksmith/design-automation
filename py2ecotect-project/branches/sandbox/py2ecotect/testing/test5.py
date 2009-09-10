import py2ecotect as p2e

p2e.doc.model.new()

z1 = p2e.ent.Zone.create("test1")
z2 = p2e.ent.Zone.create("test2")
z3 = p2e.ent.Zone.create("test3")
z4 = p2e.ent.Zone.create("test4")
z4.modf.delete()


z1.state.set_current()
points = ((0,0,0),(10,0,0),(10,0,10),(5,0,20),(5,0,3),)
w1 = p2e.obj.Wall.create(points)

z2.state.set_current()
points = ((0,0,0),(10,0,0),(10,0,10),(5,0,20),(5,0,3),)
w2 = p2e.obj.Wall.create(points)
z2.trfm.move_by_vec((10,0,0))

z3.state.set_current()
points = ((0,0,0),(10,0,0),(10,10,0),(0,10,0))
f3 = p2e.obj.Floor.create(points)
z3.func.extrude_by_vec((0,0,5))

p2e.doc.select.none()
p2e.app.view.fit_grid()

print z2.prop.surface_area()

p2e.doc.calculation.update_adjacencies(sample_size=50, shading=False)

print z2.prop.surface_area()

print "done"