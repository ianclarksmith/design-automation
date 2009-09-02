import py2rhino as p2r
"""
vertices = ((0,0,0),(10,0,0),(10,10,0),(0,10,0))
faces = ((0,1,2,2),(0,2,3,3))
mesh1 = p2r.obj.Mesh.create(vertices, faces)
print mesh1
"""

arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
arc2 = arc1.defm.trfm(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))

print arc2


print "done"
