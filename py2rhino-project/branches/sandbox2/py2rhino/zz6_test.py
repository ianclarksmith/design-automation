from py2rhino import functions as rsf

a1 = rsf.curve.add_arc_3_pt((0,0,0), (20,0,0), (10,10,0))
a2 = rsf.curve.add_arc_3_pt((0,0,10), (20,0,10), (10,10,10))
a3 = rsf.curve.add_arc_3_pt((0,0,20), (20,0,20), (10,10,20))
s1 = rsf.surface_and_polysurface.add_loft_srf( [a1, a2, a3] )
print s1
print rsf.surface_and_polysurface.surface_area(s1)