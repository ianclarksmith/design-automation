import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testLineBoxMorph(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineShear(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineTrfm(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.defm.trfm(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(line2),p2r.obj.Line) 
    
    def testLineCopySub(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineCopyMove(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_move()
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineCopyMoveByVec(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_move_by_vec()
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineCopyByOffset(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_by_offset((0,0,0),1)
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineCopyBySplit(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(line2[0]),p2r.obj.Line)
        
    def testLineCopyByTrim(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineCurvature(self):
        line1 = p2r.obj.Line.create((0,0,0),  (10,10,0))
        line2 = line1.eval.curvature(1)
        self.assertEqual(len(line2),5)      
    
    def testLineEvalDeriv(self):
        line1 = p2r.obj.Line.create((0,0,0), (10,10,0))
        line2 = line1.eval.evaluate_derivatives(1,1)
        self.assertEqual(len(line2),2)   
    
    def testLineFrame(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.eval.frame(1)
        self.assertEqual(len(line2),4) 
    
    def testLinePerpFrame(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.eval.frame(1)
        self.assertEqual(len(line2),4) 
    
    def testLineTangent(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.eval.tangent(1)
        self.assertEqual(len(line2),3) 
    
    def testLineEvaluate(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.eval.evaluate(1)
        self.assertEqual(len(line2),3) 
    
    def testLineClosed(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.close()
        self.assertEqual(type(line2),p2r.obj.Line)
    
    def testLineExtend(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create((0,0,0), 5, 45)
        line3 = line1.func.extend(1,1,line2)
        self.assertEqual(type(line3),p2r.obj.Line)
    
    def testLineExtendLength(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.extend_length(2,2,3)
        #print line2
        self.assertEqual(type(line2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testLineExtendPnt(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.func.extend_pnt(1,(1,1,1))
        self.assertEqual(type(line2),p2r.obj.NurbsCurve) #TODO: to check if it is suppose to return as a nurbscurve
        
    def testLineGroups(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.grps.groups()
        self.assertEqual(type(line2),p2r.obj.Line)
        
    def testLineTopGroup(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.grps.top_group()
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineIndex(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.mtrl.index()
        self.assertEqual(type(line2),int)       
        
    def testLineSource(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.mtrl.source(0)              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(line2),int)   
    
    def testLineFair(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.fair()
        self.assertEqual(type(line2),bool)  
        
    def testLineInsertKnot(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.insert_knot((0,1),0)
        self.assertEqual(type(line2),bool)  

    def testLineRebuild(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.rebuild()
        self.assertEqual(type(line2),bool)  
        
    def testLineRemoveKnot(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.remove_knot((0,1),0)
        self.assertEqual(type(line2),bool)  

    def testLineReverse(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.reverse(1)
        self.assertEqual(type(line2),bool)  

    def testLineSimplify(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.modf.simplify()
        self.assertEqual(type(line2),bool)    
            
    def testLineArrows(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.prop.arrows()
        self.assertEqual(type(line2),int) 
    
        
    def testLineAddMesh(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.add_mesh()
        self.assertEqual(type(line2),bool)   
        
    def testLineEnable(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.enable()
        self.assertEqual(type(line2),bool)   
        
    def testLineHasMesh(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.rndr.has_mesh()
        self.assertEqual(type(line2),bool)   
            
    def testLineHide(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.hide()
        self.assertEqual(type(line2),int)  
        
    def testLineLock(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.lock()
        self.assertEqual(type(line2),int)  
        
    def testLineMatchObjectAttributes(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create((0,0,0), (10,10,0))
        match = line1.stat.match_object_attributes(line2)
        self.assertEqual(type(match),int)  
        
    def testLineResetObjectAttributes(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        reset = line1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testLineMoveToLayoutSpace(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        reset = line1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testLineSelect(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testLineShow(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testLineUnlock(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.stat.unlock()
        self.assertEqual(type(line2),int) 
        
    def testLineUnselect(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        sel = line1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testLineIsClosable(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        closable = line1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testLineIsClosed(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        closed = line1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testLineInPlane(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        plane = line1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testLineIsLinear(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        linear = line1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testLineIsPeriodic(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        periodic = line1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testLineIsPlanar(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        planar = line1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testLineIsRational(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        rational = line1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testLineIsPntOnCrv(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        on_crv = line1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testLineMirror(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineMove(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineMoveByVec(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineOrient(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        line2 = line1.trfm.orient(pl1,pl2)
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineRemap(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineRotate(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(line2),p2r.obj.Line)  
        
    def testLineScale(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(line2),p2r.obj.Line)     
        
    def testLineDescription(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.util.description()
        self.assertEqual(type(line2),unicode)   
        
    def testLineDump(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = line1.util.dump()
        self.assertEqual(type(line2),unicode) 
            
if __name__ == '__main__':
    unittest.main()