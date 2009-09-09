import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testEllipseBoxMorph(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseShear(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(ellipse2),p2r.obj.NurbsCurve) #TODO: Check if it is suppose to return a NurbsCurve
        
    def testEllipseTrfm(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.defm.transform(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)   
        
    def testEllipseCopySub(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyMove(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_move()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyMoveByVec(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_move_by_vec()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyByOffset(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseCopyBySplit(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(ellipse2[0]),p2r.obj.EllipticalArc) 
        
    def testEllipseCopyByTrim(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(ellipse2),p2r.obj.EllipticalArc)  
        
    def testEllipseCurvature(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.curvature(1)
        self.assertEqual(len(ellipse2),5)      
    
    def testEllipseEvalDeriv(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.derivatives(1,1)
        self.assertEqual(len(ellipse2),2)   
    
    def testEllipseFrame(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.frame(1)
        self.assertEqual(len(ellipse2),4) 
    
    def testEllipsePerpFrame(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.frame(1)
        self.assertEqual(len(ellipse2),4) 
    
    def testEllipseTangent(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.tangent(1)
        self.assertEqual(len(ellipse2),3) 
    
    def testEllipseEvaluate(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.eval.evaluate(1)
        self.assertEqual(len(ellipse2),3) 

    def testEllipseArea(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        area = ellipse1.func.area(circle1)
        self.assertEqual(type(area),tuple) 
    
    def testEllipseAreaCentroid(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        areac = ellipse1.func.area_centroid(circle1)
        self.assertEqual(type(areac),tuple) 
    
    def testEllipseBooleanDifference(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        diff = ellipse1.func.boolean_difference(circle1)
        self.assertEqual(type(diff),list) 
    
    def testEllipseBooleanIntersection(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        intersn = ellipse1.func.boolean_intersection(circle1)
        self.assertEqual(type(intersn),list) 
    
    def testEllipseBooleanUnion(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        circle1 = p2r.obj.Circle.create((0,0,0), 25)
        union = circle1.func.boolean_union((ellipse1,ellipse2))
        self.assertEqual(type(union),list) 
    
    def testEllipseContainment(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        cmt = ellipse1.func.containment(ellipse2)
        self.assertEqual(type(cmt),int) 
    
    def testEllipsePointInside(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        pnt = ellipse1.func.pnt_inside((0,0,0))
        self.assertEqual(type(pnt),int) 

    def testEllipseGroups(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.grps.groups()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)
        
    def testEllipseTopGroup(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.grps.top_group()
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)         
        
    def testEllipseInsertKnot(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.insert_knot((0,1),0)
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseRebuild(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.rebuild()
        self.assertEqual(type(ellipse2),bool)  
        
    def testEllipseRemoveKnot(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.remove_knot(0)
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseReverse(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.reverse()
        self.assertEqual(type(ellipse2),bool)  

    def testEllipseSeam(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.modf.seam(0)
        self.assertEqual(type(ellipse2),bool) 

    def testEllipseIndex(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.mtrl.index()
        self.assertEqual(type(ellipse2),int) 
        
    def testEllipseSource(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.mtrl.source()
        self.assertEqual(type(ellipse2),int)

    def testEllipseCenterPoint(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.prop.center_pnt()
        self.assertEqual(type(ellipse2[0]),float)

    def testEllipseQuadPoints(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.prop.quad_pnts()
        self.assertEqual(type(ellipse2),tuple)
        
    def testEllipseAddMesh(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.add_mesh()
        self.assertEqual(type(ellipse2),bool)   
        
    def testEllipseEnable(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.enable()
        self.assertEqual(type(ellipse2),bool)   
        
    def testEllipseHasMesh(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.rndr.has_mesh()
        self.assertEqual(type(ellipse2),bool)   
            
    def testEllipseHide(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.hide()
        self.assertEqual(type(ellipse2),int)  
        
    def testEllipseLock(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.lock()
        self.assertEqual(type(ellipse2),int)  
        
    def testEllipseMatchObjectAttributes(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = p2r.obj.Ellipse.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = ellipse1.stat.match_object_attributes(ellipse2)
        self.assertEqual(type(match),int)  
        
    def testEllipseResetObjectAttributes(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        reset = ellipse1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testEllipseMoveToLayoutSpace(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        reset = ellipse1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testEllipseSelect(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testEllipseShow(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testEllipseUnlock(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.stat.unlock()
        self.assertEqual(type(ellipse2),int) 
        
    def testEllipseUnselect(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        sel = ellipse1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testEllipseIsClosable(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        closable = ellipse1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testEllipseIsClosed(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        closed = ellipse1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testEllipseInPlane(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        plane = ellipse1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testEllipseIsLinear(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        linear = ellipse1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testEllipseIsPeriodic(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        periodic = ellipse1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testEllipseIsPlanar(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        planar = ellipse1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testEllipseIsRational(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        rational = ellipse1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testEllipseIsPntOnCrv(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        on_crv = ellipse1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testEllipseMirror(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseMove(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseMoveByVec(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseOrient(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        ellipse2 = ellipse1.trfm.orient(pl1,pl2)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseRemap(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseRotate(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)  
        
    def testEllipseScale(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(ellipse2),p2r.obj.Ellipse)     
        
    def testEllipseDescription(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.util.description()
        self.assertEqual(type(ellipse2),unicode)   
        
    def testEllipseDump(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        ellipse2 = ellipse1.util.dump()
        self.assertEqual(type(ellipse2),unicode) 
        
if __name__ == '__main__':
    unittest.main()