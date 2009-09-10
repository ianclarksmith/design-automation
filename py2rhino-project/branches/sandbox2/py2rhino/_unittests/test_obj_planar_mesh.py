import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):    
    def testPlanarMeshBoxMorph(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)
        
    def testPlanarMeshShear(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(planarmesh2),p2r.obj.Mesh) #TODO: Check if it is suppose to return a mesh.
        
    def testPlanarMeshTrfm(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(planarmesh2),p2r.obj.Mesh) 
        
    def testPlanarMeshCopyMove(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.dupl.copy_move()
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)
        
    def testPlanarMeshCopyMoveByVec(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.dupl.copy_move_by_vec()
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)    
        
    def testPlanarMeshCopyMoveByOffset(self):
        circle = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle,False)
        planarmesh2 = planarmesh1.dupl.copy_by_offset(30)
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)    
        
    def testPlanarMeshGroups(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.grps.groups()
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)
        
    def testPlanarMeshTopGroup(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.grps.top_group()
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
    
    def testPlanarMeshQuadToTriangles(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.modf.quads_to_triangles()
        self.assertEqual(type(planarmesh2),bool)   
        
    def testPlanarMeshIndex(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.mtrl.index()
        self.assertEqual(type(planarmesh2),int)       
        
    def testPlanarMeshSource(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(planarmesh2),int)     
    
    def testPlanarMeshAddMesh(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.rndr.add_mesh()
        self.assertEqual(type(planarmesh2),bool)
           
    def testPlanarMeshHasMesh(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.rndr.has_mesh()
        self.assertEqual(type(planarmesh2),bool)   
                
    def testPlanarMeshHide(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.stat.hide()
        self.assertEqual(type(planarmesh2),int)  
        
    def testPlanarMeshLock(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.stat.lock()
        self.assertEqual(type(planarmesh2),int)  
        
    def testPlanarMeshMatchObjectAttributes(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh2 = p2r.obj.PlanarMesh.create_by_crv(circle2,False)
        match = planarmesh1.stat.match_object_attributes(planarmesh2)
        self.assertEqual(type(match),int)  
        
    def testPlanarMeshResetObjectAttributes(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        reset = planarmesh1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testPlanarMeshMoveToLayoutSpace(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        reset = planarmesh1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testPlanarMeshSelect(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        sel = planarmesh1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testPlanarMeshShow(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        sel = planarmesh1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testPlanarMeshUnlock(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.stat.unlock()
        self.assertEqual(type(planarmesh2),int) 
        
    def testPlanarMeshUnselect(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        sel = planarmesh1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testPlanarMeshIsClosed(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.is_closed()
        self.assertEqual(type(planarmesh2),bool)     

    def testPlanarMeshIsManifold(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.is_manifold()
        self.assertEqual(type(planarmesh2),bool)  
   
    def testPlanarMeshHasFaceNormals(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.has_face_normals()
        self.assertEqual(type(planarmesh2),bool)     
   
    def testPlanarMeshHasTextureCoordinates(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.has_texture_coordinates()
        self.assertEqual(type(planarmesh2),bool)    
   
    def testPlanarMeshHasVertexColors(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.has_vertex_colors()
        self.assertEqual(type(planarmesh2),bool)    
   
    def testPlanarMeshHasVertexNormals(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.test.has_vertex_normals()
        self.assertEqual(type(planarmesh2),bool)    
    
    def testPlanarMeshMirror(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshMove(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshMoveByVec(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshOrient(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        planarmesh2 = planarmesh1.trfm.orient(pl1,pl2)
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshRemap(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshRotate(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)  
        
    def testPlanarMeshScale(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        planarmesh1 = p2r.obj.PlanarMesh.create_by_crv(circle1,False)
        planarmesh2 = planarmesh1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(planarmesh2),p2r.obj.PlanarMesh)
if __name__ == '__main__':
    unittest.main()