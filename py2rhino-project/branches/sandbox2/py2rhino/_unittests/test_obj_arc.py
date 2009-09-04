import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testArcBoxMorph(self):
        sph1 = p2r.obj.Sphere.create((0,0,0), 5)
        sph2 = sph1.defm.box_morph(((0,0,0),(10,0,0),(10,10,0),(0,10,0),(0,0,10),(10,0,10),(10,10,5),(0,10,5)))
        self.assertEqual(type(sph2),p2r.obj.NurbsSurface)
        
    def testArcShear(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(arc2),p2r.obj.NurbsCurve)
        
    def testArcTansform(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.defm.transform(((0,0,0,0),(0,1,0,0),(0,2,0,0),(0,3,0,0)))
        self.assertEqual(type(arc2),p2r.obj.NurbsSurface)
        
    def testArcCopySub(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_sub(0,1)
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyMove(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_move()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyMoveByVec(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_move_by_vec()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyByOffset(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcCopyBySplit(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(arc2[0]),p2r.obj.Arc)
        
    def testArcCopyByTrim(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)        
    
    def testArcCurvature(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.curvature(1)
        self.assertEqual(len(arc2),5)      
    
    def testArcEvalDeriv(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.derivatives(1,1)
        self.assertEqual(len(arc2),2)   
    
    def testArcFrame(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.frame(1)
        self.assertEqual(len(arc2),4) 
    
    def testArcPerpFrame(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.frame(1)
        self.assertEqual(len(arc2),4) 
    
    def testArcTangent(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.tangent(1)
        self.assertEqual(len(arc2),3) 
    
    def testArcEvaluate(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.eval.evaluate(1)
        self.assertEqual(len(arc2),3) 
    
    def testArcClosed(self):
        points = ( (0,0,0), (10,0,0,), (10,10,0),(0,0.5,0))
        nc1 = p2r.obj.NurbsCurve.create_by_pnts(points, 3)
        nc2 = nc1.func.close()
        self.assertEqual(type(nc2),p2r.obj.bool)
    
    def testArcExtend(self):
        ln1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        ln2 = p2r.obj.Line.create((20,-10,0), (20,20,0))
        ln3 = ln1.func.extend(1,1,ln2)
        self.assertEqual(type(ln3),p2r.obj.Line)
    
    def testArcExtendLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.extend_length(2,2,3)
        #print arc2
        self.assertEqual(type(arc2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testArcExtendPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.func.extend_pnt(1,(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testArcGroups(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.grps.groups()
        self.assertEqual(type(arc2),p2r.obj.Arc)
        
    def testArcTopGroup(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.grps.top_group()
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcIndex(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.mtrl.index()
        self.assertEqual(type(arc2),int)       
        
    def testArcSource(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(arc2),int)   
    
    def testArcFair(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.fair()
        self.assertEqual(type(arc2),bool)  
        
    def testArcInsertKnot(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.insert_knot(0.2)
        self.assertEqual(type(arc2),bool)  

    def testArcRebuild(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.rebuild()
        self.assertEqual(type(arc2),bool)  
        
    def testArcRemoveKnot(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.remove_knot(0.8)
        self.assertEqual(type(arc2),bool)  

    def testArcReverse(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.reverse()
        self.assertEqual(type(arc2),bool)  

    def testArcSimplify(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = arc1.modf.simplify()
        self.assertEqual(type(arc2),bool)   
            
    def testArcAngle(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        ang = arc1.prop.angle()
        self.assertEqual(type(ang),float)   
        
    def testArcCenterPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.prop.center_pnt()
        self.assertEqual(len(arc2),3)   
        
    def testArcMidPnt(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.prop.mid_pnt()
        self.assertEqual(len(arc2),3)   
        
    def testArcRadius(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        radius = arc1.prop.radius()
        self.assertEqual(type(radius),float)   
        
    def testArcAddMesh(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.add_mesh()
        self.assertEqual(type(arc2),bool)     
        
    def testArcHasMesh(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.has_mesh()
        self.assertEqual(type(arc2),bool)   
            
    def testArcHide(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.hide()
        self.assertEqual(type(arc2),int)  
        
    def testArcLock(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.lock()
        self.assertEqual(type(arc2),int)  
        
    def testArcMatchObjectAttributes(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = arc1.stat.match_object_attributes(arc2)
        self.assertEqual(type(match),int)  
        
    def testArcResetObjectAttributes(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        reset = arc1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testArcMoveToLayoutSpace(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        reset = arc1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testArcSelect(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testArcShow(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testArcUnlock(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.stat.unlock()
        self.assertEqual(type(arc2),int) 
        
    def testArcUnselect(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        sel = arc1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testArcIsClosable(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        closable = arc1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testArcIsClosed(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        closed = arc1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testArcInPlane(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        plane = arc1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testArcIsLinear(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        linear = arc1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testArcIsPeriodic(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        periodic = arc1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testArcIsPlanar(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        planar = arc1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testArcIsRational(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        rational = arc1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testArcIsPntOnCrv(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        on_crv = arc1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testArcMirror(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcMove(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcMoveByVec(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcOrient(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        arc2 = arc1.trfm.orient(pl1,pl2)
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcRemap(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcRotate(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(arc2),p2r.obj.Arc)  
        
    def testArcScale(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(arc2),p2r.obj.Arc)     
        
    def testArcDescription(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.util.description()
        self.assertEqual(type(arc2),unicode)   
        
    def testArcDump(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.util.dump()
        self.assertEqual(type(arc2),unicode) 
        
if __name__ == '__main__':
    unittest.main()