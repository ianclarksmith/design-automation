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
        polyCurve2 = polycurve1.dupl.copy_by_sub((0,0,0),(10,0,0))
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
        polyCurve2 = polycurve1.dupl.copy_by_offset(polycurve1,2)
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
if __name__ == '__main__':
    unittest.main()