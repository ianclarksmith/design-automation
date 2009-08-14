import py2rhino.functions as p2r

cv1 = p2r.curve.add_arc_3_pt((0,0,0), (20,0,0), (10,10,0))
cv2 = p2r.curve.add_arc_3_pt((0,0,10), (20,0,10), (10,-10,10))
cv3 = p2r.curve.add_arc_3_pt((0,0,20), (20,0,20), (10,10,20))

srf = p2r.surface_and_polysurface.add_loft_srf((cv1, cv2, cv3))

print "done"



