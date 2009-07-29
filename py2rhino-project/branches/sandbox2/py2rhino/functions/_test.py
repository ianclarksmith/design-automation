import py2rhino.functions as rf

cv1 = rf.curve.add_arc3_pt((0,0,0), (20,0,0), (10,10,0))
cv2 = rf.curve.add_arc3_pt((0,0,10), (20,0,10), (10,-10,10))
cv3 = rf.curve.add_arc3_pt((0,0,20), (20,0,20), (10,10,20))

srf = rf.surface_and_polysurface.add_loft_srf((cv1, cv2, cv3))

print "done"



