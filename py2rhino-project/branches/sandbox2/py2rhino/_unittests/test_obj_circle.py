import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testCirclecBoxMorph(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleShear(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(circle2),p2r.obj.NurbsCurve)
        
    def testCircleTrfm(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.defm.transform(((0,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(circle2),p2r.obj.NurbsCurve)

    def testCircleCopySub(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyMove(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_move()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyMoveByVec(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_move_by_vec()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyByOffset(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleCopyBySplit(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(circle2[0]),p2r.obj.Arc) #TODO:double check if arc is the correct return type
        
    def testCircleCopyByTrim(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(circle2),p2r.obj.Arc)  

    def testCircleCurvature(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.curvature(1)
        self.assertEqual(len(circle2),5)      
    
    def testCircleEvalDeriv(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.derivatives(1,1)
        self.assertEqual(len(circle2),2)   
    
    def testCircleFrame(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.frame(1)
        self.assertEqual(len(circle2),4) 
    
    def testCirclePerpFrame(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.frame(1)
        self.assertEqual(len(circle2),4) 
    
    def testCircleTangent(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.tangent(1)
        self.assertEqual(len(circle2),3) 
    
    def testCircleEvaluate(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.eval.evaluate(1)
        self.assertEqual(len(circle2),3) 
    
    def testCircleArea(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create((0,0,0), 25)
        area = circle1.func.area(circle2)
        self.assertEqual(type(area),tuple) 
    
    def testCircleAreaCentroid(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create((0,0,0), 25)
        areac = circle1.func.area_centroid(circle2)
        self.assertEqual(type(areac),tuple) 
    
    def testCircleBooleanDifference(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        diff = circle1.func.boolean_difference(arc1)
        self.assertEqual(type(diff),list) 
    
    def testCircleBooleanIntersection(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        intersn = circle1.func.boolean_intersection(arc1)
        self.assertEqual(type(intersn),list) 
    
    def testCircleBooleanUnion(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        union = circle1.func.boolean_union((arc1,arc2))
        self.assertEqual(type(union),bool) 
    
    def testCircleContainment(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        cmt = circle1.func.containment(circle2)
        self.assertEqual(type(cmt),int) 
    
    def testCirclePointInside(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        pnt = circle1.func.pnt_inside((0,0,0))
        self.assertEqual(type(pnt),int) 
            
    def testCircleGroups(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.grps.groups()
        self.assertEqual(type(circle2),p2r.obj.Circle)
        
    def testCircleTopGroup(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.grps.top_group()
        self.assertEqual(type(circle2),p2r.obj.Circle) 

    def testCircleInsertKnot(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.insert_knot((0,1),0)
        self.assertEqual(type(circle2),bool)  

    def testCircleRebuild(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.rebuild()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleRemoveKnot(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.remove_knot(0)
        self.assertEqual(type(circle2),bool)  

    def testCircleReverse(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.reverse()
        self.assertEqual(type(circle2),bool)  

    def testCircleSeam(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.modf.seam(0)
        self.assertEqual(type(circle2),bool) 

    def testCircleIndex(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.mtrl.index()
        self.assertEqual(type(circle2),int) 
        
    def testCircleSource(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.mtrl.source()
        self.assertEqual(type(circle2),int)
        
    def testCircleCenterPoint(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.center_pnt()
        self.assertEqual(type(circle2),tuple)
        
    def testCircleCircumference(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.circumference()
        self.assertEqual(type(circle2),float)
        
    def testCircleRadius(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.prop.radius()
        self.assertEqual(type(circle2),float)
        
    
    def testCircleAddMesh(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.add_mesh()
        self.assertEqual(type(circle2),bool)   
        
    def testCircleHasMesh(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.has_mesh()
        self.assertEqual(type(circle2),bool)         
        
    def testCircleHide(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.hide()
        self.assertEqual(type(circle2),int)  
        
    def testCircleLock(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.lock()
        self.assertEqual(type(circle2),int)  
        
    def testCircleMatchObjectAttributes(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = p2r.obj.Circle.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        match = circle1.stat.match_object_attributes(circle2)
        self.assertEqual(type(match),int)  
        
    def testCircleResetObjectAttributes(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        reset = circle1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testCircleMoveToLayoutSpace(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        reset = circle1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testCircleSelect(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testCircleShow(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testCircleUnlock(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.stat.unlock()
        self.assertEqual(type(circle2),int) 
        
    def testCircleUnselect(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        sel = circle1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testCircleIsClosable(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        closable = circle1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testCircleIsClosed(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        closed = circle1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testCircleInPlane(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        plane = circle1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testCircleIsLinear(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        linear = circle1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testCircleIsPeriodic(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        periodic = circle1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testCircleIsPlanar(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        planar = circle1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testCircleIsRational(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        rational = circle1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testCircleIsPntOnCrv(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        on_crv = circle1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testCircleMirror(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleMove(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleMoveByVec(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleOrient(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        circle2 = circle1.trfm.orient(pl1,pl2)
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleRemap(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.remap(((0,0,0),(0,1,0),(1,0,0)),((1,1,1),(1,0,1),(0,0,1)))
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleRotate(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(circle2),p2r.obj.Circle)  
        
    def testCircleScale(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(circle2),p2r.obj.Circle)     
        
    def testCircleDescription(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.util.description()
        self.assertEqual(type(circle2),unicode)   #TODO:double check if unicode is the correct return type
        
    def testCircleDump(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.util.dump()
        self.assertEqual(type(circle2),unicode) #TODO:double check if unicode is the correct return type

if __name__ == '__main__':
    unittest.main()