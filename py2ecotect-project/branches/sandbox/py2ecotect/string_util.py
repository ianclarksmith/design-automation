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
        if listElements != 0:
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
        if len(string) != 0:
            return typeFunc(string)
        else:
            return None
    except:
        print "Error in type conversion: __toType()"            
        return None
