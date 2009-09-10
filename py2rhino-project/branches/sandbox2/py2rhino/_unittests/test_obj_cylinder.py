import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testCylinderBoxMorph(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(cylinder2),p2r.obj.NurbsSurface)# TODO: check if it is suppose to return a NurbsSurface
        
    def testCylinderShear(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(cylinder2),p2r.obj.NurbsSurface)# TODO: check if it is suppose to return a NurbsSurface
        
    def testCylinderTrfm(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.defm.transform(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)    
        
    def testCylinderCopyMove(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.dupl.copy_move()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderCopyMoveByVec(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.dupl.copy_move_by_vec()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderEvaluate(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.eval.evaluate(1)
        self.assertEqual(len(cylinder2),3) 

    def testCylinderEvalFrame(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.eval.evaluate_frame((0,1))
        self.assertEqual(type(cylinder2),list)      
        
    def testCylinderGroups(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.grps.groups()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)
        
    def testCylinderTopGroup(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.grps.top_group()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  

    def testCylinderIndex(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.mtrl.index()
        self.assertEqual(type(cylinder2),int)  

    def testCylinderSource(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.mtrl.source()
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  

    def testCylinderFlip(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.flip()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderInsertKnot(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.insert_knot((0,1),0)
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderRebuild(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.rebuild()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderRemoveKnot(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.remove_knot((0,1),0)
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderReverse(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.reverse(1)
        self.assertEqual(type(cylinder2),bool)  

    def testCylinderShrinkTrimmed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.modf.shrink_trimmed()
        self.assertEqual(type(cylinder2),bool) 

    def testCylinderDefinition(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.prop.cylinder_def()
        self.assertEqual(len(cylinder2),3) 
        
    def testCylinderAddMesh(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.add_mesh()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderEnable(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.enable()
        self.assertEqual(type(cylinder2),bool)   
        
    def testCylinderHasMesh(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.rndr.has_mesh()
        self.assertEqual(type(cylinder2),bool)    
    def testCylinderHide(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.hide()
        self.assertEqual(type(cylinder2),int)  
        
    def testCylinderLock(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.lock()
        self.assertEqual(type(cylinder2),int)  
        
    def testCylinderMatchObjectAttributes(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = p2r.obj.Cylinder.create((0,0,0), (1,1,1), 5)
        match = cylinder1.stat.match_object_attributes(cylinder2)
        self.assertEqual(type(match),int)  
        
    def testCylinderResetObjectAttributes(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        reset = cylinder1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testCylinderMoveToLayoutSpace(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        reset = cylinder1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testCylinderSelect(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testCylinderShow(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testCylinderUnlock(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.stat.unlock()
        self.assertEqual(type(cylinder2),int) 
        
    def testCylinderUnselect(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        sel = cylinder1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testCylinderIsBrep(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_brep()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsBrepManifold(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_brep_manifold()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsParameterOnSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPointInSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPointOnSrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPolySurfaceClosed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_surface_closed()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPlaneSurface(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_plane_surface()
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsPolySrf(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_srf()
        self.assertEqual(type(cylinder2),bool)     
        
    def testCylinderIsPolySrfPlanar(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_poly_srf_planar()
        self.assertEqual(type(cylinder2),bool)     
        
    def testCylinderIsSrfClosed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_closed(0)
        self.assertEqual(type(cylinder2),bool)   
        
    def testCylinderIsSrfPeriodic(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_periodic(0)
        self.assertEqual(type(cylinder2),bool) 
        
    def testCylinderIsSrfPlanar(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_planar()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfRational(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_rational()
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfSingular(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_singular(0)
        self.assertEqual(type(cylinder2),bool)  
        
    def testCylinderIsSrfTrimmed(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.test.is_srf_trimmed()
        self.assertEqual(type(cylinder2),bool)

    def testCylinderMirror(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderMove(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderMoveByVec(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderOrient(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        cylinder2 = cylinder1.trfm.orient(pl1,pl2)
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderRemap(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderRotate(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)  
        
    def testCylinderScale(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(cylinder2),p2r.obj.Cylinder)     
        
    def testCylinderDescription(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.util.description()
        self.assertEqual(type(cylinder2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testCylinderDump(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),(1,1,1), 5)
        cylinder2 = cylinder1.util.dump()  
        self.assertEqual(type(cylinder2),unicode) #TODO:double check if unicode is the correct return type
if __name__ == '__main__':
    unittest.main()