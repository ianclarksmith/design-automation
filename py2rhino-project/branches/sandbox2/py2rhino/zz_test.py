#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))


arc2 = arc1.trfm.copy()

p2r.

print "done"