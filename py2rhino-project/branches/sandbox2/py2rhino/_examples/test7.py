import py2rhino as p2r

points = ( (0,0,0),(0,10,0),(20,20,0),(50,-30,0)  )




crv = p2r.obj.NurbsCurve.create_by_pnts(points, 3)



print crv.prop.domain()

"""
sph = p2r.obj.Sphere.create((0,0,0), 9)

intsct = crv.func.srf_intersection(sph)

print intsct

p2r.obj.Sphere.create(intsct[0][1], 1)
p2r.obj.Sphere.create(intsct[0][4], 1)
#print crv.func.divide_crv(30, False, True)

ln1 = p2r.obj.Line.create((0,0,0), (10,3,0))
ln2 = p2r.obj.Line.create((0,0,0), (1,10,0))

print p2r.obj.Arc.create_by_fillet(ln1, ln2, 2)
"""