#from py2rhino.nurbs_curve import NurbsCurve
import py2rhino as p2r

points = ( (0,0,0),(10,0,0),(20,0,0),(30,0,0),(40,0,0) )


arc1 = p2r.Arc.create_arc_3pt((0,0,0), (20,0,0), (10,10,0))
arc1.transform.move((0,0,0), (10,0,0))







print "done"