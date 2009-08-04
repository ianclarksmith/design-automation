#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r


arc1 = p2r.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))




print arc1.genr.sub(0.1, 0.2)


print "done"