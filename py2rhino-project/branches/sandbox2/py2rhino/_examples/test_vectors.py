import py2rhino as p2r

circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
planarmesh3 = planarmesh1.dupl.copy_by_offset(30)

print "done"