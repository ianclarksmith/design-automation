import re

def _convert_args_to_string(*args):
    arg_str = ""
    for i in args:
        if not isinstance(i, str):
            i = str(i)
        arg_str += (i + " ")
    return arg_str.strip()

def _convert_str_to_list(string, *typeFunc):
    str_list = re.split("[,\s]+", string[:-1])
    listElements = len(str_list)
    try:
        if str_list[0].lower() != "nil" and listElements != 0:
            new_list = []
            if listElements == len(typeFunc):
                typeFunc = tuple(typeFunc)
                str_list = list(str_list)
                for i in range(listElements):
                    new_list.append(typeFunc.__getitem__(i)(str_list.__getitem__(i)))
            else:
                for i_str in str_list:
                    i = typeFunc.__getitem__(0)(i_str)
                    new_list.append(i)
            
            return new_list
        else:
            return None
    except:
        print "Error in type conversion: __toTypeList()"
        return None
    
def _convert_str_to_type(string, typeFunc):
    string = string[:-1]
    try:
        if string.lower() != "nil" and len(string) != 0:
            return typeFunc(string)
        else:
            return None
    except:
        print "Error in type conversion: __toType()"            
        return None

def scale_1000(input):
    return scale_by_factor(input, 1000)

def scale_inverse_1000(input):
    return scale_by_factor(input, 0.001)

def scale_by_factor(input, scale_factor):
    if input == None:
        return None
    elif isinstance(input, int) or isinstance(input, float):
        return input * scale_factor
    elif isinstance(input, list) or isinstance(input, tuple):
        if isinstance(input[0], int or float):
            return map(lambda i: i*scale_factor, input)
        elif isinstance(input[0], list) or isinstance(input[0], tuple):
            return map(lambda i: map(lambda j: j*scale_factor, i), input)
    raise Exception        

class WrapBase(object):
    def __init__(self, obj):
        object.__setattr__(self, "obj", obj) 
    def __getattribute__(self, name):
        obj = object.__getattribute__(self, "obj")
        return getattr(obj, name)
    def __setattr__(self, name, value):
        obj = object.__getattribute__(self, "obj")
        return setattr(obj, name, value)   
    
    