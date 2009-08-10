class A(object):
    pass

class B(A):
    def test(self):
        return C()
    def ppp(self):
        pass
    def qqq(self):
        pass
    def rrr(self):
        pass

class C(object):
    def __init__(self):
        self.b = B()
    def xxx(self):
        pass
    def yyy(self):
        pass
    def zzz(self):
        pass
        
c1 = C()
c2 = c1.b.test()

