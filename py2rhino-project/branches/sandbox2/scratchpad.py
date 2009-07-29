import py2rhino.functions as p2r

points = ( (0,0,0), (10,20,0), (20,-20,0), (30,0,0) )

p2r.curve.add_curve(points, 4)

points = ( (0,0,10), (10,20,10), (20,-20,10), (30,0,10) )

p2r.curve.add_nurbs_curve(points)