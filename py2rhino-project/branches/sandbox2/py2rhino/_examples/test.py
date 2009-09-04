import py2rhino as p2r
"""
vertices = ((0,0,0),(10,0,0),(10,10,0),(0,10,0))
faces = ((0,1,2,2),(0,2,3,3))
mesh1 = p2r.obj.Mesh.create(vertices, faces)
print mesh1
"""

"""
srf1 = p2r.obj.NurbsSurface("a6ccfef8-f59d-4207-a2aa-2316f1625b14")
srf2 = p2r.obj.NurbsSurface("f8c4d250-d092-4f58-89f3-06bc79cdce15")

print srf2.func.intersect_2_srfs_test(srf1)
curves = srf2.func.intersect_2_srfs(srf1, create=True)
p2r.obj.Sphere.create(curves[0].prop.start_pnt(), 0.5)"""

br1 = p2r.obj.PolySurface("09c9aced-a04d-48fb-b74f-ac74685529be") 
br2 = p2r.obj.PolySurface("76332eee-2901-471b-8f46-19c4fdb4c07c") 


srf3 = p2r.obj.NurbsSurface("a54c6ede-63d7-4519-8a3d-6446b9d5eae0")


sp1 = p2r.obj.Sphere("95ff2024-758a-47a6-84a4-f4452e8364d2")
sp2 = p2r.obj.Sphere("bb6ab3cf-692e-42bd-b3d1-ee8e01b7e083")

srf4 = p2r.obj.NurbsSurface("25627221-a5b1-4fd1-badc-bc03f781bad4")


ps = p2r.obj.PolySurface("430bf646-4cf6-4a08-b980-c46e16ffbedc")

print ps.func.explode(False)

print "done"
