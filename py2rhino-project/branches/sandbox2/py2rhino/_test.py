#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

points = ( (0,0,0),(10,0,0),(20,0,0),(30,0,0),(40,0,0) )

cv1 = p2r.NurbsCurve.create_curve_by_points(points)

print cv1, type(cv1)



print "done"