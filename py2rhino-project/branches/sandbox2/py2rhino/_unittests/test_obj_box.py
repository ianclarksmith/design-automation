import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testBoxMorph(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxShear(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxCopyMove(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.dupl.copy_move()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxCopyMoveByVec(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.dupl.copy_move_by_vec()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxEvaluate(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.eval.evaluate(1)
        self.assertEqual(len(box2),3) 

    def testBoxEvalFrame(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.eval.evaluate_frame((0,1))
        self.assertEqual(type(box2),list)   
               
    def testBoxGroups(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.grps.groups()
        self.assertEqual(type(box2),p2r.obj.Box)
        
    def testBoxTopGroup(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.grps.top_group()
        self.assertEqual(type(box2),p2r.obj.Box)  

    def testBoxFlip(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.flip()
        self.assertEqual(type(box2),bool)  
        
    def testBoxInsertKnot(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.insert_knot((0,1),0)
        self.assertEqual(type(box2),bool)  

    def testBoxRebuild(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.rebuild()
        self.assertEqual(type(box2),bool)  
        
    def testBoxRemoveKnot(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.remove_knot((0,1),0)
        self.assertEqual(type(box2),bool)  

    def testBoxReverse(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.reverse(1)
        self.assertEqual(type(box2),bool)  

    def testBoxShrinkTrimmed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.shrink_trimmed()
        self.assertEqual(type(box2),bool)  

    def testBoxSeam(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.modf.seam(0,1)
        self.assertEqual(type(box2),bool) 

    def testBoxIndex(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.mtrl.index()
        self.assertEqual(type(box2),int) 
        
    def testBoxSource(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.mtrl.source()
        self.assertEqual(type(box2),int)
        
    def testBoxVolume(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume()
        self.assertEqual(type(box2),tuple)  
        
    def testBoxVolumeCentroid(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume_centroid()
        self.assertEqual(type(box2),tuple) 
        
    def testBoxVolumeMoments(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.prop.volume_moments()
        self.assertEqual(type(box2),tuple) 
        
    def testBoxAddMesh(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.add_mesh()
        self.assertEqual(type(box2),bool)   
        
    def testBoxEnable(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.enable()
        self.assertEqual(type(box2),bool)   
        
    def testBoxHasMesh(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.has_mesh()
        self.assertEqual(type(box2),bool)   
        
    def testBoxHide(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.hide()
        self.assertEqual(type(box2),int)  
        
    def testBoxLock(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.lock()
        self.assertEqual(type(box2),int)  
        
    def testBoxMatchObjectAttributes(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        match = box1.stat.match_object_attributes(box2)
        self.assertEqual(type(match),int)  
        
    def testBoxResetObjectAttributes(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        reset = box1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testBoxMoveToLayoutSpace(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        reset = box1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testBoxSelect(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testBoxShow(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testBoxUnlock(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.stat.unlock()
        self.assertEqual(type(box2),int) 
        
    def testBoxUnselect(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        sel = box1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testBoxIsBrep(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_brep()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsBrepManifold(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_brep_manifold()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsParameterOnSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPointInSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPointOnSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPolySurfaceClosed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_surface_closed()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPlaneSurface(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_plane_surface()
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsPolySrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_srf()
        self.assertEqual(type(box2),bool)     
        
    def testBoxIsPolySrfPlanar(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_poly_srf_planar()
        self.assertEqual(type(box2),bool)     
        
    def testBoxIsSrfClosed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_closed(0)
        self.assertEqual(type(box2),bool)   
        
    def testBoxIsSrfPeriodic(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_periodic(0)
        self.assertEqual(type(box2),bool) 
        
    def testBoxIsSrfPlanar(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_planar()
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfRational(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_rational()
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfSingular(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_singular(0)
        self.assertEqual(type(box2),bool)  
        
    def testBoxIsSrfTrimmed(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.test.is_srf_trimmed()
        self.assertEqual(type(box2),bool)

    def testBoxMirror(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxMove(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxMoveByVec(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxOrient(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        box2 = box1.trfm.orient(pl1, pl2)
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxRemap(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxRotate(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(box2),p2r.obj.Box)  
        
    def testBoxScale(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(box2),p2r.obj.Box)     
        
    def testBoxDescription(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.util.description()
        self.assertEqual(type(box2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testBoxDump(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.util.dump()  
        self.assertEqual(type(box2),unicode) #TODO:double check if unicode is the correct return type
if __name__ == '__main__':
    unittest.main()