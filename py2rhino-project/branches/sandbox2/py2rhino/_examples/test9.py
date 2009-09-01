import py2rhino as p2r

#print p2r.obj.Ellipse.create(( (0,0,0), (1,0,0), (0,0,1)), 10, 5)
#p2r.obj.Cylinder.create((0,0,0), (0,0,20), 5, True)

p2r.obj.Cylinder.create_by_plane( ( (20,0,0),(2,0,0),(0,0,12) ), 18, 2, True )

#p2r.obj.Torus.create_by_plane(( (0,0,0), (1,0,0), (0,0,1) , (0,1,0) ), 10, 2 )