import py2rhino as p2r

arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))



arc2 = arc1.dupl.copy_move_by_vec((0,0,20))
arc3 = arc1.dupl.copy_move_by_vec((0,0,40))

srfs = p2r.obj.NurbsSurface.create_by_loft( [arc1, arc2, arc3] )

srf = srfs

u_domain = srf.prop.domain(0)
v_domain = srf.prop.domain(1)

print p2r.util.vector.cross_product( (23,65,867), (3,65,99))

print "done", p2r._version


stuff = ["dfds", "sdfsd", "sdfds"]
