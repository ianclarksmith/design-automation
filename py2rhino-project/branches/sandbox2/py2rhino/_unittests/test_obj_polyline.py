import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testPolylineBoxMorph(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.defm.box_morph(((0,0,0),(0,1,0),(10,0,0),(0,10,0),(0,0,10),(1,0,0),(0,5,5),(5,0,0)))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineShear(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.defm.shear((0,0,0),(10,10,10),45)
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineTrfm(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.defm.transform(((0,0,0),(0,1,0),(0,2,0),(0,3,0),(1,0,0),(1,1,1),(1,2,0),(1,3,0),(2,0,0),(2,1,0),(2,2,1),(2,3,0),(3,0,0),(3,1,0),(3,2,0),(3,3,1)))
        self.assertEqual(type(polyline2),p2r.obj.Polyline) 
        
    def testPolylineCopySub(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_by_sub((0,0,0),(10,0,0))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineCopyMove(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_move()
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineCopyMoveByVec(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_move_by_vec()
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineCopyByOffset(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_by_offset(polyline1,2)
        self.assertEqual(type(polyline2),p2r.obj.Polyline)    

    def testPolylineCopyBySplit(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(polyline2[0]),p2r.obj.Polyline)
        
    def testPolylineCopyByTrim(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineCurvature(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.curvature(1)
        self.assertEqual(len(polyline2),5)      
    
    def testPolylineEvalDeriv(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.derivatives(1,1)
        self.assertEqual(len(polyline2),2)   
    
    def testPolylineFrame(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.frame(1)
        self.assertEqual(len(polyline2),4) 
    
    def testPolylinePerpFrame(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.frame(1)
        self.assertEqual(len(polyline2),4) 
    
    def testPolylineTangent(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.tangent(1)
        self.assertEqual(len(polyline2),3) 
    
    def testPolylineEvaluate(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.eval.evaluate(1)
        self.assertEqual(len(polyline2),3) 
        
    def testPolylineGroups(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.grps.groups()
        self.assertEqual(type(polyline2),p2r.obj.Polyline)
        
    def testPolylineTopGroup(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.grps.top_group()
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  

    def testPolylineSeam(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.seam((0,0,1))
        self.assertEqual(type(polyline2),bool) 

    def testPolylineFair(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.fair()
        self.assertEqual(type(polyline2),bool)  
        
    def testPolylineInsertKnot(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.insert_knot((0,1),0)
        self.assertEqual(type(polyline2),bool)  

    def testPolylineRebuild(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.rebuild()
        self.assertEqual(type(polyline2),bool)  
        
    def testPolylineRemoveKnot(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.remove_knot((0,0,1));
        self.assertEqual(type(polyline2),bool)  

    def testPolylineReverse(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.reverse()
        self.assertEqual(type(polyline2),bool)  

    def testPolylineSimplify(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.modf.simplify()
        self.assertEqual(type(polyline2),bool)  

    def testPolylineIndex(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.mtrl.index()
        self.assertEqual(type(polyline2),int)       
        
    def testPolylineSource(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.mtrl.source(0);              #TODO: if 0 is not provided, none is returned.
        self.assertEqual(type(polyline2),int)   
        
    def testPolylineVertices(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.prop.vertices()
        self.assertEqual(type(polyline2),tuple)     
        
    def testPolylineAddMesh(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.rndr.add_mesh()
        self.assertEqual(type(polyline2),bool)   
        
    def testPolylineEnable(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.rndr.enable()
        self.assertEqual(type(polyline2),bool)   
        
    def testPolylineHasMesh(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.rndr.has_mesh()
        self.assertEqual(type(polyline2),bool)   
            
    def testPolylineHide(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.stat.hide()
        self.assertEqual(type(polyline2),int)  
        
    def testPolylineLock(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.stat.lock()
        self.assertEqual(type(polyline2),int)  
        
    def testPolylineMatchObjectAttributes(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = p2r.obj.Polyline.create(((0,0,0),(10,10,0)))
        match = polyline1.stat.match_object_attributes(polyline2)
        self.assertEqual(type(match),int)  
        
    def testPolylineResetObjectAttributes(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        reset = polyline1.stat.reset_object_attributes()
        self.assertEqual(type(reset),int)  
        
    def testPolylineMoveToLayoutSpace(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        reset = polyline1.stat.move_to_layout_space()
        self.assertEqual(type(reset),str)  
        
    def testPolylineSelect(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        sel = polyline1.stat.select()
        self.assertEqual(type(sel),int)  
        
    def testPolylineShow(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        sel = polyline1.stat.show()
        self.assertEqual(type(sel),int)  
        
    def testPolylineUnlock(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.stat.unlock()
        self.assertEqual(type(polyline2),int) 
        
    def testPolylineUnselect(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        sel = polyline1.stat.unselect()
        self.assertEqual(type(sel),int) 
        
    def testPolylineIsClosable(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        closable = polyline1.test.is_closable()
        self.assertEqual(type(closable),bool) 
        
    def testPolylineIsClosed(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        closed = polyline1.test.is_closed()
        self.assertEqual(type(closed),bool) 
        
    def testPolylineInPlane(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        plane = polyline1.test.in_plane()
        self.assertEqual(type(plane),bool) 
        
    def testPolylineIsPolylinear(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        linear = polyline1.test.is_linear()
        self.assertEqual(type(linear),bool)
        
    def testPolylineIsPeriodic(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        periodic = polyline1.test.is_periodic()
        self.assertEqual(type(periodic),bool)
        
    def testPolylineIsPlanar(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        planar = polyline1.test.is_planar()
        self.assertEqual(type(planar),bool)
        
    def testPolylineIsRational(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        rational = polyline1.test.is_rational()
        self.assertEqual(type(rational),bool)   
        
    def testPolylineIsPntOnCrv(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        on_crv = polyline1.test.is_pnt_on_crv((0,0,0))
        self.assertEqual(type(on_crv),bool)         
        
    def testPolylineMirror(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineMove(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineMoveByVec(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineOrient(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        polyline2 = polyline1.trfm.orient(pl1,pl2)
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineRemap(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineRotate(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(polyline2),p2r.obj.Polyline)  
        
    def testPolylineScale(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(polyline2),p2r.obj.Polyline)     
        
    def testPolylineDescription(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.util.description()
        self.assertEqual(type(polyline2),unicode)   
        
    def testPolylineDump(self):
        polyline1 = p2r.obj.Polyline.create(((0,0,0),(10,0,0)))
        polyline2 = polyline1.util.dump()
        self.assertEqual(type(polyline2),unicode) 
if __name__ == '__main__':
    unittest.main()