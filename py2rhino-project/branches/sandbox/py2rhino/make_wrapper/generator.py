from ct  import rhinoscript as ct_rs
from pw32 import  rhinoscript as pw32_rs
import keyword
from util import *

def write_classes(folders):
    for folder_name in folders.keys():
        write_class(folder_name, folders[folder_name])

def write_class(folder_name, folder_data):
    #get the names formatted in the right way
    class_file_name = folder_name[:-8].lower()
    class_name = ''.join(map(lambda i: i.capitalize(), class_file_name.split("_")))
    
    #open, write, and close
    f = open("..\\gen\\" + class_file_name + ".py", mode='w')
    write_class_header(class_name, f)
    for file_name in sorted(folder_data.keys()):
        write_class_method(file_name, folder_data[file_name], f)
    f.close()
    
def write_class_header(class_name, f):
    w(f,"# Auto-generated wrapper for Rhino4 RhinoScript functions", nle=2)
    w(f,"import exceptions")
    w(f,"from _utils import *")
    w(f,"from _rhinoscript import IRhinoScript", nle=2)
    w(f,"class %s(IRhinoScript):" % class_name, nle=4)

def write_class_method(file_name, file_data, f):

    #get the names into the right format
    vb_method_name = file_name
    py_method_name = camel_to_underscore(file_name)
    if keyword.iskeyword(py_method_name):
        py_method_name += "_rh"
    vb_params = []
    py_params = []
    if file_data["params"]:
        for param in file_data["params"]:
            vb_params.append(param[0])
            py_param = camel_to_underscore(param[0])
            if keyword.iskeyword(py_param):
                py_param += "_param"
            py_params.append(py_param)
        
    #first check if this is a method with mismatch in parameters
    if not params_match_ct(file_name, file_data):
        w(f, ["def ", py_method_name, "(self):"], tabs=1, nle=1)
        w(f, '"""', tabs=2, nle=2)
        w(f, "METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH", tabs=2, nls=1, nle=2)
        w(f, '"""', tabs=2, nls=1, nle=2)
        w(f, "raise exceptions.NotImplementedError", tabs=2, nle=2)
        return
            
    #create the method signature
    w(f, ["def ", py_method_name, "(self"], tabs=1, nle=0)
    if py_params:
        w(f, [", ", ", ".join(py_params), "):"], tabs=0, nle=1)
    else:
        w(f, "):", tabs=0, nle=1)

    #create the method documentation
    #TODO: add syntax example here
    #TODO: use the py_params format in the doc string
    w(f, '"""', tabs=2, nle=2)    
    w(f, file_data["help"], tabs=2, nle=2)
    if file_data["params"]:
        w(f, "Parameters", tabs=2, nle=2)
        for param in file_data["params"]:
            w(f, [param[0], " : ", param[1],", ", param[2], ", ", param[3], ", ", param[-1]], tabs=2, nle=1)
    else:
        w(f, "No parameters", tabs=2, nle=1)
    if file_data["returns"]:
        w(f, "Returns", tabs=2, nls=1, nle=2)
        for returns in file_data["returns"]:
            w(f, [returns[0], " : ", returns[1]], tabs=2, nle=1)
    else:
        w(f, "No returns", tabs=2, nls=1, nle=2)        
    w(f, '"""', tabs=2, nls=1, nle=2)
    #w(f, "pass", tabs=2, nle=2)
    
    #mapping from type to magic numbers
    #VT_I2 = 2 = signed short
    #VT_I4 = 3 = signed long
    #VT_R4 = 4 = signed float
    #VT_R8 = 5 = signed double  
    type_map = {
        "bln":"VT_BOOL",
        "int":"VT_I2",        
        "lng":"VT_I4",
        "dbl":"VT_R8",
        "str":"VT_BSTR",        
        "arrdbl":"VT_ARRAY + VT_R8",
        "arrstr":"VT_ARRAY + VT_BSTR",       
        "va":"VT_VARIANT",
        "n":"VT_I2"
    }
    
    #figure out the params, adding in flatten for all arrays
    py_params_flattened = []
    if file_data["params"]:
        for param in file_data["params"]:
            py_param = camel_to_underscore(param[0])
            if keyword.iskeyword(py_param):
                py_param += "_param"
            if param[3].startswith("arr"):
                py_param = "flatten(" + py_param + ")"
            py_params_flattened.append(py_param)
    py_params_flattened = ", ".join(py_params_flattened)

    #figure out the magic numbers
    magic_id = get_ct_id_by_name(vb_method_name)
    magic_returns = "(VT_VARIANT, 0)"
    magic_params = []
    for i in file_data["params"]:
        if i[3] in type_map.keys():
            param = "(" + str(type_map[i[3]]) + ", 1)"
        else:
            param = i[3]
            print "ERROR FINDING TYPE: ", i[3], file_name
        magic_params.append(param)
    magic_params = ", ".join(magic_params)
    
    #now write the function    
    magic = str(magic_id) + ", 1, "+magic_returns+", ("+magic_params+",)"
    w(f, ["return self._ApplyTypes_(", magic,", u'",vb_method_name,"', None, ", py_params_flattened, ")"], tabs=2, nle=2)

