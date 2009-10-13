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
        self.assertEqual(type(lyr2),unicode)   
   
    def testExpandLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.expand(False)
        self.assertEqual(type(lyr2),bool)  
         
    def testColorLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.color()
        self.assertEqual(type(lyr2),int)  
        
    def testLineTypeLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.line_type()
        self.assertEqual(type(lyr2),unicode)  
        
    def testMaterialIndexLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.material_index()
        self.assertEqual(type(lyr2),int)          
          
    def testModeLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.mode()
        self.assertEqual(type(lyr2),int)         
          
    def testOrderLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.order()
        self.assertEqual(type(lyr2),int)    
          
    def testPrintColorLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.print_color()
        self.assertEqual(type(lyr2),int)    
          
    def testPrintWidthLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.print_width()
        self.assertEqual(type(lyr2),float)    
          
    def testVisibleLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.visible()
        self.assertEqual(type(lyr2),bool)    
          
    def testLockedLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.dspl.locked()
        self.assertEqual(type(lyr2),bool)    
        
    def testIsChangeableLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_changeable()
        self.assertEqual(type(lyr2),bool)  
        
    def testIsChildOfLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_child_of("Layer 23")
        self.assertEqual(type(lyr2),bool) 
        
    def testIsCurrentLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_current()
        self.assertEqual(type(lyr2),bool)         
        
    def testIsEmptyLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_empty()
        self.assertEqual(type(lyr2),bool)  
        
    def testIsExpandedLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_expanded()
        self.assertEqual(type(lyr2),bool) 
        
    def testIsOnLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_on()
        self.assertEqual(type(lyr2),bool) 
        
    def testIsParentOfLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_parent_of("Layer 23")
        self.assertEqual(type(lyr2),bool) 
        
    def testIsReferenceLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_reference()
        self.assertEqual(type(lyr2),bool) 
        
    def testIsSelectableLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_selectable()
        self.assertEqual(type(lyr2),bool) 
        
    def testIsVisibleLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_visible()
        self.assertEqual(type(lyr2),bool) 
        
    def testIsLockedLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.test.is_locked()
        self.assertEqual(type(lyr2),bool) 
        
    def testMakeCurrentLayer(self):
        lyr = p2r.ent.Layer("Layer 15")
        lyr2 = lyr.prop.make_current()
        self.assertEqual(type(lyr2),unicode) 
        
    def testNameLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.name("test")
        self.assertEqual(type(lyr2),unicode)  
        
    def testRenameLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.rename("test123")
        self.assertEqual(type(lyr2),unicode)  
        
    def testChildCountLayer(self):
        lyr = p2r.ent.Layer.create()
        lyr2 = lyr.prop.child_count()
        self.assertEqual(type(lyr2),int)  
        
    def testChildrenLayer(self):
        #lyr = p2r.ent.Layer("Layer 15")
        #lyr = p2r.ent.Layer.create(name = "Layer test", color = "100", visible = True, locked = True, parent = "Layer 15")
        lyr = p2r.ent.Layer.create(parent = "Layer 15")
        lyr2 = lyr.prop.children()
        self.assertEqual(type(lyr2[0]),unicode)  
        
if __name__ == '__main__':
    unittest.main()