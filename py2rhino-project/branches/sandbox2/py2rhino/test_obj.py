import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    #def testSingleWord(self):
        #self.assertEqual('justoneword', 'justoneword')
        
    def testCreateArc(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        self.assertEqual(type(arc1), p2r.obj.Arc)
    
    def testCreateArcByPt(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        self.assertEqual(type(arc1),p2r.obj.Arc)
        
    def testCreateArcByFillet(self):
        arc1 = p2r.obj.Arc.create_by_3pt((0,0,0), (20,0,0), (10,10,0))
        arc2 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc3 = arc2.create_by_fillet(arc1,arc2)
        self.assertEqual(type(arc3),p2r.obj.Arc)
    
    def testBox(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        self.assertEqual(type(box1),p2r.obj.Box)
        
    def testCircleByPt(self):
        circle1 = p2r.obj.Circle.create_by_3pt((0,0,0),(0,1,0),(1,0,0))
        self.assertEqual(type(circle1),p2r.obj.Circle)
    
    def testCircle(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        self.assertEqual(type(circle1),p2r.obj.Circle)
    
    def testCreateCone(self):
        cone1 = p2r.obj.Cone.create((0,0,0), 8, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
        
    def testCreateConeByPlane(self):
        cone1 = p2r.obj.Cone.create_by_plane((0,0,0), 8, 5)
        self.assertEqual(type(cone1),p2r.obj.Cone)
    
    def testCreateCylinder(self):
        cylinder1 = p2r.obj.Cylinder.create((0,0,0),2, 5)
        self.assertEqual(type(cylinder1),p2r.obj.Cylinder)
        
    def testCreateCylinderbyPlane(self):
        cylinder1 = p2r.obj.Cylinder.create_by_plane((0,0,0),2, 5)
        self.assertEqual(type(cylinder1),p2r.obj.Cylinder)
        
    def testCreateEllipse(self):
        ellipse1 = p2r.obj.Ellipse.create(((0,0,0),(0,1,0),(1,0,0)), 5, 10)
        self.assertEqual(type(ellipse1),p2r.obj.Ellipse)
if __name__ == '__main__':
    unittest.main()
