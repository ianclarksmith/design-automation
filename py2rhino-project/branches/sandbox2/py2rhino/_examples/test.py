import py2rhino as p2r

polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0) ))
mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
nurbscurve1 = p2r.obj.Polyline.create_by_mesh_border(mesh1)

print "done"