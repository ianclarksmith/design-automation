import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testConeBoxMorph(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(cone2),p2r.obj.NurbsSurface) #TODO: Check if it is suppose to return a NurbsSurface
        
    def testConeShear(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(cone2),p2r.obj.NurbsSurface)
        
    def testConeTrfm(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(cone2),p2r.obj.NurbsSurface)
        
    def testConeCopyMove(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.dupl.copy_move()
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeCopyMoveByVec(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.dupl.copy_move_by_vec()
        self.assertEqual(type(cone2),p2r.obj.Cone)
        
    def testConeEvaluate(self):
        cone1 = p2r.obj.Cone.create((0,0,0),(1,1,1), 5)
        cone2 = cone1.eval.evaluate(1)
        self.assertEqual(len(cone2),3) 
        
    def testConeEvalFrame(self):
        cone1 = p2r.obj.Cone.create((0,0,0),(1,1,1), 5)
        cone2 = cone1.eval.evaluate_frame((0,1))
        self.assertEqual(type(cone2),list)  
        
    def testConeGroups(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        grp = p2r.ent.Group.create()
        grp2 = grp.objs.add_object(cone1)
        cone2 = cone1.grps.groups()
        self.assertEqual(type(cone2[0]),unicode)
        
    def testConeTopGroup(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        grp = p2r.ent.Group.create()
        grp2 = grp.objs.add_object(cone1)
        cone2 = cone1.grps.top_group()
        self.assertEqual(type(cone2),unicode)  

    def testConeFlip(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.flip()
        self.assertEqual(type(cone2),bool)  
        
    def testConeInsertKnot(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.insert_knot((0,1),0)
        self.assertEqual(type(cone2),bool)  

    def testConeRebuild(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.rebuild()
        self.assertEqual(type(cone2),bool)  
        
    def testConeRemoveKnot(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.remove_knot((0,1),0)
        self.assertEqual(type(cone2),bool)  

    def testConeReverse(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.reverse(1)
        self.assertEqual(type(cone2),bool)  

    def testConeShrinkTrimmed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.modf.shrink_trimmed()
        self.assertEqual(type(cone2),bool) 

    def testConeDefinition(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.prop.cone_def()
        self.assertEqual(len(cone2),3) 
        
    def testConeAddMesh(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.add_mesh()
        self.assertEqual(type(cone2),bool)   
        
    def testConeEnable(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.enable()
        self.assertEqual(type(cone2),bool)   
        
    def testConeHasMesh(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.has_mesh()
        self.assertEqual(type(cone2),bool)   
                
    def testConeHide(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.hide()
        self.assertEqual(type(cone2),int)  
        
    def testConeLock(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.lock()
        self.assertEqual(type(cone2),int)  
        
    def testConeMatchObjectAttributes(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        match = cone1.stat.match_object_attributes(cone2)
        self.assertEqual(type(match),int)  
        
    def testConeResetObjectAttributes(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        reset = cone1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testConeMoveToLayoutSpace(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        reset = cone1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testConeSelect(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testConeShow(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testConeUnlock(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.stat.unlock()
        self.assertEqual(type(cone2),int) 
        
    def testConeUnselect(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        sel = cone1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testConeIsBrep(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_brep()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsBrepManifold(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_brep_manifold()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsParameterOnSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPointInSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPointOnSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPolySurfaceClosed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_surface_closed()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPlaneSurface(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_plane_surface()
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsPolySrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_srf()
        self.assertEqual(type(cone2),bool)     
        
    def testConeIsPolySrfPlanar(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_poly_srf_planar()
        self.assertEqual(type(cone2),bool)     
        
    def testConeIsSrfClosed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_closed(0)
        self.assertEqual(type(cone2),bool)   
        
    def testConeIsSrfPeriodic(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_periodic(0)
        self.assertEqual(type(cone2),bool) 
        
    def testConeIsSrfPlanar(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_planar()
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfRational(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_rational()
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfSingular(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_singular(0)
        self.assertEqual(type(cone2),bool)  
        
    def testConeIsSrfTrimmed(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.test.is_srf_trimmed()
        self.assertEqual(type(cone2),bool)

    def testConeMirror(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeMove(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeMoveByVec(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeOrient(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        cone2 = cone1.trfm.orient(pl1,pl2)
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeRemap(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeRotate(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(cone2),p2r.obj.Cone)  
        
    def testConeScale(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(cone2),p2r.obj.Cone)     
        
    def testConeDescription(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.util.description()
        self.assertEqual(type(cone2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testConeDump(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.util.dump()  
        self.assertEqual(type(cone2),unicode) #TODO:double check if unicode is the correct return type

if __name__ == '__main__':
    unittest.main()