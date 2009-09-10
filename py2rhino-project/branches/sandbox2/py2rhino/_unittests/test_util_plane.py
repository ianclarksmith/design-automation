import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testPlaneDistanceToPln(self):
        planesurface1 = p2r.util.plane.distance_to_pln(((0,0,0),(0,1,0),(1,0,0)), (0,0,0))
        self.assertEqual(type(planesurface1),float)
        
    def testPlaneEvaluate(self):
        planesurface1 = p2r.util.plane.evaluate(((0,0,0),(0,1,0),(1,0,0)), (0,0,0))
        self.assertEqual(type(planesurface1[0]),float)
        
    def testPlaneIntersect3Plns(self):
        planesurface1 = p2r.util.plane.intersect_3_plns(((0,0,0),(0,1,0),(1,0,0)), ((1,0,0),(0,1,0),(1,0,0)),((0,0,0),(1,1,0),(1,0,0)))
        self.assertEqual(type(planesurface1),float)        
        
    def testPlaneMove(self):
        planesurface1 = p2r.util.plane.move(((0,0,0),(0,1,0),(1,0,0)), (0,0,0))
        self.assertEqual(type(planesurface1[0][0]),float) 

    def testPlaneClosestPnt(self):
        planesurface1 = p2r.util.plane.closest_pnt(((0,0,0),(0,1,0),(1,0,0)), (0,0,0))
        self.assertEqual(type(planesurface1[0]),float) 
        
    def testPlaneEquation(self):
        planesurface1 = p2r.util.plane.equation(((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(planesurface1[0]),float) 
        
    def testPlaneFitFromPnts(self):
        planesurface1 = p2r.util.plane.fit_from_pnts((0,0,0))
        self.assertEqual(type(planesurface1[0]),float) 
        
    def testPlaneFromFrame(self):
        planesurface1 = p2r.util.plane.from_frame((0,0,0), (1,0,0),(1,1,0))
        self.assertEqual(type(planesurface1[0][0]),float) 
        
    def testPlaneFromNormal(self):
        planesurface1 = p2r.util.plane.from_normal((0,0,0), (1,0,0))
        self.assertEqual(type(planesurface1[0][0]),float) 
        
    def testPlaneFromPoint(self):
        planesurface1 = p2r.util.plane.from_pnts((0,0,0), (1,0,0),(1,1,0))
        self.assertEqual(type(planesurface1[0][0]),float) 
        
    def testPlaneIntersect2Plns(self):
        planesurface1 = p2r.util.plane.intersect_2_plns(((0,0,0),(0,1,0),(1,0,0)),((0,0,0), (1,0,0),(1,1,0)))
        self.assertEqual(type(planesurface1[0][0]),float) 

    def testPlaneXform(self):
        planesurface1 = p2r.util.plane.xform(((0,0,0),(0,1,0),(1,0,0)),((1,0,0,0), (0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(planesurface1),float) 
        
    def testPlaneRotate(self):
        planesurface1 = p2r.util.plane.rotate(((0,0,0),(0,1,0),(1,0,0)),45,(1,0,0))
        self.assertEqual(type(planesurface1[0][0]),float) 

    def testPlaneworldXYPlane(self):
        planesurface1 = p2r.util.plane.world_x_y_plane()
        self.assertEqual(type(planesurface1[0][0]),float) 

    def testPlaneworldYZPlane(self):
        planesurface1 = p2r.util.plane.world_y_z_plane()
        self.assertEqual(type(planesurface1[0][0]),float) 

    def testPlaneworldZXPlane(self):
        planesurface1 = p2r.util.plane.world_z_x_plane()
        self.assertEqual(type(planesurface1[0][0]),float) 
                
if __name__ == '__main__':
    unittest.main()