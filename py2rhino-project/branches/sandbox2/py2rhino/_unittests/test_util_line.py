import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testLineClosestPt(self):
        pt = p2r.util.line.closest_pnt(((5,0,0), (10,0,10)), (10,0,0))
        self.assertEqual(type(pt[0]), float)
    
    def testLineIntersect2Line(self):
        pt = p2r.util.line.intersect_2_lines(((5,0,0), (10,0,10)),((5,0,10), (10,10,10)))
        self.assertEqual(type(pt),list)
    
    def testLineMaxDistanceToPnt(self):
        pt = p2r.util.line.max_distance_to_pnt(((5,0,10), (10,10,10)), (10,0,0))
        self.assertEqual(type(pt), float)
    
    def testLineMaxDistanceToLine(self):
        line1 = ((5,0,0), (10,0,10))
        line2 = ((5,0,10), (10,10,10))
        pt = p2r.util.line.max_distance_to_line(line1, line2)
        self.assertEqual(type(pt), float)
    
    def testLineMinDistanceToPnt(self):
        line1 = ((5,0,0), (10,0,10))
        pt = p2r.util.line.min_distance_to_pnt(line1, (10,0,0))
        self.assertEqual(type(pt), float)
    
    def testLineMinDistanceToLine(self):
        line1 = ((5,0,0), (10,0,10))
        line2 = ((5,0,10), (10,10,10))
        pt = p2r.util.line.min_distance_to_line(line1, line2)
        self.assertEqual(type(pt), float)
    
    def testLinePln(self):
        line1 = ((5,0,0), (10,0,10))
        pt = p2r.util.line.line_pln(line1)
        self.assertEqual(type(pt), tuple)
    
    def testLineIntersectPln(self):
        line1 = ((5,0,0), (10,0,10))
        pl1 = (1,0,0)
        pt = p2r.util.line.intersect_pln(line1,pl1)
        self.assertEqual(type(pt), list)

    def testLineTransform(self):        
        line1 = ((5,0,0), (10,0,10))
        vector1 = p2r.util.line.xform(line1,((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(vector1[0]),float)         
if __name__ == '__main__':
    unittest.main()
