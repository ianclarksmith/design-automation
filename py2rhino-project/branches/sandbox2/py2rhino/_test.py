#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

points = ( (0,0,0),(10,0,0),(20,0,0),(30,0,0),(40,0,0) )

cv1 = p2r.NurbsCurve.create_curve_by_points(points)

print cv1.rhino_id
print cv1.modify.rhino_id

for i in cv1.modify.__dict__.keys():
    print i

#cv1.modify.rebuild_curve(3, 12)


print "done"