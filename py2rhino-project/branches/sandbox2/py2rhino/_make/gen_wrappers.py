import keyword
from util import *
from py2rhino._make.data.gen_wrp_in import descriptors as wrp

out_folder = "..\\_base\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for function_list_name in wrp.__dict__.keys():
        if function_list_name.endswith('_functions'):
            function_list = wrp.__dict__[function_list_name]
            data_dict[function_list_name] = {}
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    function = function_list.__dict__[function_name]
                    data_dict[function_list_name][function_name] = function
    return data_dict

#===============================================================================
# Write the RhinoscriptFunctions class
#===============================================================================
def write_RhinoscriptFunctions_class(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_class_header(f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import exceptions')
        w(f,'import pythoncom')
        w(f,'from _util import *')
        w(f,'from _rhinoscript import IRhinoScript', nle=2)
        w(f,'class _RhinoscriptFunctions(IRhinoScript):', nle=2)
    #---------------------------------------------------------------------------
    def write_init(f):
        w(f,'# Class constructor', tabs=1, nls=0, nle=1)
        w(f,'def __init__(self, _rso):', tabs=1, nls=0, nle=1)
        w(f,'if _rso is None:', tabs=2, nls=0, nle=1)
        w(f,'raise exceptions.Exception', tabs=3, nls=0, nle=1)
        w(f,'# initialisation code coped from win32com.client.DispatchBaseClass', tabs=2, nls=0, nle=1)
        w(f,'oobj = _rso', tabs=2, nls=0, nle=1)
        w(f,'oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)', tabs=2, nls=0, nle=1)
        w(f,'self.__dict__["_oleobj_"] = oobj', tabs=2, nls=0, nle=2)
        
    #---------------------------------------------------------------------------
    def write_class_function(function_dict, f):
    
        #get the param data into a set of lists for easy access
        params_name = []
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
            #check if we still have arrays with no type specified
            if param_type == 'arr':
                print '\tThe following function has "arr" parameters: ', function_dict['function_name']
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
        params_flattened = ', '.join(params_flattened)        
        if num_params == 1:
            params_magic_numbers = params_magic_numbers + ','
            params_flattened = params_flattened + ','
        
        #w(f, ('params = [', ', '.join(params_name), ']'), tabs=2, nls=1, nle=0)
        #w(f, ('required = [', ', '.join(params_required), ']'), tabs=2, nls=1, nle=0)
        w(f, ('magic = (', params_magic_numbers, ')'), tabs=2, nls=1, nle=0)
        w(f, ('flattened = (', params_flattened, ')'), tabs=2, nls=1, nle=1)
        #w(f, ('magic, flattened = select_params(params, required, magic, flattened)'), tabs=2, nls=1, nle=1)
    
        #now write the function    
        magic_str = str(magic_id) + ', 1, '+returns_magic_numbers+', magic'
        w(f, ['return self._ApplyTypes_(', magic_str,', u"', function_dict['function_vb_name'],'", None, *flattened)'], tabs=2, nls=1, nle=2)
    #---------------------------------------------------------------------------
    #open the file
    f = open(out_folder + '_rhinoscript_functions.py', mode='w')
    
    #write header and init
    write_class_header(f)
    write_init(f)
    
    for function_list_name in sorted(data_dict.keys()):
        print function_list_name
        for function_name in sorted(data_dict[function_list_name].keys()):
            write_class_function(data_dict[function_list_name][function_name], f)
            
    #close the file
    f.close()
    #---------------------------------------------------------------------------
#===============================================================================
# Write all the modules that wrap the RhinoscriptFunctions class
#===============================================================================
def write_function_modules(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_module_header(f):
        w(f,'# Auto-generated module that wraps the RhinoscriptFunctions class', nle=2)
        w(f,'import pythoncom', nle=2)        
        w(f,'_rsf = None', nle=2)
    #---------------------------------------------------------------------------
    def write_module_function(function_dict, f):
        #get the param data into a set of lists for easy access
        params_name = []
        params_opt_or_req = []
        num_params = len(function_dict['function_parameters'])
        
        for param_num in range(num_params):
            #get the list of parameters
            param_list = function_dict['function_parameters']
            #extract the data
            params_name.append(param_list[param_num][0])
            params_opt_or_req.append(param_list[param_num][2])
        
        #create the method signature
        w(f, ('def ', function_dict['function_name']), tabs=0, nle=0)
        if num_params > 0:
            param_str = ''
            for i in range(num_params):
                param_str += params_name[i]
                if params_opt_or_req[i] == 'OPT':
                    param_str = param_str + '=pythoncom.Empty'
                param_str += ', '
            param_str = param_str[:-2]
            w(f, ('(', param_str, '):'), tabs=0, nle=1)
        else:
            w(f, '():', tabs=0, nle=1)
        
        #TODO: write the documentation
        
        #now write the function call
        w(f, ('return _rsf.',function_dict['function_name'],'(', ', '.join(params_name), ')'), tabs=1, nls=1, nle=2)  
    #---------------------------------------------------------------------------
    for function_list_name in sorted(data_dict.keys()):
        f = open(out_folder + function_list_name[:-10] + '.py', mode='w')
        #write the module header
        write_module_header(f)
        for function_name in sorted(data_dict[function_list_name].keys()):
            #write the function
            write_module_function(data_dict[function_list_name][function_name], f)
        #close the file
        f.close()
#===============================================================================
# Write the init file
#===============================================================================
def write_init_file(data_dict):
    f = open(out_folder + '__init__.py', mode='w')
    
    w(f, 'from win32com.client import Dispatch')
    w(f, 'import time')
    w(f, 'app = Dispatch("Rhino4.Interface")')
    w(f, 'time.sleep(1)')
    w(f, 'app.Visible = True')
    w(f, '_rso = app.GetScriptObject', nle = 2)
    
    w(f, 'from _rhinoscript_functions import _RhinoscriptFunctions')
    w(f, '_rsf = _RhinoscriptFunctions(_rso)', nle=2)    
    for function_list_name in sorted(data_dict.keys()):
        module_name = function_list_name[:-10]
        w(f, ('import ', module_name))
        w(f, (module_name, '._rsf = _rsf'))
    #close the file
    f.close()
#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_RhinoscriptFunctions_class(data_dict)
    write_function_modules(data_dict)
    write_init_file(data_dict)
    print "done"