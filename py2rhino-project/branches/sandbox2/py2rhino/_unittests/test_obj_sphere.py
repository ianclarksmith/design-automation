import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):  
    def testSphereBoxMorph(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(sphere2),p2r.obj.NurbsSurface)#TODO: Check if the return is suppose to be NurbsSurface
        
    def testSphereShear(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(sphere2),p2r.obj.NurbsSurface)#TODO: Check if the return is suppose to be NurbsSurface
        
    def testSphereTrfm(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(sphere2),p2r.obj.NurbsSurface) 
        
    def testSphereCopyMove(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.dupl.copy_move()
        self.assertEqual(type(sphere2),p2r.obj.Sphere)

    def testSphereCopyMoveByVec(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.dupl.copy_move_by_vec()
        self.assertEqual(type(sphere2),p2r.obj.Sphere)
    
    def testSphereEvaluate(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.eval.evaluate(1)
        self.assertEqual(len(sphere2),3)  

    def testSphereEvalFrame(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.eval.evaluate_frame((0,1))
        self.assertEqual(type(sphere2),tuple)   
    
    def testSphereGroups(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.grps.groups()
        self.assertEqual(type(sphere2),p2r.obj.Sphere)
        
    def testSphereTopGroup(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.grps.top_group()
        self.assertEqual(type(sphere2),p2r.obj.Sphere)   
        
    def testSphereFlip(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.flip()
        self.assertEqual(type(sphere2),bool)  
        
    def testSphereInsertKnot(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.insert_knot(1,0)
        self.assertEqual(type(sphere2),bool)  

    def testSphereRebuild(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.rebuild()
        self.assertEqual(type(sphere2),bool)  
        
    def testSphereRemoveKnot(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.remove_knot((0,1),0)
        self.assertEqual(type(sphere2),bool)  

    def testSphereReverse(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.reverse(1)
        self.assertEqual(type(sphere2),bool)  

    def testSphereShrinkTrimmed(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.modf.shrink_trimmed()
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIndex(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.mtrl.index()
        self.assertEqual(type(sphere2),int)       
        
    def testSphereSource(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(sphere2),int)    
        
    def testSphereDefinition(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.prop.sphere_definition()
        self.assertEqual(len(sphere2),2) 

    def testSphereAddMesh(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.rndr.add_mesh()
        self.assertEqual(type(sphere2),bool)   
        
    def testSphereEnable(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.rndr.enable()
        self.assertEqual(type(sphere2),bool)   
        
    def testSphereHasMesh(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.rndr.has_mesh()
        self.assertEqual(type(sphere2),bool)   

    def testSphereHide(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.stat.hide()
        self.assertEqual(type(sphere2),int)  
        
    def testSphereLock(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.stat.lock()
        self.assertEqual(type(sphere2),int)  
        
    def testSphereIsBrep(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_brep()
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsBrepManifold(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_brep_manifold()
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsParameterOnSrf(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsPointInSrf(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsPointOnSrf(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsPolySurfaceClosed(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_poly_surface_closed()
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsSphere(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_plane_surface()
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsPolySrf(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_poly_srf()
        self.assertEqual(type(sphere2),bool)     
        
    def testSphereIsPolySrfPlanar(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_poly_srf_planar()
        self.assertEqual(type(sphere2),bool)     
        
    def testSphereIsSrfClosed(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_closed(0)
        self.assertEqual(type(sphere2),bool)   
        
    def testSphereIsSrfPeriodic(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_periodic(0)
        self.assertEqual(type(sphere2),bool) 
        
    def testSphereIsSrfPlanar(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_planar()
        self.assertEqual(type(sphere2),bool)  
        
    def testSphereIsSrfRational(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_rational()
        self.assertEqual(type(sphere2),bool)  
        
    def testSphereIsSrfSingular(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_singular(0)
        self.assertEqual(type(sphere2),bool)  
        
    def testSphereIsSrfTrimmed(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.test.is_srf_trimmed()
        self.assertEqual(type(sphere2),bool)

    def testSphereMirror(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereMove(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereMoveByVec(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereOrient(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        sphere2 = sphere1.trfm.orient(pl1,pl2)
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereRemap(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereRotate(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(sphere2),p2r.obj.Sphere)  
        
    def testSphereScale(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(sphere2),p2r.obj.Sphere)     
        
    def testSphereDescription(self):
        sphere1 = p2r.obj.Sphere.create((0,0,0), 3)
        sphere2 = sphere1.util.description()
        self.assertEqual(type(sphere2),unicode)      
        
if __name__ == '__main__':
    unittest.main()   