class _m(object):
    """This is the doc for class _m"""
    def __init__(self):
        self.pqr = X.A()
    def m1(self):
        """This is the doc for method x1"""
        pass

class X(object):
    """This is the doc for class A"""
    class mmm(_m):
        """This is the doc for class A"""
        def __init__(self, pqr):
            self.pqr = pqr
        def a1(self):
            """This is the doc for method a1"""
            print self.pqr
    def __init__(self):
        self.mmm = X.Mmm("hello x mmm")
        self.pqr = "hello x"
    def x1(self):
        """This is the doc for method x1"""
        pass
    
class Y(object):
    """This is the doc for class A"""
    class mmm(_m):
        """This is the doc for class A"""
        def __init__(self, pqr):
            pass
        def b1(self):
            """This is the doc for method b1"""
            pass
    def __init__(self):
        self.mmm = Y.Mmm("hello y mmm")        
        self.pqr = "hello y"
        
    def y1(self):
        """This is the doc for method y1"""
        pass
    
x =  X()
x.mmm.a1()

y = Y()
y.mmm.b1()