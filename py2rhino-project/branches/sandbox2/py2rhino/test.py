import py2rhino as p2r

points = ( (0,0,0),(20,0,0),(40,40,0),(20,40,0),(-20,10,0), )

print p2r

nc = p2r.obj.NurbsCurve.create_by_pnts(points, 3)

nc2 = nc.dupl.copy_move((0,0,20))
nc3 = nc.dupl.copy_move((0,0,40))

sf = p2r.obj.NurbsSurface.create_by_loft( [nc, nc2, nc3] )

print "done"