#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

points = ( (0,0,0),(10,0,0),(20,0,0),(30,0,0),(40,0,0) )

cv1 = p2r.NurbsCurve.create_curve_by_points(points)


arc1 = p2r.Arc.create_arc_3pt( (0,0,0), (10,0,0), (5,5,1) )
print "closing carc = ", arc1.close_curve()
print "extend carc = ", arc1.extend_curve_length(0, 0, 2)

print arc1.length()

print cv1, type(cv1)

print "cv1 = ", cv1.rhino_id

cv2 = cv1.split_curve(parameters, delete)

print "cv2 = ", cv2





print "done"