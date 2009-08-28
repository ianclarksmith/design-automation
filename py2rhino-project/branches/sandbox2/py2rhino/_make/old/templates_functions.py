import keyword
from util import *
from py2rhino.data import gen_py2rhino as p2r 
from py2rhino.data import api_definition as api
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
                        
    return data_dict

                    
#===============================================================================
# Run
#===============================================================================
def write_classes(data_dict):
    for module_name in sorted(data_dict.keys()):
        write_class(module_name, data_dict[module_name])

def write_class(module_name, module_dict):
    #open, write, and close
    f = open(out_folder + module_name + '.py', mode='w')
    write_class_header(underscore_to_camel(module_name), f)
    write_init(f)
    for method_name in sorted(module_dict.keys()):
        if len(module_dict[method_name]['params_html']) != len(module_dict[method_name]['params_com']):
            for method_num in range(len(module_dict[method_name]['syntax_html'])):
                write_class_method(module_dict[method_name], method_num, f)
            print module_name, method_name
        else:
            
            write_class_method(module_dict[method_name], -1, f)
    f.close()
    
def write_class_header(class_name, f):
    w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
    w(f,'import exceptions')
    w(f,'import pythoncom')
    w(f,'import py2rhino')        
    w(f,'from py2rhino._util import *')
    w(f,'from py2rhino._rhinoscript import IRhinoScript', nle=2)
    w(f,'class %s(IRhinoScript):' % class_name, nle=2)

def write_init(f):
    w(f,'# Class constructor', tabs=1, nls=0, nle=1)
    w(f,'def __init__(self):', tabs=1, nls=0, nle=1)
    w(f,'if py2rhino._rso is None:', tabs=2, nls=0, nle=1)
    w(f,'raise exceptions.Exception', tabs=3, nls=0, nle=1)
    w(f,'# initialisation code coped from win32com.client.DispatchBaseClass', tabs=2, nls=0, nle=1)
    w(f,'oobj = py2rhino._rso', tabs=2, nls=0, nle=1)
    w(f,'oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)', tabs=2, nls=0, nle=1)
    w(f,'self.__dict__["_oleobj_"] = oobj', tabs=2, nls=0, nle=2)
    

def write_class_method(method_dict, method_num, f):

    #get the method name in py format
    py_method_name = method_dict['output_module_name']
    if method_num > 0:
        py_method_name = py_method_name + '_' + str(method_num + 1)
    if keyword.iskeyword(py_method_name):
        py_method_name += '_'         
    vb_method_name = method_dict['input_file_name']
   

    """
    
    #first check if this is a method with mismatch in parameters
    if len(method_dict['params_html']) != len(method_dict['params_com']):
        w(f, ['def ', py_method_name, '(self):'], tabs=1, nle=1)
        w(f, '" ""', tabs=2, nle=2)
        w(f, 'METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH', tabs=2, nls=1, nle=2)
        w(f, '" ""', tabs=2, nls=1, nle=2)
        w(f, 'raise exceptions.NotImplementedError', tabs=2, nle=2)
        return
    
    """
    
    #type map for params
    string_to_type_map = {
        "bln":"Boolean",
        "int":"Integer",        
        "lng":"Integer",
        "dbl":"Double",
        "str":"String",
        "arr_of_bln":"Array of Booleans",
        "arr_of_int":"Array of Integers",
        "arr_of_lng":"Array of Integers",        
        "arr_of_dbl":"Array of Doubles",
        "arr_of_str":"Array of Strings",       
        "arr_of_any":"Array of Generic Objects",
        "arr_of_???":"Array of ???", 
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
        "arr_of_bln":"VT_ARRAY + VT_BOOL",
        "arr_of_int":"VT_ARRAY + VT_I2",
        "arr_of_lng":"VT_ARRAY + VT_I4",  
        "arr_of_dbl":"VT_ARRAY + VT_R8",
        "arr_of_str":"VT_VARIANT",
        "arr_of_any":"VT_VARIANT",       
        "arr_of_???":"VT_VARIANT",               
        "va":"VT_VARIANT",
        "n":"VT_I2",
        "arr":"VT_VARIANT"
    }
    
    #get the param data into a set of lists for easy access
    params_name = []
    params_flattened = []
    params_type = []
    params_opt_or_req = []
    params_required = []    
    params_doc = []
    params_magic_numbers = []
    if len(method_dict['params_html']) > 0:
        for param_num in method_dict['params_html'].keys():
            param_dict = method_dict['params_html'][param_num]
            
            if (method_num == -1) or (param_dict['name'] in method_dict['syntax_html'][method_num]):
                param_py_name = param_dict['py_name']
                if keyword.iskeyword(param_py_name):
                    param_py_name += "_"
                param_flattened = param_py_name
                if param_dict['name_prefix'].startswith('arr'):
                    param_flattened = 'flatten_params(' + param_py_name + ')'
                param_required = 'False'
                if param_dict['opt_or_req'] == 'Required':
                    param_required = 'True'
                #add data to the lsists
                params_name.append(param_py_name)
                params_type.append(string_to_type_map[param_dict['name_prefix']])
                params_flattened.append(param_flattened)
                params_opt_or_req.append( param_dict['opt_or_req'])
                params_required.append(param_required)
                params_doc.append(param_dict['doc'])
                params_magic_numbers.append( '(' + str(string_to_magic_map[param_dict['name_prefix']]) + ', 1)')
    num_params = len(params_name)
    
    #create the method signature
    w(f, ('def ', py_method_name), tabs=1, nle=0)
    if num_params > 0:
        param_list = ''
        for i in range(num_params):
            param_list = param_list + params_name[i]
            if params_opt_or_req[i] == 'Optional':
                param_list = param_list + '=None'
            param_list = param_list + ', '
        param_list = param_list[:-2]
        w(f, ('(self, ', param_list, '):'), tabs=0, nle=1)
    else:
        w(f, '(self):', tabs=0, nle=1)


    
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
    w(f, '"""', tabs=2, nls=1, nle=1)

    #figure out the magic numbers
    magic_id = method_dict['id_com']
    returns_magic_numbers = '(VT_VARIANT, 0)'
    params_magic_numbers = ', '.join(params_magic_numbers)
    if num_params == 1:
        params_magic_numbers = params_magic_numbers + ','
    params_flattened = ', '.join(params_flattened)
    
    w(f, ('params = [', ', '.join(params_name), ']'), tabs=2, nls=1, nle=0)
    w(f, ('required = [', ', '.join(params_required), ']'), tabs=2, nls=1, nle=0)
    w(f, ('magic = [', params_magic_numbers, ']'), tabs=2, nls=1, nle=0)
    w(f, ('flattened = [', params_flattened, ']'), tabs=2, nls=1, nle=1)
    w(f, ('magic, flattened = select_params(params, required, magic, flattened)'), tabs=2, nls=1, nle=1)

    #now write the function    
    magic_str = str(magic_id) + ', 1, '+returns_magic_numbers+', magic'
    w(f, ['return self._ApplyTypes_(', magic_str,', u"', vb_method_name,'", None, *flattened)'], tabs=2, nls=1, nle=2)

#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_classes(data_dict)
    print "done"



