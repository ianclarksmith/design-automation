
#=======================
class _Object(object):
    def __init__(self, id, points):
        print id
        self.func = PointFunc()
        
        #add nodes
        
    @classmethod
    def _create_empty_object(cls, type):
        return 5
    
class Point(_Object):
    
    @classmethod
    def create(cls, points):
        id = Point._create_empty_object(Point, "wall")
        return Point(id, points)
    

class PointFunc(object):
    def func2(self):
        print "hello"
#=======================

c = Point.create()
print c.__dict__
c.func.func2()
c.func.func2()