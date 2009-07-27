import py2rhino as p2r
ui_o = p2r.UserInterface()
pt_origin = ui_o.get_points("Plane origin")
print str(pt_origin)