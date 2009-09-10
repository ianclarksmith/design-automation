import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testMeshBoxMorph(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
        
    def testMeshShear(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
                
    def testMeshTransform(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.defm.transform(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(mesh2),p2r.obj.Line) 
                    
    def testMeshCopyMove(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.dupl.copy_move()
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
        
    def testMeshCopyMoveByVec(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.dupl.copy_move_by_vec()
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
        
    def testMeshCopyByOffset(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.dupl.copy_by_offset(mesh1,2)
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
        
    def testMeshGroups(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.grps.groups()
        self.assertEqual(type(mesh2),p2r.obj.Mesh)
        
    def testMeshTopGroup(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.grps.top_group()
        self.assertEqual(type(mesh2),p2r.obj.Mesh)   
        
    def testMeshQuadToTriangles(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.modf.quads_to_triangles()
        self.assertEqual(type(mesh2),bool)   
        
    def testMeshIndex(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.mtrl.index()
        self.assertEqual(type(mesh2),int)       
        
    def testMeshSource(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        mesh2 = mesh1.mtrl.source(0)              
        self.assertEqual(type(mesh2),int)         

    def testMeshAddMesh(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.rndr.add_mesh()
        self.assertEqual(type(mesh2),bool)   
        
    def testMeshEnable(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.rndr.enable()
        self.assertEqual(type(mesh2),bool)   
        
    def testMeshHasMesh(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.rndr.has_mesh()
        self.assertEqual(type(mesh2),bool)  
    
    def testMeshHide(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.stat.hide()
        self.assertEqual(type(mesh2),int)  
        
    def testMeshLock(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.stat.lock()
        self.assertEqual(type(mesh2),int)       
        
    def testMeshIsClosed(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.test.is_closed()
        self.assertEqual(type(mesh2),bool)     

    def testMeshIsManifold(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.test.is_manifold()
        self.assertEqual(type(mesh2),bool)  
   
    def testMeshHasFaceNormals(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.test.has_face_normals()
        self.assertEqual(type(mesh2),bool)     
   
    def testMeshHasTextureCoordinates(self):
        mesh1 = p2r.obj.Mesh.create(((0,0,0),(5,0,0),(10,0,0),(0,5,0),(5,5,0),(10,5,0),(0,10,0),(5,10,0),(10,10,0)), ((0,1,4,4),(2,4,1,1),(0,4,3,3),(2,5,4,4),(3,4,6,6),(5,8,4,4),(6,4,7,7),(8,7,4,4)))
        mesh2 = mesh1.test.has_texture_coordinates()
        self.assertEqual(type(mesh2),p2r.obj.Mesh)    
   
    def testMeshHasVertexColors(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.test.has_vertex_colors()
        self.assertEqual(type(mesh2),bool)    
   
    def testMeshHasVertexNormals(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.test.has_vertex_normals()
        self.assertEqual(type(mesh2),bool)    
    
    def testMeshMirror(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshMove(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshMoveByVec(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshOrient(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        mesh2 = mesh1.trfm.orient(pl1,pl2)
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshRemap(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshRotate(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(mesh2),p2r.obj.Mesh)  
        
    def testMeshScale(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(mesh2),p2r.obj.Mesh)     
        
    def testMeshDescription(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.util.description()
        self.assertEqual(type(mesh2),unicode)   
        
    def testMeshDump(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,0)))
        mesh1 = p2r.obj.Mesh.create_by_polyline(polyline1)
        mesh2 = mesh1.util.dump()
        self.assertEqual(type(mesh2),unicode)     
        
if __name__ == '__main__':
    unittest.main()    