import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testLineClosestPt(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pt = p2r.util.line.closest_pnt(line1, (10,0,0))
        self.assertEqual(type(pt)[0], list)
    
    def testLineIntersect2Line(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create((5,0,10), (10,10,10))
        pt = p2r.util.line.intersect_2_lines(line1,line2)
        self.assertEqual(type(pt),list)
    
    def testLineMaxDistanceToPnt(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pt = p2r.util.line.max_distance_to_pnt(line1, (10,0,0))
        self.assertEqual(type(pt)[0], bool)
    
    def testLineMaxDistanceToLine(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create((5,0,10), (10,10,10))
        pt = p2r.util.line.max_distance_to_line(line1, line2)
        self.assertEqual(type(pt)[0], bool)
    
    def testLineMinDistanceToPnt(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pt = p2r.util.line.min_distance_to_pnt(line1, (10,0,0))
        self.assertEqual(type(pt)[0], bool)
    
    def testLineMinDistanceToLine(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        line2 = p2r.obj.Line.create((5,0,10), (10,10,10))
        pt = p2r.util.line.min_distance_to_line(line1, line2)
        self.assertEqual(type(pt)[0], bool)
    
    def testLinePln(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pt = p2r.util.line.line_pln(line1)
        self.assertEqual(type(pt)[0], bool)
    
    def testLineIntersectPln(self):
        line1 = p2r.obj.Line.create((5,0,0), (10,0,10))
        pl1 = (1,0,0)
        pt = p2r.util.line.intersect_pln(line1,pl1)
        self.assertEqual(type(pt)[0], bool)
        
if __name__ == '__main__':
    unittest.main()
