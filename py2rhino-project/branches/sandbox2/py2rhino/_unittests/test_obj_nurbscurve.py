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
        nurbscurve2 = nurbscurve1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
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
        nurbscurve2 = nurbscurve1.eval.derivatives(1,1)
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
    
    def testNurbsCurveGroups(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        grp = p2r.ent.Group.create()
        grp2 = grp.objs.add_object(nurbscurve1)
        nurbscurve2 = nurbscurve1.grps.groups()
        self.assertEqual(type(nurbscurve2[0]),unicode)
        
    def testNurbsCurveTopGroup(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        grp = p2r.ent.Group.create()
        grp2 = grp.objs.add_object(nurbscurve1)
        nurbscurve2 = nurbscurve1.grps.groups()
        nurbscurve2 = nurbscurve1.grps.top_group()
        self.assertEqual(type(nurbscurve2),unicode)  
        
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
        nurbscurve2 = nurbscurve1.modf.remove_knot(0)
        self.assertEqual(type(nurbscurve2),bool)  

    def testNurbsCurveReverse(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.reverse()
        self.assertEqual(type(nurbscurve2),bool)  

    def testNurbsCurveSimplify(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.modf.simplify()
        self.assertEqual(type(nurbscurve2),bool)    
        
    def testNurbsCurveDegree(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.degree()
        self.assertEqual(type(nurbscurve2),int)     
            
    def testNurbsCurveDim(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.dim()
        self.assertEqual(type(nurbscurve2),int) 
    
    def testNurbsCurveDomain(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.domain()
        self.assertEqual(type(nurbscurve2[0]),float)       

    def testNurbsCurveDiscontinuity(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.discontinuity(1)
        self.assertEqual(type(nurbscurve2),int)   
        
    def testNurbsCurveEditPnts(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.edit_pnts()
        self.assertEqual(type(nurbscurve2[0][0]),float)  

    def testNurbsCurveEndPnts(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.end_pnt()
        self.assertEqual(type(nurbscurve2[0]),float)       
                       
    def testNurbsCurveKnotCount(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.knot_count()
        self.assertEqual(type(nurbscurve2),int) 
                          
    def testNurbsCurveKnots(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.knots()
        self.assertEqual(type(nurbscurve2[0]),float)  

    def testNurbsCurveLength(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.length()
        self.assertEqual(type(nurbscurve2),float) 
         
    def testNurbsCurveMidPnts(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.mid_pnt()
        self.assertEqual(type(nurbscurve2[0]),float)  
               
    def testNurbsCurveNormal(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.normal()
        self.assertEqual(type(nurbscurve2[0]),float)        
        
    def testNurbsCurvePlane(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.plane()
        self.assertEqual(type(nurbscurve2[0][0]),float)          
        
    def testNurbsCurveControlPntCount(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.control_pnt_count()
        self.assertEqual(type(nurbscurve2),int) 
        
    def testNurbsCurveControlPnts(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.control_pnts()
        self.assertEqual(type(nurbscurve2[0][0]),float)  

    def testNurbsCurveStartPnt(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.start_pnt()
        self.assertEqual(type(nurbscurve2[0]),float)  
                          
    def testNurbsCurveWeights(self):
        nurbscurve1 = p2r.obj.NurbsCurve.create_by_pnts(((0,0,0),(1,0,0),(5,0,0)))
        nurbscurve2 = nurbscurve1.prop.weights()
        self.assertEqual(type(nurbscurve2[0]),float)  
        
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
        nurbscurve2 = nurbscurve1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
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