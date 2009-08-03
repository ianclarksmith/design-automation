#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

points = ( (0,0,0),(10,0,0),(20,0,0),(30,0,0),(40,0,0) )


cv1 = p2r.NurbsCurve.create_by_points(points)

cv1.evaluate.evaluate(0.5)
cv1.modify.simplify_curve()





print "done"