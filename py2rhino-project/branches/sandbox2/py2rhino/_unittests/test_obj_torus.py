import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testTorusBoxMorph(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(torus2),p2r.obj.Torus)
        
    def testTorusShear(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(torus2),p2r.obj.Torus)
        
    def testTorusTrfm(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(torus2),p2r.obj.Torus)
    
    def testTorusCopyMove(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.dupl.copy_move()
        self.assertEqual(type(torus2),p2r.obj.Torus)
        
    def testTorusCopyMoveByVec(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.dupl.copy_move_by_vec()
        self.assertEqual(type(torus2),p2r.obj.Torus)
        
    def testTorusEvaluate(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.eval.evaluate(1)
        self.assertEqual(len(torus2),3) 

    def testTorusEvalDeriv(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.eval.evaluate_derivatives(1,1)
        self.assertEqual(type(torus2),list)   

    def testTorusEvalFrame(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.eval.evaluate_frame((0,1))
        self.assertEqual(type(torus2)[0],list)   
        
    def testTorusGroups(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.grps.groups()
        self.assertEqual(type(torus2),p2r.obj.Torus)
        
    def testTorusTopGroup(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.grps.top_group()
        self.assertEqual(type(torus2),p2r.obj.Torus) 
        
    def testTorusFlip(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.flip()
        self.assertEqual(type(torus2),bool)  
        
    def testTorusInsertKnot(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.insert_knot((0,1),0)
        self.assertEqual(type(torus2),bool)  

    def testTorusRebuild(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.rebuild()
        self.assertEqual(type(torus2),bool)  
        
    def testTorusRemoveKnot(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.remove_knot((0,1),0)
        self.assertEqual(type(torus2),bool)  

    def testTorusReverse(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.reverse(1)
        self.assertEqual(type(torus2),bool)  

    def testTorusShrinkTrimmed(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.shrink_trimmed()
        self.assertEqual(type(torus2),bool) 

    def testTorusSeam(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.modf.seam(0,1)
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIndex(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.mtrl.index()
        self.assertEqual(type(torus2),int)       
        
    def testTorusSource(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(torus2),int)  
        
    def testTorusDefinition(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.prop.torus_definition()
        self.assertEqual(len(torus2),3) 
        
    def testTorusAddMesh(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.rndr.add_mesh()
        self.assertEqual(type(torus2),bool)   
        
    def testTorusEnable(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.rndr.enable()
        self.assertEqual(type(torus2),bool)   
        
    def testTorusHasMesh(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.rndr.has_mesh()
        self.assertEqual(type(torus2),bool)   
            
    def testTorusHide(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.stat.hide()
        self.assertEqual(type(torus2),int)  
        
    def testTorusLock(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.stat.lock()
        self.assertEqual(type(torus2),int)  
        
    def testTorusMatchObjectAttributes(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = p2r.obj.Torus.create((0,0,0), 5, 3)
        match = torus1.stat.match_object_attributes(torus2)
        self.assertEqual(type(match),int)  
        
    def testTorusResetObjectAttributes(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        reset = torus1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testTorusMoveToLayoutSpace(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        reset = torus1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testTorusSelect(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        sel = torus1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testTorusShow(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        sel = torus1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testTorusUnlock(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.stat.unlock()
        self.assertEqual(type(torus2),int) 
        
    def testTorusUnselect(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        sel = torus1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testTorusIsBrep(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_brep()
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsBrepManifold(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_brep_manifold()
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsParameterOnSrf(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsPointInSrf(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsPointOnSrf(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsPolySurfaceClosed(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_poly_surface_closed()
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsTorus(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_plane_surface()
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsPolySrf(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_poly_srf()
        self.assertEqual(type(torus2),bool)     
        
    def testTorusIsPolySrfPlanar(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_poly_srf_planar()
        self.assertEqual(type(torus2),bool)     
        
    def testTorusIsSrfClosed(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_closed(0)
        self.assertEqual(type(torus2),bool)   
        
    def testTorusIsSrfPeriodic(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_periodic(0)
        self.assertEqual(type(torus2),bool) 
        
    def testTorusIsSrfPlanar(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_planar()
        self.assertEqual(type(torus2),bool)  
        
    def testTorusIsSrfRational(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_rational()
        self.assertEqual(type(torus2),bool)  
        
    def testTorusIsSrfSingular(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_singular(0)
        self.assertEqual(type(torus2),bool)  
        
    def testTorusIsSrfTrimmed(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.test.is_srf_trimmed()
        self.assertEqual(type(torus2),bool)

    def testTorusMirror(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusMove(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusMoveByVec(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusOrient(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        torus2 = torus1.trfm.orient(pl1,pl2)
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusRemap(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        torus2 = torus1.trfm.remap(pl1, pl2)
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusRotate(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(torus2),p2r.obj.Torus)  
        
    def testTorusScale(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(torus2),p2r.obj.Torus)     
        
    def testTorusDescription(self):
        torus1 = p2r.obj.Torus.create((0,0,0), 5, 3)
        torus2 = torus1.util.description()
        self.assertEqual(type(torus2),unicode)    
if __name__ == '__main__':
    unittest.main()