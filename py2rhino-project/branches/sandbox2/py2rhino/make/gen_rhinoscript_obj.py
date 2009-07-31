import keyword
from exceptions import Exception
from util import *
from py2rhino.make.data.templates_obj import descriptors as des_obj

out_folder = "..\\"
#===============================================================================
# Run some checks
#===============================================================================
def check_class_strings():
    class_map = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            function_list = des_obj.__dict__[function_list_name]
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    print function_list_name, function_name
                    method_dict = function_list.__dict__[function_name]
                    methods = []
                    #has this function been split
                    if method_dict.keys()[0] == 0:
                        #we have a split
                        for i in method_dict.keys():
                            methods.append(method_dict[i])
                    else:
                        methods.append(method_dict)
                    #now go through the methods list
                    for method in methods:
                        #get the class str
                        class_str = method['method_location']
                        #split the list of classes
                        class_list = class_str.split('.')
                        #get the class name
                        class_name = class_list[-1]                    
    
                        if class_name in class_map.keys():
                            assert class_map[class_name] == class_str
                        else:
                            class_map[class_name] = class_str


#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            function_list = des_obj.__dict__[function_list_name]
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    print function_list_name, function_name
                    method_dict = function_list.__dict__[function_name]
                    methods = []
                    #has this function been split
                    if method_dict.keys()[0] == 0:
                        #we have a split
                        for i in method_dict.keys():
                            methods.append(method_dict[i])
                    else:
                        methods.append(method_dict)
                    #now go through the methods list
                    for method in methods:
                        #get the class str
                        class_str = method['method_location']
                 
                        if not class_str in data_dict.keys():
                            data_dict[class_str] = {}
                        data_dict[class_str][function_name] = method
    
    return data_dict

