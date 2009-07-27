

class Base(object):
    @classmethod
    def test(cls):
        print "hello"
        return cls()

class A(Base):
    def __init__(self):
        print "I am in A init"


class B(Base):
    pass


a = A.test()
b = B.test()

print a, b