import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testCreatePolyCurve(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        self.assertEqual(type(polycurve1),p2r.obj.PolyCurve)
        
    def testPolyCurveCopySub(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_by_sub(0,1)
        self.assertEqual(type(polyCurve2),p2r.obj.PolyCurve)
        
    def testPolyCurveCopyMove(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_move()
        self.assertEqual(type(polyCurve2),p2r.obj.PolyCurve)
        
    def testPolyCurveCopyMoveByVec(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_move_by_vec()
        self.assertEqual(type(polyCurve2),p2r.obj.PolyCurve)
        
    def testPolyCurveCopyByOffset(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_by_offset((0,0,0),2)
        self.assertEqual(type(polyCurve2),p2r.obj.PolyCurve)    

    def testPolyCurveCopyBySplit(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_by_split((0,0,0),1)
        self.assertEqual(type(polyCurve2[0]),p2r.obj.PolyCurve)
        
    def testPolyCurveCopyByTrim(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polyCurve2 = polycurve1.dupl.copy_by_trim((0,1))
        self.assertEqual(type(polyCurve2),p2r.obj.PolyCurve)
        
    def testPolyCurveTangent(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.eval.tangent(1,0)
        self.assertEqual(len(polycurve2),3) 
    
    def testPolyCurveEvaluate(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.eval.evaluate(1,0)
        self.assertEqual(len(polycurve2),3) 
    
    def testPolyCurveExplode(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.func.explode()
        self.assertEqual(type(polycurve2),list) 
        
    def testPolyCurveGroups(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.grps.groups()
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve) 
        
    def testPolyCurveTopGroup(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.grps.top_group()
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve) 
        
    def testPolyCurveIndex(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.mtrl.index()
        self.assertEqual(type(polycurve2),int) 
        
    def testPolyCurveSource(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.mtrl.source()
        self.assertEqual(type(polycurve2),int) 
        
    def testPolycurveDegree(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.degree(1)
        self.assertEqual(type(polycurve2),int)     
            
    def testPolycurveDim(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.dim(1)
        self.assertEqual(type(polycurve2),int) 
    
    def testPolycurveDomain(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.domain(1)
        self.assertEqual(type(polycurve2),tuple)        
        
    def testPolycurveEditPnts(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.edit_pnts("true",1)
        self.assertEqual(type(polycurve2),int)  

    def testPolycurveEndPnts(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.end_pnt(1)
        self.assertEqual(type(polycurve2),tuple)       
                       
    def testPolycurveKnotCount(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.knot_count(1)
        self.assertEqual(type(polycurve2),int) 
                          
    def testPolycurveKnots(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.knots(1)
        self.assertEqual(type(polycurve2),tuple)  

    def testPolycurveLength(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.length(1)
        self.assertEqual(type(polycurve2),float) 
         
    def testPolycurveMidPnts(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.mid_pnt()
        self.assertEqual(type(polycurve2),tuple)          
        
    def testPolycurveControlPntCount(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.control_pnt_count(1)
        self.assertEqual(type(polycurve2),int) 
        
    def testPolycurveControlPnts(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.control_pnts(1)
        self.assertEqual(type(polycurve2),tuple)  

    def testPolycurveStartPnt(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.start_pnt(1)
        self.assertEqual(type(polycurve2),tuple)  
                          
    def testPolycurveWeight(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.prop.weights(1)
        self.assertEqual(type(polycurve2),tuple) 
                          
    def testPolycurveArrows(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.stat.arrows()
        self.assertEqual(type(polycurve2),int) 
        
    def testPolyCurveMirror(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.mirror((0,0,0),(1,1,1))
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveMove(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.move((0,0,0),(1,1,1))
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveMoveByVec(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.move_by_vec(((0,0,0),(1,1,1)))
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveOrient(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        pl1 = ((0,0,0),(1,0,0),(0,1,0))
        pl2 = ((10,0,0),(1,0,0),(0,1,0))
        polycurve2 = polycurve1.trfm.orient(pl1,pl2)
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveRemap(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.remap((0,0,0),(1,1,1))
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveRotate(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.rotate((0,0,0),45)
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)  
        
    def testPolyCurveScale(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.trfm.scale((0,0,0),(1,2,3))
        self.assertEqual(type(polycurve2),p2r.obj.PolyCurve)     
        
    def testPolyCurveDescription(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.util.description()
        self.assertEqual(type(polycurve2),unicode)   
        
    def testPolyCurveDump(self):
        arc1 = p2r.obj.Line.create((0,0,0), (10,0,0))
        arc2 = p2r.obj.Line.create((10,0,0), (20,20,0))
        polycurve1 = p2r.obj.PolyCurve.create((arc1,arc2))
        polycurve2 = polycurve1.util.dump()
        self.assertEqual(type(polycurve2),unicode) 
if __name__ == '__main__':
    unittest.main()