#===============================================================================
# Write the classes
#===============================================================================
def write_rhinoscript_classes(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_class_header(class_name, parent_module_name, parent_class_name, f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import pythoncom')
        if parent_class_name != 'object':
            w(f,('from py2rhino.', parent_module_name, ' import ', parent_class_name))
        w(f,'from exceptions import Exception')           
        w(f,'_rsf = None', nls=1, nle=2)   
        w(f,('class ', class_name,'(', parent_class_name,'):'), nle=2)
        
    #---------------------------------------------------------------------------
    def write_init(f):
        w(f,'# Class constructor', tabs=1)
        w(f,'def __init__(self, rhino_id=None):', tabs=1)
        w(f,'if rhino_id==None:', tabs=2)
        w(f,'raise Exception("Use the create... methods to create instances of this class.")', tabs=3)
        w(f,'self.rhino_id = rhino_id', tabs=2, nle=2)
    #---------------------------------------------------------------------------
    def write_class_method(function_name, class_name, method_dict, f):
        #get the param data into a set of lists for easy access
        params_name = []
        params_opt_or_req = []
        params_type = []
        
        param_list = method_dict['method_parameters']
        num_params = len(param_list)
        
        for param_num in range(num_params):
            #extract the data
            params_name.append(param_list[param_num][0])
            params_type.append(param_list[param_num][1])            
            params_opt_or_req.append(param_list[param_num][2])
        
        #if this is a constructor or a class method, make it a class method
        method_type = method_dict['method_type']        
        if method_type in ('CONSTRUCTOR', 'CLASS_METHOD'):
            w(f, '@classmethod', tabs=1, nls=1, nle=0)
            self_or_cls = 'cls'
        else:
            self_or_cls = 'self'
            
        #create the method signature
        method_name = method_dict['method_name']
        w(f, ('def ', method_name), tabs=1, nls=1, nle=0)
        if num_params > 0:
            params = []
            for i in range(num_params):
                param_str = ''
                if params_type[i] == 'self':
                    pass #skip the self
                else:
                    param_str = params_name[i]
                    if params_opt_or_req[i] == 'OPT':
                        param_str = param_str + '=pythoncom.Empty'
                    params.append(param_str)
            params = ', '.join(params)
            w(f, ('(',self_or_cls,', ', params, '):'), tabs=0, nle=1)
        else:
            w(f, ('(',self_or_cls,'):'), tabs=0, nle=1)
        
        #TODO: write the documentation
        
        #a list of simple types
        simple_types = ('bln', 'int', 'lng', 'dbl', 'str', 'n', 'va')
        
        #create the arguments
        args = []        
        if num_params > 0:
            for i in range(num_params):
                if params_type[i] == 'self':
                    args.append('self.rhino_id')
                elif params_type[i] in simple_types:
                    args.append(params_name[i])
                elif params_type[i].startswith('_Object'):
                    args.append(params_name[i] + '.rhino_id')
                elif params_type[i].startswith('_Entity'):
                    args.append(params_name[i] + '.rhino_id')             
                elif params_type[i].startswith('array_of'):
                    params_type_tail = params_type[i][9:]
                    if params_type_tail in simple_types:
                        args.append(params_name[i])
                    elif params_type_tail.startswith('_Object'):
                        args.append('map(lambda i: i.rhino_id, '+params_name[i] + ')')
                    else:
                        #args.append('trouble')#TODO: complete this bit
                        raise Exception('Cannot understand type')
                else:
                    raise Exception('Cannot understand param type')
        args = ', '.join(args)

        
        #get the return type
        return_type = method_dict['method_returns']
        if len(return_type) > 0:
            return_type = return_type[0]
        else:
            return_type = None
        
        #now write the function call
        if method_type == 'CONSTRUCTOR':
            w(f, ('rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)
            if return_type.startswith('_Object') or return_type.startswith('_Entity'):
                w(f, ('return '+class_name+'(rhino_id)'), tabs=2, nls=1, nle=2)
            elif return_type.startswith('array_of _Object') or return_type.startswith('array_of _Entity') :
                w(f, ('return map(lambda i: '+class_name+'(i), rhino_id)'), tabs=2, nls=1, nle=2)
            else:
                raise Exception('Cannot understand return type')
        else:
            w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)#TODO: deal with return types
    #---------------------------------------------------------------------------
    for class_str in sorted(data_dict.keys()):
        
        #split the list of classes
        class_list = class_str.split('.')
        #check the class name
        class_name = class_list[-1]
        
        #get the class parent
        parent_class_name = 'object'
        if len(class_list) > 1:
            parent_class_name = class_list[-2]
        #get the module names
        module_name = camel_to_underscore(class_name)
        parent_module_name = camel_to_underscore(parent_class_name)
        
        #open the file
        f = open(out_folder + module_name + '.py', mode='w')
        
        #write header and init
        write_class_header(class_name, parent_module_name, parent_class_name, f)
        write_init(f)        
        
        #write each method to the class file
        for function_name in sorted(data_dict[class_str].keys()):
            print class_name
            print function_name
            write_class_method(function_name, class_name, data_dict[class_str][function_name], f)
            
        #close the file
        f.close()
    #---------------------------------------------------------------------------
#===============================================================================
# Write the init file
#===============================================================================
def write_init_file(data_dict):
    f = open(out_folder + '__init__.py', mode='w')
    w(f, ('from win32com.client import Dispatch'))
    w(f, ('import time'))
    w(f, ('app = Dispatch("Rhino4.Interface")'))
    w(f, ('time.sleep(1)'))
    w(f, ('app.Visible = True'))
    w(f, ('_rso = app.GetScriptObject'), nle=2)

    w(f, ('from functions._rhinoscript_functions import _RhinoscriptFunctions'))
    w(f, ('_rsf = _RhinoscriptFunctions(_rso)'), nle=2)
    
    classes = {}
    for class_str in sorted(data_dict.keys()):
        #split the list of classes
        class_list = class_str.split('.')
        #get the class name
        class_name = class_list[-1]
        #get the module name
        module_name = camel_to_underscore(class_name)
        #add to a dict so we dont get dups
        classes[class_name] = module_name
        
    for class_name in sorted(classes.keys()):
        module_name = classes[class_name]
        w(f, ('import ', module_name))
        w(f, (module_name, '._rsf = _rsf'))        
        w(f, ('from ', module_name, ' import ', class_name))
        
    #close the file
    f.close()
#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    check_class_strings()
    data_dict = get_data_dictionary()
    write_rhinoscript_classes(data_dict)
    write_init_file(data_dict)

    print "done"
    
    
    
    
    
    