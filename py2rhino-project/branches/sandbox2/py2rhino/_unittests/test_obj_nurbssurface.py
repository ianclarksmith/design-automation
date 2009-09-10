import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testNurbsSurfaceBoxMorph(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)
        
    def testNurbsSurfaceShear(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)
        
    def testNurbsSurfaceTrfm(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface) 
        
    def testNurbsSurfaceCopyMove(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.dupl.copy_move()
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)
        
    def testNurbsSurfaceCopyMoveByVec(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.dupl.copy_move_by_vec()
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)
        
    def testNurbsSurfaceCopyByOffset(self):
        nurbssurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.dupl.copy_by_offset(1)
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)     
        
    def testNurbsSurfaceGroups(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.grps.groups()
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)
        
    def testNurbsSurfaceTopGroup(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.grps.top_group()
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
    
    def testNurbsSurfaceFlip(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.flip()
        self.assertEqual(type(nurbssurface2),bool)  
        
    def testNurbsSurfaceInsertKnot(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.insert_knot((0,1),0)
        self.assertEqual(type(nurbssurface2),bool)  

    def testNurbsSurfaceRebuild(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.rebuild()
        self.assertEqual(type(nurbssurface2),bool)  
        
    def testNurbsSurfaceRemoveKnot(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.remove_knot((0,1),0)
        self.assertEqual(type(nurbssurface2),bool)  

    def testNurbsSurfaceReverse(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.reverse(1)
        self.assertEqual(type(nurbssurface2),bool)  

    def testNurbsSurfaceShrinkTrimmed(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.modf.shrink_trimmed()
        self.assertEqual(type(nurbssurface2),bool) 
    
    def testNurbsSurfaceAddMesh(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.rndr.add_mesh()
        self.assertEqual(type(nurbssurface2),bool)   
        
    def testNurbsSurfaceEnable(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.rndr.enable()
        self.assertEqual(type(nurbssurface2),bool)   
        
    def testNurbsSurfaceHasMesh(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.rndr.has_mesh()
        self.assertEqual(type(nurbssurface2),bool)   
                
    def testNurbsSurfaceHide(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.stat.hide()
        self.assertEqual(type(nurbssurface2),int)  
        
    def testNurbsSurfaceLock(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.stat.lock()
        self.assertEqual(type(nurbssurface2),int)  
        
    def testNurbsSurfaceMatchObjectAttributes(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        match = nurbssurface1.stat.match_object_attributes(nurbssurface2)
        self.assertEqual(type(match),int)  
        
    def testNurbsSurfaceResetObjectAttributes(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        reset = nurbssurface1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testNurbsSurfaceMoveToLayoutSpace(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        reset = nurbssurface1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testNurbsSurfaceSelect(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        sel = nurbssurface1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testNurbsSurfaceShow(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        sel = nurbssurface1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testNurbsSurfaceUnlock(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.stat.unlock()
        self.assertEqual(type(nurbssurface2),int) 
        
    def testNurbsSurfaceUnselect(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        sel = nurbssurface1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testNurbsSurfaceIsBrep(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_brep()
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsBrepManifold(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_brep_manifold()
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsParameterOnSrf(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_parameter_on_srf((0,0))
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsPointInSrf(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_pnt_in_srf((0,0,0))
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsPointOnSrf(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_pnt_on_srf((0,0,0))
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsPolySurfaceClosed(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_poly_surface_closed()
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsPlaneSurface(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_plane_surface()
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsPolySrf(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_poly_srf()
        self.assertEqual(type(nurbssurface2),bool)     
        
    def testNurbsSurfaceIsPolySrfPlanar(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_poly_srf_planar()
        self.assertEqual(type(nurbssurface2),bool)     
        
    def testNurbsSurfaceIsSrfClosed(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_closed(0)
        self.assertEqual(type(nurbssurface2),bool)   
        
    def testNurbsSurfaceIsSrfPeriodic(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_periodic(0)
        self.assertEqual(type(nurbssurface2),bool) 
        
    def testNurbsSurfaceIsSrfPlanar(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_planar()
        self.assertEqual(type(nurbssurface2),bool)  
        
    def testNurbsSurfaceIsSrfRational(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_rational()
        self.assertEqual(type(nurbssurface2),bool)  
        
    def testNurbsSurfaceIsSrfSingular(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_singular(0)
        self.assertEqual(type(nurbssurface2),bool)  
        
    def testNurbsSurfaceIsSrfTrimmed(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.test.is_srf_trimmed()
        self.assertEqual(type(nurbssurface2),bool)

    def testNurbsSurfaceMirror(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceMove(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceMoveByVec(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceOrient(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        nurbssurface2 = nurbssurface1.trfm.orient(pl1,pl2)
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceRemap(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceRotate(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)  
        
    def testNurbsSurfaceScale(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(nurbssurface2),p2r.obj.NurbsSurface)     
        
    def testNurbsSurfaceDescription(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.util.description()
        self.assertEqual(type(nurbssurface2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testNurbsSurfaceDump(self):
        nurbssurface1= p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        nurbssurface2 = nurbssurface1.util.dump()  
        self.assertEqual(type(nurbssurface2),unicode) #TODO:double check if unicode is the correct return type
if __name__ == '__main__':
    unittest.main()