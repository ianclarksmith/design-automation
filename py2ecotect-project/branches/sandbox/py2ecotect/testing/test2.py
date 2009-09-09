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
    y.b. #code completion does not work here...    