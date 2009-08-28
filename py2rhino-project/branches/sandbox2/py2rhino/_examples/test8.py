import py2rhino as p2r

points = ( (0,0,0),(0,10,0),(20,20,0),(50,-30,0)  )

crv = p2r.obj.NurbsCurve.create_by_pnts(points, 3)

pl = p2r.obj.Polyline.create(points)


print crv