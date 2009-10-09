import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testCreateBlock(self):
        blk = p2r.ent.Block("test")
        blki = p2r.ent.BlockInstance.create(blk,(0,0,0))
        self.assertEqual(type(blki),p2r.ent.block.BlockInstance)
        
    def testCreateByXform(self):
        blk = p2r.ent.Block("test")
        blki = p2r.ent.BlockInstance.create_by_xform(blk,((1,0,0,0), (0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(type(blki),p2r.ent.block.BlockInstance)
    
    def testInstanceInsertPoint(self):
        blk = p2r.ent.Block("test")
        blki = p2r.ent.BlockInstance.instance_insert_point()
        self.assertEqual(type(blki),p2r.ent.block.BlockInstance)
        
    def testInstanceName(self):
        blk = p2r.ent.Block("test")
        blki1 = blk.instance_name()
        self.assertEqual(type(blki1),p2r.ent.block.BlockInstance)
        
    def testExplodeInstance(self):
        blk = p2r.ent.Block("test")
        blki1 = p2r.ent.BlockInstance.explode_instance()
        self.assertEqual(type(blki1),p2r.ent.block.BlockInstance)
         
    def testBlockRename(self):
        blk = p2r.ent.Block("test")
        blk_rnm = blk.objs.rename("test")
        self.assertEqual(type(blk_rnm),unicode)           
         
    def testBlockCount(self):
        blk = p2r.ent.Block("test")
        blk_cnt = blk.objs.object_count()
        self.assertEqual(type(blk_cnt),int)           
        
    def testBlockObjects(self):
        blk = p2r.ent.Block("test")
        blks = blk.objs.objects()
        self.assertEqual(type(blks[0]),unicode)       
        
    def testCreateIsEmbedded(self):
        blk = p2r.ent.Block("test")
        blk_emd = blk.test.is_embedded()
        self.assertEqual(type(blk_emd),bool)    
        
    def testCreateIsInUse(self):
        blk = p2r.ent.Block("test")
        blk_use = blk.test.is_in_use()
        self.assertEqual(type(blk_use),bool)      
        
    def testCreateIsReference(self):
        blk = p2r.ent.Block("test")
        blk_ref = blk.test.is_reference()
        self.assertEqual(type(blk_ref),bool)      

    def testCreateDescription(self):
        blk = p2r.ent.Block("test")
        blk_des = blk.prop.description()
        self.assertEqual(type(blk_des),str) 

    def testCreateInstanceCount(self):
        blk = p2r.ent.Block("test")
        blki_cnt = blk.prop.instance_count()
        self.assertEqual(type(blki_cnt),int) 
        
    def testCreateInstances(self):
        blk = p2r.ent.Block("test")
        blki = blk.prop.instances()
        self.assertEqual(type(blki),str) 

    def testCreatePath(self):
        blk = p2r.ent.Block("test")
        blk_pth = blk.prop.path()
        self.assertEqual(type(blk_pth),str)        

    def testCreateUrl(self):
        blk = p2r.ent.Block("test")
        blk_url = blk.prop.url()
        self.assertEqual(type(blk_url),str)     

    def testCreateUrlTag(self):
        blk = p2r.ent.Block("test")
        blk_url = blk.prop.url_tag()
        self.assertEqual(type(blk_url),str)            
        
    def testCreateDelete(self):
        blk = p2r.ent.Block("test")
        blk_del = blk.modf.delete()
        self.assertEqual(type(blk_del),bool)
        
if __name__ == '__main__':
    unittest.main()