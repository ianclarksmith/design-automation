class Test1(object):
    def __init__(self):
        self.test2 = Test2()
        
class Test2(object):
    def __init__(self):
        print "hello"
    def xyz(self):
        print "hi from xyz"
    
t = Test1()

t.test2.xyz()