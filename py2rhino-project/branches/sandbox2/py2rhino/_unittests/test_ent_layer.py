import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testCreateLayer(self):
        lyr = p2r.ent.Layer.create()
        self.assertEqual(type(lyr),p2r.ent.layer.Layer)      
    
    def testDeleteLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.modf.delete()
        self.assertEqual(type(lyr2),bool)       
    
    def testPurgeLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.modf.purge()
        self.assertEqual(type(lyr2),bool)   
    
    def testExpandLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.dspl.expand(True)
        self.assertEqual(type(lyr2),bool)  
        
    def testMakeCurrentLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.make_current()
        self.assertEqual(type(lyr2),bool) 
        
    def testNameLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.name("test")
        self.assertEqual(type(lyr2),bool)  
        
    def testRenameLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.name("test")
        self.assertEqual(type(lyr2),bool)  
        
if __name__ == '__main__':
    unittest.main()