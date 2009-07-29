import keyword
from util import *
from py2rhino.make.data.templates_api import descriptors as obj

out_folder = "..\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for function_list_name in obj.__dict__.keys():
        if function_list_name.endswith('_functions'):
            function_list = obj.__dict__[function_list_name]
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    #get the method data
                    method = function_list.__dict__[function_name]
                    #get the class name
                    class_name = method['method_location'].split('.')[-1]
                    if class_name in data_dict.keys():
                        data_dict[class_name] = {}
                    data_dict[class_name][function_name] = method
                    
    
    return data_dict

#===============================================================================
# Write the classes
#===============================================================================
def write_rhinoscript_classes(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_class_header(f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import py2rhino.functions as rf')
        w(f,'class ', nle=0)
        
    #---------------------------------------------------------------------------
    def write_init(f):
        w(f,'# Class constructor', tabs=1, nls=0, nle=1)
        w(f,'def __init__(self):', tabs=1, nls=0, nle=1)
        w(f,'pass', tabs=2, nls=0, nle=1)
    #---------------------------------------------------------------------------
    def write_class_method(function_name, method_dict, f):
        #get the param data into a set of lists for easy access
        params_name = []
        params_opt_or_req = []
        num_params = len(method_dict['method_parameters'])
        
        for param_num in range(num_params):
            #get the list of parameters
            param_list = method_dict['method_parameters']
            #extract the data
            params_name.append(param_list[param_num][0])
            params_opt_or_req.append(param_list[param_num][2])
        
        #create the method signature
        w(f, ('def ', method_dict['method_name']), tabs=0, nle=0)
        if num_params > 0:
            param_str = ''
            for i in range(num_params):
                param_str += params_name[i]
                if params_opt_or_req[i] == 'OPT':
                    param_str = param_str + '=None'
                param_str += ', '
            param_str = param_str[:-2]
            w(f, ('(', param_str, '):'), tabs=0, nle=1)
        else:
            w(f, '():', tabs=0, nle=1)
        
        #TODO: write the documentation
        
        #now write the function call
        w(f, ('return _rsf.',function_name,'(', ', '.join(params_name), ')'), tabs=1, nls=1, nle=2)  
    #---------------------------------------------------------------------------
    for class_name in sorted(data_dict.keys()):
        
        #open the file
        f = open(out_folder + '_rhinoscript_functions.py', mode='w')
        
        #write header and init
        write_class_header(f)
        write_init(f)        
        
        for function_name in sorted(data_dict[class_name].keys()):
            write_class_method(function_name, data_dict[class_name][function_name], f)
            
        #close the file
        f.close()
    #---------------------------------------------------------------------------
    
    
    
    
    
    
    