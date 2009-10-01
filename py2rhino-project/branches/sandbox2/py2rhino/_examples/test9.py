import py2rhino as p2r
    
pline = p2r.obj.Polyline.create([(0,0,0), (20,0,0), (10,10,0) ])

cir1 = p2r.obj.Circle.create_by_3pt((0,0,0), (15,-10,0), (30,0,0))
cir2 = p2r.obj.Circle.create_by_3pt((0,0,0), (15,-20,0), (30,0,0))

srfs = p2r.obj.NurbsSurface.create_by_planar_crv(cir1)

grp = p2r.ent.Group.create()
print grp._name
grp.objs.add_objects([cir1, cir2])

lay = p2r.ent.Layer.create()

blocks = p2r.doc.block.blocks()
p2r.ent.BlockInstance.create(blocks[0], (0,0,0))
print lay
print srfs

print "done"
