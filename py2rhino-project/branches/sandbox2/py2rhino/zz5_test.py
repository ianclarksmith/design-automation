import py2rhino as p2r

arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
print arc1.prop.length()
print arc1.prop.mid_pnt()

print "eval = ",  arc1.eval.evaluate(0.5)
print arc1.prop.domain()

arc2 = p2r.Arc.create_copy_move_by_vec(arc1, (0,0,20))
#arc2.trfm.rotate((0,10,0), 90)
arc3 = p2r.Arc.create_copy_move_by_vec(arc1, (0,0,40))
srf = p2r.NurbsSurface.create_by_loft( [arc1, arc2, arc3] )

print srf.func.contour_pnts((0,0,0), (20,0,10), 5)

print srf._rhino_id

print "area = ", srf.prop.area()
print "domain = ", srf.prop.domain(1,)
print "pt = ", srf.eval.evaluate((0.5, 0.5))

print "done"