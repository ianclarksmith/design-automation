import py2rhino as p2r
"""
vertices = ((0,0,0),(10,0,0),(10,10,0),(0,10,0))
faces = ((0,1,2,2),(0,2,3,3))
mesh1 = p2r.obj.Mesh.create(vertices, faces)
print mesh1
"""

mesh1 = p2r.obj.Mesh("3a54b419-d050-47bf-ab96-53491a14dc2e")
nurbscurve1 = p2r.obj.NurbsCurve("ca535942-4860-4c57-bde9-41a42492f82f")

nurbscurve2 = p2r.obj.Polyline.create_by_mesh_pull(nurbscurve1, mesh1)


print nurbscurve2

print "done"
