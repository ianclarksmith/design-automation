import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):    
    def testNurbsCurveBoxMorph(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveShear(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveTrfm(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve) 
        
    def testNurbsCurveCopySub(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCopyMove(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_move()
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCopyMoveByVec(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_move_by_vec()
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCopyByOffset(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_by_offset(nurbscurve1,2)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)    
            
    def testNurbsCurveCopyByOffsetOnSrf(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve2 = nurbscurve1.dupl.copy_by_offset_on_srf(planesurface1,(1,2))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
            
    def testNurbsCurveCopyByOffsetOnSrfByParam(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        planesurface1 = p2r.obj.PlaneSurface.create(((0,0,0),(0,1,0),(1,0,0)),3,5)
        nurbscurve2 = nurbscurve1.dupl.copy_by_offset_on_srf_by_param(planesurface1,(1,0))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCopyBySplit(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(nurbscurve2[0]),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCopyByTrim(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveCurvature(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.curvature(1)
        self.assertEqual(len(nurbscurve2),5)      
    
    def testNurbsCurveEvalDeriv(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(nurbscurve2),2)   
    
    def testNurbsCurveFrame(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.frame(1)
        self.assertEqual(len(nurbscurve2),4) 
    
    def testNurbsCurvePerpFrame(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.frame(1)
        self.assertEqual(len(nurbscurve2),4) 
    
    def testNurbsCurveTangent(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.tangent(1)
        self.assertEqual(len(nurbscurve2),3) 
    
    def testNurbsCurveEvaluate(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.eval.evaluate(1)
        self.assertEqual(len(nurbscurve2),3) 
        
    def testNurbsCurveClosed(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.func.close()
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
    
    def testNurbsCurveExtend(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = p2r.obj.NurbsCurve.create((0,0,0), 5, 45)
        nurbscurve3 = nurbscurve1.func.extend(1,1,nurbscurve2)
        self.assertEqual(type(nurbscurve3),p2r.obj.NurbsCurve)
    
    def testNurbsCurveExtendLength(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.func.extend_length(2,2,3)
        #print nurbscurve2
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testNurbsCurveExtendPnt(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.func.extend_pnt(1,(1,1,1))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testNurbsCurveGroups(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.grps.groups()
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)
        
    def testNurbsCurveTopGroup(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.grps.top_group()
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveIndex(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.mtrl.index()
        self.assertEqual(type(nurbscurve2),int)       
        
    def testNurbsCurveSource(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(nurbscurve2),int)   
    def testNurbsCurveFair(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.fair()
        self.assertEqual(type(nurbscurve2),bool)  
        
    def testNurbsCurveInsertKnot(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.insert_knot((0,1),0)
        self.assertEqual(type(nurbscurve2),bool)  

    def testNurbsCurveRebuild(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.rebuild()
        self.assertEqual(type(nurbscurve2),bool)  
        
    def testNurbsCurveRemoveKnot(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.remove_knot((0,1),0)
        self.assertEqual(type(nurbscurve2),bool)  

    def testNurbsCurveReverse(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.reverse(1)
        self.assertEqual(type(nurbscurve2),bool)  

    def testNurbsCurveSimplify(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.simplify()
        self.assertEqual(type(nurbscurve2),bool)    
        
    def testNurbsCurveArrows(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.arrows()
        self.assertEqual(type(nurbscurve2),int)     
        
    def testNurbscurveAddMesh(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.rndr.add_mesh()
        self.assertEqual(type(nurbscurve2),bool)   
        
    def testNurbsCurveEnable(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.rndr.enable()
        self.assertEqual(type(nurbscurve2),bool)   
        
    def testNurbsCurveHasMesh(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.rndr.has_mesh()
        self.assertEqual(type(nurbscurve2),bool)   
            
    def testNurbsCurveHide(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.stat.hide()
        self.assertEqual(type(nurbscurve2),int)  
        
    def testNurbsCurveLock(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.stat.lock()
        self.assertEqual(type(nurbscurve2),int)  
        
    def testNurbsCurveMatchObjectAttributes(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = p2r.obj.NurbsCurve.create((0,0,0), (6,0,0), (10,10,0))
        match = nurbscurve1.stat.match_object_attributes(nurbscurve2)
        self.assertEqual(type(match),int)  
        
    def testNurbsCurveResetObjectAttributes(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        reset = nurbscurve1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testNurbsCurveMoveToLayoutSpace(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        reset = nurbscurve1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testNurbsCurveSelect(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        sel = nurbscurve1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testNurbsCurveShow(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        sel = nurbscurve1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testNurbsCurveUnlock(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.stat.unlock()
        self.assertEqual(type(nurbscurve2),int) 
        
    def testNurbsCurveUnselect(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        sel = nurbscurve1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testNurbsCurveIsClosable(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        closable = nurbscurve1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testNurbsCurveIsClosed(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        closed = nurbscurve1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testNurbsCurveInPlane(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        plane = nurbscurve1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testNurbsCurveIsNurbscurvear(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve_linear = nurbscurve1.test.is_linear()
        self.assertEqual(type(nurbscurve_linear),bool)
        
    def testNurbsCurveIsPeriodic(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        periodic = nurbscurve1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testNurbsCurveIsPlanar(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        planar = nurbscurve1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testNurbsCurveIsRational(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        rational = nurbscurve1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testNurbsCurveIsPntOnCrv(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        on_crv = nurbscurve1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testNurbsCurveMirror(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveMove(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveMoveByVec(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveOrient(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        nurbscurve2 = nurbscurve1.trfm.orient(pl1,pl2)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveRemap(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveRotate(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)  
        
    def testNurbsCurveScale(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(nurbscurve2),p2r.obj.NurbsCurve)     
        
    def testNurbsCurveDescription(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.util.description()
        self.assertEqual(type(nurbscurve2),unicode)   
        
    def testNurbsCurveDump(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.util.dump()
        self.assertEqual(type(nurbscurve2),unicode)  
if __name__ == '__main__':
    unittest.main()