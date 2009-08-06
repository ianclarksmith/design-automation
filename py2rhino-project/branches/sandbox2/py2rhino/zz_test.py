#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r


arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
arc2 = arc1.trfm.copy()
arc3 = arc1.trfm.copy()
arc2.trfm.move((0,0,0), (0,0,20))
arc3.trfm.move((0,0,0), (0,0,40))

sp1 = p2r.Sphere.create((0,0,0), 10)
sp2 = p2r.Sphere.create((5,0,0), 10)
sp1.func.boolean_intersection([sp2], True)
sp1.func.delete()
sp2.func.delete()

srf1 = p2r.NurbsSurface.create_by_loft([arc1, arc2, arc3])

arc4 = arc3.func.sub(0.1, 0.2)
mv = arc3.trfm.move((0,0,0),(0,0,20))
print arc4


print arc1.prop.domain()
arc1.modf.rebuild(4, 20)

print arc1.test.is_hidden()
arc1.stat.hide()

pl = ((30,0,0), (10,0,0), (0,10,0))
c1 = p2r.Circle.create(pl, 10)
c2 = p2r.Circle.create(pl, 10)
c2.trfm.move_by_vec((5,0,0))
c1.func.boolean_intersection([c2])


"""
arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))


arc2 = arc1.trfm.copy()

p2r.
"""
print "done"