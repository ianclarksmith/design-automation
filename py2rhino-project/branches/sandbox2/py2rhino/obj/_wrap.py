class WrapBase(object):
    def __init__(self, obj):
        object.__setattr__(self, "obj", obj) 
    def __getattribute__(self, name):
        obj = object.__getattribute__(self, "obj")
        return getattr(obj, name)
    def __setattr__(self, name, value):
        obj = object.__getattribute__(self, "obj")
        return setattr(obj, name, value)