import py2rhino as p2r


#create a flat surface in some polygon form
points = ((0,0,0),(15,-10,0), (30,0,0), (30,60,0), (0,0,0))
pline = p2r.obj.Polyline.create(points)
srf1 = p2r.obj.NurbsSurface.create_by_planar_crv(pline)

#create circular surface
cir = p2r.obj.Circle.create_by_3pt((0,0,0), (15,-10,0), (30,0,0))
srf2 = p2r.obj.NurbsSurface.create_by_planar_crv(cir)


pline.trfm.move_by_vec((10,0,0))

print "intersect ", cir.func.boolean_intersection(pline)



#delete construction geometry
#pline.func.delete()
cir.func.delete()



print "done"
