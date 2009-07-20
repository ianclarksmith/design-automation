import keyword
from util import *

from py2rhino.data import gen_py2rhino as p2r 
in_folder = "..\\data\\gen_py2rhino\\"
out_folder = "..\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    #the first set of keys will contain the module names
    for key1 in sorted(p2r.__dict__.keys()):
        if not key1.startswith("__"):
            if not isinstance(p2r.__dict__[key1], dict):
                data_dict[key1] = {}
                mod = p2r.__dict__[key1]
                #the second set of keys will contain the method names
                for key2 in sorted(mod.__dict__.keys()):
                    if not key2.startswith("__"):
                        data_dict[key1][key2] = mod.__dict__[key2]
                        
    #overwrite we overwrite the array strings with the corrected ones
    
    return data_dict

def write_array_type_strings(data_dict):
    counter = 0
    f = open(in_folder + "_array_type_strings.py", mode='w')
    w(f, '#Replace in the ??? with either "bln", "int", "dbl", or "str"', tabs=0, nls=0, nle=2)

    for module_name in sorted(data_dict.keys()):
        w(f, (module_name, ' = {'), tabs=0, nls=0, nle=1)
        for method_name in sorted(data_dict[module_name].keys()):
            has_array = False
            has_mismatch = False
            param_html_dict = data_dict[module_name][method_name]['params_html']
            param_com_dict = data_dict[module_name][method_name]['params_com']
            if len(param_html_dict) != len(param_com_dict):
                has_mismatch = True            
            for param_num in param_html_dict.keys():
                type_string = param_html_dict[param_num]['type_string']
                if type_string.startswith('arr'):
                    has_array = True
                    counter += 1
            if has_array and not has_mismatch:
                w(f, ('"', method_name, '": {'), tabs=1, nls=0, nle=1)
                for param_num in data_dict[module_name][method_name]['params_html'].keys():
                    name = param_html_dict[param_num]['name']
                    type_string = param_html_dict[param_num]['type_string']
                    if type_string == 'arr':
                        type_string += '_of_???'
                    w(f, ('"', name, '": "', type_string, '",'), tabs=2, nls=0, nle=1)
                w(f, '},', tabs=1, nls=0, nle=1)
        w(f, '},', tabs=0, nls=0, nle=1)
    f.close()
    print counter
#===============================================================================
# Run
#===============================================================================
def write_classes(data_dict):
    for module_name in sorted(data_dict.keys()):
        write_class(module_name, data_dict[module_name])

def write_class(module_name, module_dict):
    #open, write, and close
    f = open(out_folder + module_name + ".py", mode='w')
    write_class_header(underscore_to_camel(module_name), f)
    for method_name in sorted(module_dict.keys()):
        write_class_method(module_dict[method_name], f)
    f.close()
    
def write_class_header(class_name, f):
    w(f,"# Auto-generated wrapper for Rhino4 RhinoScript functions", nle=2)
    w(f,"import exceptions")
    w(f,"from py2rhino._util import *")
    w(f,"from py2rhino._rhinoscript import IRhinoScript", nle=2)
    w(f,"class %s(IRhinoScript):" % class_name, nle=4)