def pretty_print_data(folder_data):
    space = "    "
    for folder in sorted(folder_data.keys()):
        print folder
        for file_name in sorted(folder_data[folder].keys()):
            print space, file_name
            print space, space, "Help = ", folder_data[folder][file_name]["help"]
            print space, space, "Syntax = ", folder_data[folder][file_name]["syntax"]
            print space, space, "Parameters : "
            counter = 1
            for param in folder_data[folder][file_name]["params"]:
                print space, space, "  ", counter, ") ", param[0], " = ", param[1], param[2], param[3]
                counter += 1
            print space, space, "Returns : "
            counter = 1            
            for return_val in folder_data[folder][file_name]["returns"]: 
                print space, space, "  ", counter, ") ", return_val[0], " = ", return_val[1]
                counter += 1

    
def params_match_ct(file_name, file_data):
    num_ct_params = get_ct_num_params(file_name)
    num_doc_params = len(file_data['params'])
    return num_ct_params == num_doc_params 
    
def compare_with_ct(folder_data):
    count_mis = 0
    count_ok = 0
    for folder_name in folder_data.keys():
        for file_name in folder_data[folder_name]:
            if is_in_ct(file_name):
                num_ct_params = get_ct_num_params(file_name)
                num_doc_params = len(folder_data[folder_name][file_name]['params'])            
                if ( num_doc_params != num_ct_params ):
                    count_mis += 1
                    print "============================================"
                    print "MISMATCH IN PARAMETERS"
                    print file_name + " in " + folder_name
                    print "params from docs files:" 
                    for i in folder_data[folder_name][file_name]['params']:
                        print "\t", i
                    print "params from comtypes file : "
                    for i in get_ct_params(file_name):
                        print "\t", i
                    print "============================================"
                else:
                    count_ok += 1
            else:
                print "MISSING: ", file_name, " in ", folder_name
    
    print "number of mismatches = ", count_mis, " out of ", count_ok
                    
def get_ct_name_by_id(id):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if id == i[2][0]:
            return i[1]
    return None

def get_ct_id_by_name(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if name == i[1]:
            return i[2][0]
    return None

def get_ct_num_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if name == i[1]:
            return len(i[-1])
    return None

def get_ct_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if name == i[1]:
            params = []
            for j in i[-1]:
                if j[0] == []:
                    flag = "Required"
                else:
                    flag = "Optional"
                params.append((j[2], flag, j[1].__name__))
            return params
    return None
    
def find_methods_mismatch(folder_data):
    print "MISSING METHODS"
    for folder_name in folder_data.keys():
        for file_name in folder_data[folder_name]:
            if not is_in_ct(file_name):
                print "ct \t", file_name, " in ", folder_name
            if not is_in_pw32(file_name):
                print "pw32 \t", file_name, " in ", folder_name



def is_in_pw32(name):
    return name in pw32_rs.IRhinoScript.__dict__.keys()

def is_in_ct(name):
    if get_ct_id_by_name(name) == None: 
        return False
    return True

#===============================================================================
# Run
#===============================================================================

data = parse_docs()
find_methods_mismatch(data)
#compare_with_ct(data)
write_classes(data)

#pretty_print_data(data) 


