import unittest
import py2rhino as p2r

class obj_test(unittest.TestCase):
    
    def testCreateGroup(self):
        grp = p2r.ent.Group.create()
        self.assertEqual(type(grp),p2r.ent.group.Group)
        
    def testGroupAddObject(self):
        grp = p2r.ent.Group.create()
        sph1 = p2r.obj.Sphere.create((0,0,0), 5)
        grp2 = grp.objs.add_object(sph1)
        self.assertEqual(type(grp2),bool)

    def testGroupAddObjects(self):
        grp = p2r.ent.Group.create()
        sph1 = p2r.obj.Sphere.create((0,0,0), 5)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        grp2 = grp.objs.add_objects((sph1,arc1))
        self.assertEqual(type(grp2),int)    

    def testGroupRemoveObject(self):
        grp = p2r.ent.Group.create()
        sph1 = p2r.obj.Sphere.create((0,0,0), 5)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        grp.objs.add_objects((sph1,arc1))
        grp3 = grp.objs.remove_object(sph1)
        self.assertEqual(type(grp3),bool)
        
    def testGroupRemoveObjects(self): 
        grp = p2r.ent.Group.create()
        sph1 = p2r.obj.Sphere.create((0,0,0), 5)
        arc1 = p2r.obj.Arc.create((0,0,0), 5, 45)
        grp.objs.add_objects((sph1,arc1))
        grp3 = grp.objs.remove_objects((sph1,arc1))
        self.assertEqual(type(grp3),int)       
            
    def testGroupDeleteGroup(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.modf.delete()
        self.assertEqual(type(grp2),bool)        
        
    def testGroupIsEmpty(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.test.is_empty()
        self.assertEqual(type(grp2),bool)       

    def testGroupHide(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.dspl.hide()
        self.assertEqual(type(grp2),int)
        
    def testGroupShow(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.dspl.show(grp)
        self.assertEqual(type(grp2),int)    
        
    def testGroupLock(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.dspl.lock()
        self.assertEqual(type(grp2),int)            

    def testGroupUnlock(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.dspl.unlok(grp) #TODO: shouldn't it be unlock?
        self.assertEqual(type(grp2),int) 

    def testGroupName(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.prop.name(grp)
        self.assertEqual(type(grp2),unicode)
                
    def testGroupRename(self):
        grp = p2r.ent.Group.create()
        grp2 = grp.prop.rename(grp)
        self.assertEqual(type(grp2),unicode)
        
if __name__ == '__main__':
    unittest.main()