import py2rhino as p2r

#print p2r.obj.Ellipse.create(( (0,0,0), (1,0,0), (0,0,1)), 10, 5)
#p2r.obj.Cylinder.create((0,0,0), (0,0,20), 5, True)

c = p2r.obj.Cylinder.create_by_plane( ( (20,0,0),(2,0,0),(0,0,12) ), 18, 2, True )

class B(object): 
    def test_b(self): 
        pass 
 
class A(object): 
    def __init__(self): 
        self.b = B() 
 
x = A() 
x.b.test_b() #code completion works fine here... 
 
def test3(): 
    y = A() 
    assert isinstance(y, A)
    #code completion does not work here... 