def write_class_method(method_dict, f):

    #get the method name in py format
    py_method_name = method_dict['output_module_name']
    vb_method_name = method_dict['input_file_name']
    if keyword.iskeyword(py_method_name):
        py_method_name += '_'    
    
    #first check if this is a method with mismatch in parameters
    if len(method_dict['params_html']) != len(method_dict['params_com']):
        w(f, ['def ', py_method_name, '(self):'], tabs=1, nle=1)
        w(f, '"""', tabs=2, nle=2)
        w(f, 'METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH', tabs=2, nls=1, nle=2)
        w(f, '"""', tabs=2, nls=1, nle=2)
        w(f, 'raise exceptions.NotImplementedError', tabs=2, nle=2)
        return
    
    #type map for params
    string_to_type_map = {
        "bln":"Boolean",
        "int":"Integer",        
        "lng":"Integer",
        "dbl":"Double",
        "str":"String",
        "arrbln":"Array of Booleans",
        "arrint":"Array of Integers",
        "arrlng":"Array of Integers",        
        "arrdbl":"Array of Doubles",
        "arrstr":"Array of Strings",       
        "va":"Variant",
        "n":"Integer",
        "arr":"Array of ????"
    }
    
    #mapping from type to magic numbers
    #VT_I2 = 2 = signed short
    #VT_I4 = 3 = signed long
    #VT_R4 = 4 = signed float
    #VT_R8 = 5 = signed double  
    string_to_magic_map = {
        "bln":"VT_BOOL",
        "int":"VT_I2",        
        "lng":"VT_I4",
        "dbl":"VT_R8",
        "str":"VT_BSTR",
        "arrbln":"VT_ARRAY + VT_BOOL",
        "arrint":"VT_ARRAY + VT_I2",
        "arrlng":"VT_ARRAY + VT_I4",  
        "arrdbl":"VT_ARRAY + VT_R8",
        "arrstr":"VT_ARRAY + VT_BSTR",       
        "va":"VT_VARIANT",
        "n":"VT_I2",
        "arr":"VT_VARIANT"
    }
    
    #get the param data into a set of lists for easy access
    params_name = []
    params_flattened = []
    params_type = []
    params_opt_or_req = []
    params_doc = []
    params_magic_numbers = []
    num_params = 0
    if method_dict['params_html']:
        num_params = len(method_dict['params_html']) 
    if num_params > 0:
        for param_num in method_dict['params_html'].keys():
            param_dict = method_dict['params_html'][param_num]
            param_name = camel_to_underscore(param_dict['name'])
            if keyword.iskeyword(param_name):
                param_name += "_"
            param_flattened = param_name
            if param_dict['type_string'].startswith('arr'):
                param_flattened = 'flatten(' + param_name + ')'
            #add data to the lsists
            params_name.append(param_name)
            params_type.append(string_to_type_map[param_dict['type_string']])
            params_flattened.append(param_flattened)
            params_opt_or_req.append( param_dict['opt_or_req'])
            params_doc.append(param_dict['doc'])
            params_magic_numbers.append( '(' + str(string_to_magic_map[param_dict['type_string']]) + ', 1)')
            
    #create the method signature
    w(f, ['def ', py_method_name, '(self'], tabs=1, nle=0)
    if params_name:
        w(f, [', ', ', '.join(params_name), '):'], tabs=0, nle=1)
    else:
        w(f, '):', tabs=0, nle=1)


    
    #create the method documentation
    #TODO: add syntax example here
    #TODO: use the py_params format in the doc string
    w(f, '"""', tabs=2, nle=0)    
    w(f, method_dict['doc_html'], tabs=2, nls=0, nle=1)
    if params_name:
        w(f, 'Parameters', tabs=2, nls=0, nle=1)
        w(f, '==========', tabs=2, nls=0, nle=1)
        for i in range(len(params_name)):
            w(f, [', '.join((params_name[i], params_type[i], params_opt_or_req[i]))], tabs=2, nls=1, nle=0)
            w(f, params_doc[i], tabs=2, nls=0, nle=0)
    else:
        w(f, 'No parameters', tabs=2, nle=1)
    if method_dict['returns_html']:
        w(f, 'Returns', tabs=2, nls=1, nle=1)
        w(f, '=======', tabs=2, nls=0, nle=1)
        for returns_num in method_dict['returns_html']:
            returns_dict = method_dict['returns_html'][returns_num]
            returns_type = returns_dict['type']
            returns_doc = returns_dict['doc']
            w(f, returns_type, tabs=2, nls=1, nle=1)
            w(f, returns_doc, tabs=2, nls=0, nle=1)
    else:
        w(f, 'No returns', tabs=2, nls=1, nle=2)        
    w(f, '"""', tabs=2, nls=1, nle=2)
    #w(f, "pass", tabs=2, nle=2)

    #figure out the magic numbers
    magic_id = method_dict['id_com']
    returns_magic_numbers = '(VT_VARIANT, 0)'
    params_magic_numbers = ', '.join(params_magic_numbers)
    if num_params == 1:
        params_magic_numbers = params_magic_numbers + ','
    params_flattened = ', '.join(params_flattened)
    
    #now write the function    
    magic = str(magic_id) + ', 1, '+returns_magic_numbers+', ('+params_magic_numbers+')'
    w(f, ['return self._ApplyTypes_(', magic,', u"', vb_method_name,'", None, ', params_flattened, ')'], tabs=2, nle=2)




#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_array_type_strings(data_dict)
    write_classes(data_dict)
    print "done"



