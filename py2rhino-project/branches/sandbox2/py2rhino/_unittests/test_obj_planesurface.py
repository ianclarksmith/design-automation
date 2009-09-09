import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):    
    def testPlaneSurfaceBoxMorph(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)
        
    def testPlaneSurfaceShear(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(planesurface2),p2r.obj.NurbsSurface)#TODO: Check if it is suppose to return a NurbsSurface
        
    def testPlaneSurfaceTrfm(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.defm.transform(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface) 
        
    def testPlaneSurfaceCopyMove(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.dupl.copy_move()
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)

    def testPlaneSurfaceCopyMoveByVec(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.dupl.copy_move_by_vec()
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)

    def testPlaneSurfaceCopyByOffset(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.dupl.copy_by_offset(1)
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceEvaluate(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.eval.evaluate(1)
        self.assertEqual(len(planesurface2),3) 

    def testPlaneSurfaceEvalDeriv(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.eval.evaluate_derivatives(1,1)
        self.assertEqual(type(planesurface2),list)   

    def testPlaneSurfaceEvalFrame(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.eval.evaluate_frame((0,1))
        self.assertEqual(type(planesurface2[0][0]),float)   
    
    def testPlaneSurfaceGroups(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.grps.groups()
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)
        
    def testPlaneSurfaceTopGroup(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.grps.top_group()
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)          

    def testPlaneSurfaceFlip(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.flip()
        self.assertEqual(type(planesurface2),bool)  
        
    def testPlaneSurfaceInsertKnot(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.insert_knot((0,1),0)
        self.assertEqual(type(planesurface2),bool)  

    def testPlaneSurfaceRebuild(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.rebuild()
        self.assertEqual(type(planesurface2),bool)  
        
    def testPlaneSurfaceRemoveKnot(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.remove_knot((0,1),0)
        self.assertEqual(type(planesurface2),bool)  

    def testPlaneSurfaceReverse(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.reverse(1)
        self.assertEqual(type(planesurface2),bool)  

    def testPlaneSurfaceShrinkTrimmed(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.modf.shrink_trimmed()
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIndex(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.mtrl.index()
        self.assertEqual(type(planesurface2),int)       
        
    def testPlaneSurfaceSource(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(planesurface2),int)         
        
    def testPlaneSurfaceAddMesh(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.rndr.add_mesh()
        self.assertEqual(type(planesurface2),bool)   
        
    def testPlaneSurfaceEnable(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.rndr.enable()
        self.assertEqual(type(planesurface2),bool)   
        
    def testPlaneSurfaceHasMesh(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.rndr.has_mesh()
        self.assertEqual(type(planesurface2),bool)   

    def testPlaneSurfaceHide(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.stat.hide()
        self.assertEqual(type(planesurface2),int)  
        
    def testPlaneSurfaceLock(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.stat.lock()
        self.assertEqual(type(planesurface2),int)  
        
    def testPlaneSurfaceIsBrep(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_brep()
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsBrepManifold(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_brep_manifold()
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsParameterOnSrf(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsPointInSrf(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsPointOnSrf(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsPolySurfaceClosed(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_poly_surface_closed()
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsPlaneSurface(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_plane_surface()
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsPolySrf(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_poly_srf()
        self.assertEqual(type(planesurface2),bool)     
        
    def testPlaneSurfaceIsPolySrfPlanar(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_poly_srf_planar()
        self.assertEqual(type(planesurface2),bool)     
        
    def testPlaneSurfaceIsSrfClosed(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_closed(0)
        self.assertEqual(type(planesurface2),bool)   
        
    def testPlaneSurfaceIsSrfPeriodic(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_periodic(0)
        self.assertEqual(type(planesurface2),bool) 
        
    def testPlaneSurfaceIsSrfPlanar(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_planar()
        self.assertEqual(type(planesurface2),bool)  
        
    def testPlaneSurfaceIsSrfRational(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_rational()
        self.assertEqual(type(planesurface2),bool)  
        
    def testPlaneSurfaceIsSrfSingular(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_singular(0)
        self.assertEqual(type(planesurface2),bool)  
        
    def testPlaneSurfaceIsSrfTrimmed(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.test.is_srf_trimmed()
        self.assertEqual(type(planesurface2),bool)

    def testPlaneSurfaceMirror(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceMove(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceMoveByVec(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceOrient(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        planesurface2 = planesurface1.trfm.orient(pl1,pl2)
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceRemap(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceRotate(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)  
        
    def testPlaneSurfaceScale(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(planesurface2),p2r.obj.PlaneSurface)     
        
    def testPlaneSurfaceDescription(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.util.description()
        self.assertEqual(type(planesurface2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testPlaneSurfaceDump(self):
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        planesurface2 = planesurface1.util.dump()  
        self.assertEqual(type(planesurface2),unicode) #TODO:double check if unicode is the correct return type
if __name__ == '__main__':
    unittest.main()    