import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testArcDensity(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.density()
        self.assertEqual(type(arc2),bool)          
        
    def testArcMaxAngle(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_angle()
        self.assertEqual(type(arc2),bool)  
        
    def testArcAspectRatio(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_aspect_ratio()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMaxDistEdgeToSrf(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_dist_edge_to_srf()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMaxEdgeLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.max_edge_length()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMinEdgeLength(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.min_edge_length()
        self.assertEqual(type(arc2),bool)  
        
    def testArcMinInitialGridQuads(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.min_initial_grid_quads()
        self.assertEqual(type(arc2),bool)  
        
    def testArcQuality(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.quality()
        self.assertEqual(type(arc2),bool)  
        
    def testArcSettings(self):
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        arc2 = arc1.rndr.settings()
        self.assertEqual(type(arc2),bool)  
        
    def testBoxDensity(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.density()
        self.assertEqual(type(box2),bool)   
        
    def testBoxMaxAngle(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.max_angle()
        self.assertEqual(type(box2),bool)  
        
    def testBoxAspectRatio(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.max_aspect_ratio()
        self.assertEqual(type(box2),bool)  
        
    def testBoxMaxDistEdgeToSrf(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.max_dist_edge_to_srf()
        self.assertEqual(type(box2),bool)  
        
    def testBoxMaxEdgeLength(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.max_edge_length()
        self.assertEqual(type(box2),bool)  
        
    def testBoxMinEdgeLength(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.min_edge_length()
        self.assertEqual(type(box2),bool)  
        
    def testBoxMinInitialGridQuads(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.min_initial_grid_quads()
        self.assertEqual(type(box2),bool)  
        
    def testBoxQuality(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.quality()
        self.assertEqual(type(box2),bool)  
        
    def testBoxSettings(self):
        box1 = p2r.obj.Box.create(((0,0,0),(0,0,1),(5,0,0),(10,0,0),(20,0,0),(20,0,1),(8,0,0),(20,10,0)))
        box2 = box1.rndr.settings()
        self.assertEqual(type(box2),bool)  
        
    def testCircleDensity(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.density()
        self.assertEqual(type(circle2),bool)   
        
    def testCircleMaxAngle(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.max_angle()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleAspectRatio(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.max_aspect_ratio()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleMaxDistEdgeToSrf(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.max_dist_edge_to_srf()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleMaxEdgeLength(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.max_edge_length()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleMinEdgeLength(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.min_edge_length()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleMinInitialGridQuads(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.min_initial_grid_quads()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleQuality(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.quality()
        self.assertEqual(type(circle2),bool)  
        
    def testCircleSettings(self):
        circle1 = p2r.obj.Circle.create((0,0,0), 45)
        circle2 = circle1.rndr.settings()
        self.assertEqual(type(circle2),bool)  
        
    def testConeDensity(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.density()
        self.assertEqual(type(cone2),bool)   
        
    def testConeMaxAngle(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.max_angle()
        self.assertEqual(type(cone2),bool)  
        
    def testConeAspectRatio(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.max_aspect_ratio()
        self.assertEqual(type(cone2),bool)  
        
    def testConeMaxDistEdgeToSrf(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.max_dist_edge_to_srf()
        self.assertEqual(type(cone2),bool)  
        
    def testConeMaxEdgeLength(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.max_edge_length()
        self.assertEqual(type(cone2),bool)  
        
    def testConeMinEdgeLength(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.min_edge_length()
        self.assertEqual(type(cone2),bool)  
        
    def testConeMinInitialGridQuads(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.min_initial_grid_quads()
        self.assertEqual(type(cone2),bool)  
        
    def testConeQuality(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.quality()
        self.assertEqual(type(cone2),bool)  
        
    def testConeSettings(self):
        cone1 = p2r.obj.Cone.create((0,0,0), (1,1,1), 5)
        cone2 = cone1.rndr.settings()
        self.assertEqual(type(cone2),bool)  

if __name__ == '__main__':
    unittest.main()