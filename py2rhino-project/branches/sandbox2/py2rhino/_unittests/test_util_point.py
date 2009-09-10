import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    def testPointAdd(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.add(pt1,pt2)
        self.assertEqual(type(pt[0]),float)
        
    def testPointsBoundingBox(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.points_bounding_box((pt1,pt2))
        self.assertEqual(type(pt[0][0]),float)   
        
    def testPointsClosestPoint(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.points_closest_point((pt1,pt2),(0,0,0))
        self.assertEqual(type(pt),int)        

    def testPointsCompare(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.compare(pt1,pt2)
        self.assertEqual(type(pt),bool)   
        
    def testPointsDivide(self):
        pt1 = (0,0,0)
        pt = p2r.util.point.divide(pt1,1)
        self.assertEqual(type(pt[0]),float)   
        
    def testPointsScale(self):
        pt1 = (0,0,0)
        pt = p2r.util.point.scale(pt1,1)
        self.assertEqual(type(pt[0]),float)   

    def testPointsSubtract(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.subtract(pt1,pt2)
        self.assertEqual(type(pt[0]),float)   
        
    def testPointsAreCoplanar(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        pt = p2r.util.point.points_are_coplanar((pt1,pt2))
        self.assertEqual(type(pt),bool)   
        
    def testProjectPointToSurface(self):
        pt1 = (0,0,0)
        pt2 = (0,0,1)
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        pt = p2r.util.point.project_point_to_surface(((pt1,pt2)),nurvesurface1,(0,0,0))
        self.assertEqual(type(pt[0]),float)      

    def testPullPoint(self):
        nurvesurface1  = p2r.obj.NurbsSurface.create_by_corner_pnts(((0,0,0),(5,0,0),(5,5,0),(0,5,0)))
        pt = p2r.util.point.pull_points(nurvesurface1,(0,0,0))
        self.assertEqual(type(pt[0][0]),float)   
        
    def testPointXform(self):
        pt1 = (0,0,1)
        planesurface1 = p2r.util.point.transform(pt1,((1,0,0,0), (0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(planesurface1),float) 
if __name__ == '__main__':
    unittest.main()