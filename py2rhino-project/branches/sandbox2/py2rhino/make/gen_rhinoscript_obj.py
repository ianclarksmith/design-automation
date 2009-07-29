import keyword
from util import *
from py2rhino.make.data.templates_obj import descriptors as obj

out_folder = "..\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for function_list_name in obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            function_list = obj.__dict__[function_list_name]
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    print function_list_name, function_name
                    
                    #get the method data
                    method = function_list.__dict__[function_name]
                    #get the class name
                    class_list = method['method_location']
                    if not class_list in data_dict.keys():
                        data_dict[class_list] = {}
                    data_dict[class_list][function_name] = method
                    
    
    return data_dict

#===============================================================================
# Write the classes
#===============================================================================
def write_rhinoscript_classes(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_class_header(class_name, class_parent_name, f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import py2rhino.functions as rf')
        w(f,('class ', class_name,'(', class_parent_name,'):'), nle=0)
        
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
        param_list = method_dict['method_parameters']
        num_params = len(param_list)
        
        for param_num in range(num_params):
            #extract the data
            params_name.append(param_list[param_num][0])
            params_opt_or_req.append(param_list[param_num][2])
        
        #create the method signature
        w(f, ('def ', method_dict['method_name']), tabs=1, nle=0)
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
        w(f, ('return _rsf.',function_name,'(', ', '.join(params_name), ')'), tabs=2, nls=1, nle=2)  
    #---------------------------------------------------------------------------
    for class_str in sorted(data_dict.keys()):
        #split the list of classes
        class_list = class_str.split('.')
        
        #get the class name
        class_name = class_list[-1]
        #get the class parent
        class_parent_name = 'object'
        if len(class_list) > 1:
            class_parent_name = class_list[-2]
        #get the module name
        module_name = camel_to_underscore(class_name)
        
        #open the file
        f = open(out_folder + module_name + '.py', mode='w')
        
        #write header and init
        write_class_header(class_name, class_parent_name, f)
        write_init(f)        
        
        #write each method to the class file
        for function_name in sorted(data_dict[class_str].keys()):
            print class_name
            print function_name
            write_class_method(function_name, data_dict[class_str][function_name], f)
            
        #close the file
        f.close()
    #---------------------------------------------------------------------------
#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    print data_dict
    write_rhinoscript_classes(data_dict)

    print "done"
    
    
    
    
    
    