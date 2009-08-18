import py2rhino as p2r


cir1 = p2r.obj.Circle.create_by_3pt((0,0,0), (15,-10,0), (30,0,0))


srf = p2r.obj.NurbsSurface.create_by_planar_crv(cir1)

print srf

print "done"
