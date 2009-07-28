import keyword
from util import *
from py2rhino.make.data.templates_fnc import descriptors as fnc

out_folder = "..\\functions\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for function_list_name in fnc.__dict__.keys():
        if function_list_name.endswith('_functions'):
            function_list = fnc.__dict__[function_list_name]

            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    function = function_list.__dict__[function_name]
                    data_dict[function_name] = function
    return data_dict

#===============================================================================
# Write the class
#===============================================================================
def write_class(data_dict):
    #open the file
    f = open(out_folder + '_rhinoscript_functions.py', mode='w')
    
    #write header and init
    write_class_header(f)
    write_init(f)
    
    
    for function_name in sorted(data_dict.keys()):
        write_function(data_dict[function_name], f)
            
    #close the file
    f.close()
#------------------------------------------------------------------------------ 
def write_class_header(f):
    w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
    w(f,'import exceptions')
    w(f,'import pythoncom')
    w(f,'import py2rhino')        
    w(f,'from py2rhino._util import *')
    w(f,'from py2rhino._rhinoscript import IRhinoScript', nle=2)
    w(f,'class RhinoscriptFunctions(IRhinoScript):', nle=2)
#------------------------------------------------------------------------------ 
def write_init(f):
    w(f,'# Class constructor', tabs=1, nls=0, nle=1)
    w(f,'def __init__(self):', tabs=1, nls=0, nle=1)
    w(f,'if py2rhino._rso is None:', tabs=2, nls=0, nle=1)
    w(f,'raise exceptions.Exception', tabs=3, nls=0, nle=1)
    w(f,'# initialisation code coped from win32com.client.DispatchBaseClass', tabs=2, nls=0, nle=1)
    w(f,'oobj = py2rhino._rso', tabs=2, nls=0, nle=1)
    w(f,'oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)', tabs=2, nls=0, nle=1)
    w(f,'self.__dict__["_oleobj_"] = oobj', tabs=2, nls=0, nle=2)
    
#------------------------------------------------------------------------------ 
def write_function(function_dict, f):

    #type map for params
    string_to_type_map = {
        "bln":"Boolean",
        "int":"Integer",        
        "lng":"Integer",
        "dbl":"Double",
        "str":"String",
        "array_of bln":"Array of Booleans",
        "array_of int":"Array of Integers",
        "array_of lng":"Array of Integers",        
        "array_of dbl":"Array of Doubles",
        "array_of str":"Array of Strings",       
        "array_of any":"Array of Generic Objects",
        #"array_of ???":"Array of ???", 
        #"va":"Variant",
        #"n":"Integer",
        #"arr":"Array of ????"
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
        "array_of bln":"VT_ARRAY + VT_BOOL",
        "array_of int":"VT_ARRAY + VT_I2",
        "array_of lng":"VT_ARRAY + VT_I4",  
        "array_of dbl":"VT_ARRAY + VT_R8",
        "aarray_of str":"VT_VARIANT",
        "array_of any":"VT_VARIANT",       
        #"array_of ???":"VT_VARIANT",               
        #"va":"VT_VARIANT",
        #"n":"VT_I2",
        #"arr":"VT_VARIANT"
    }
    
    #get the param data into a set of lists for easy access
    params_name = []
    params_type = []
    params_opt_or_req = []
   
    params_flattened = []    
    params_magic_numbers = []
    params_required = [] 
    
    num_params = len(function_dict['function_parameters'])
    
    for param_num in range(num_params):
        #get the list of parameters
        param_list = function_dict['function_parameters']
        #extract the data
        param_py_name = param_list[param_num][0]
        param_type = param_list[param_num][1]
        param_opt_or_req = param_list[param_num][2]
        #flattened?
        param_flattened = param_py_name
        if param_type.startswith('array'):
            param_flattened = 'flatten_params(' + param_py_name + ')'
        #required?
        param_required = 'False'
        if params_opt_or_req == 'REQ':
            param_required = 'True'
        #add data to the lists
        params_name.append(param_py_name)
        params_type.append(string_to_type_map[param_type])
        params_flattened.append(param_flattened)
        params_opt_or_req.append(param_opt_or_req)
        params_required.append(param_required)
        params_magic_numbers.append( '(' + str(string_to_magic_map[param_type]) + ', 1)')
    
    #create the method signature
    w(f, ('def ', function_dict['function_name']), tabs=1, nle=0)
    if num_params > 0:
        param_list = ''
        for i in range(num_params):
            param_list = param_list + params_name[i]
            if not params_required[i]:
                param_list = param_list + '=None'
            param_list = param_list + ', '
        param_list = param_list[:-2]
        w(f, ('(self, ', param_list, '):'), tabs=0, nle=1)
    else:
        w(f, '(self):', tabs=0, nle=1)

    #figure out the magic numbers
    magic_id = function_dict['function_com_id']
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
    w(f, ['return self._ApplyTypes_(', magic_str,', u"', function_dict['function_vb_name'],'", None, *flattened)'], tabs=2, nls=1, nle=2)

#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_class(data_dict)
    print "done"