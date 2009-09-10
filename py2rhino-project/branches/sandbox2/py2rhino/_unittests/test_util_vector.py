import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testVectorIsParallelTo(self):
        vector1 = p2r.util.vector.is_parallel_to(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),int)        
    
    def testVectorIsPerpendicularTo(self):
        vector1 = p2r.util.vector.is_perpendicular_to(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),bool)
        
    def testVectorIsTiny(self):
        vector1 = p2r.util.vector.is_tiny(((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),bool)
    
    def testVectorAdd(self):
        vector1 = p2r.util.vector.add(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1[0]),float)        
    
    def testVectorCompare(self):
        vector1 = p2r.util.vector.compare(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),int)      
        
    def testVectorCreate(self):
        vector1 = p2r.util.vector.create((0,0,0),(0,1,0))
        self.assertEqual(type(vector1[0]),float)  
        
    def testVectorCrossProduct(self):
        vector1 = p2r.util.vector.cross_product(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1[0]),float) 
        
    def testVector(self):
        vector1 = p2r.util.vector.divide(((0,0,0),(0,1,0),(1,0,0)),2)
        self.assertEqual(type(vector1[0]),float) 
        
    def testVectorDotProduct(self):
        vector1 = p2r.util.vector.dot_product(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),float) 
        
    def testVectorLength(self):
        vector1 = p2r.util.vector.length(((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),float) 
          
    def testVectorMultiply(self):
        vector1 = p2r.util.vector.multiply(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1),float) 
        
    def testVectorReverse(self):
        vector1 = p2r.util.vector.reverse(((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1[0]),float) 
        
    def testVectorRotate(self):
        vector1 = p2r.util.vector.rotate(((0,0,0),(0,1,0),(1,0,0)),45,((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1[0]),float) 
        
    def testVectorScale(self):
        vector1 = p2r.util.vector.scale(((0,0,0),(0,1,0),(1,0,0)),2)
        self.assertEqual(type(vector1[0]),float) 
          
    def testVectorSubtract(self):
        vector1 = p2r.util.vector.subtract(((0,0,0),(0,1,0),(1,0,0)),((0,0,0),(0,1,0),(1,0,0)))
        self.assertEqual(type(vector1[0]),float) 
        
    def testVectorTransform(self):        
        vector1 = p2r.util.vector.transform(((0,0,0),(0,1,0),(1,0,0)),((0,0,0,0),(0,1,0,0),(0,2,0,0),(0,3,0,0)))
        self.assertEqual(type(vector1[0]),float)         
        
    def testVectorUnitize(self):
        vector1 = p2r.util.vector.unitize((0,0,1))
        self.assertEqual(type(vector1[0]),float) 
if __name__ == '__main__':
    unittest.main()