import py2rhino as p2r

cy = p2r.obj.Cylinder.create((0,0,0), (0,0,10), 5, True)
p2r.obj.NurbsCurve.create_by_srf_section(cy, ((0,0,1),(2,0,0),(0,2,0),(0,0,2)))



print "done"