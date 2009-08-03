import keyword
from exceptions import Exception
from util import *
from py2rhino.make.data.templates_obj import descriptors as des_obj

out_folder = "..\\"
#===============================================================================
# Run some checks
#===============================================================================
def get_data_dictionary(debug=False):
    
    print des_obj.__dict__.keys()
    
    class_map = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            if debug: print function_list_name
            function_list = des_obj.__dict__[function_list_name]
            for class_name in function_list.__dict__.keys():
                if not class_name.startswith('__'):
                    clas = function_list.__dict__[class_name]
                    if debug: print "\t", class_name
                    
                    #create an empty dict to store class methods
                    if not class_name in class_map.keys():
                        class_map[class_name] = {}
                    
                    #inherits
                    inherits_from = clas.__dict__["inherits"]
                    
                    #holds
                    holds = {}
                    if "holds" in clas.__dict__.keys():
                        holds = clas.__dict__["holds"]
                        
                    #constructors
                    if "constructors" in class_map[class_name].keys():
                        constructors = class_map[class_name]["constructors"]
                    else:                    
                        constructors = {}
                    if "Constructors" in clas.__dict__.keys():
                        for function_name in clas.__dict__["Constructors"].__dict__.keys():
                            if not function_name.startswith("__"):
                                constructors[function_name] = clas.__dict__["Constructors"].__dict__[function_name]
                                
                    #methods
                    if "methods" in class_map[class_name].keys():
                        methods = class_map[class_name]["methods"]
                    else:                                     
                        methods = {}
                    if "Methods" in clas.__dict__.keys():
                        for function_name in clas.__dict__["Methods"].__dict__.keys():
                            if not function_name.startswith("__"):
                                methods[function_name] = clas.__dict__["Methods"].__dict__[function_name]
                        
                    #class methods
                    if "class_methods" in class_map[class_name].keys():
                        class_methods = class_map[class_name]["class_methods"]
                    else:                                     
                        class_methods = {}
                    if "ClassMethods" in clas.__dict__.keys():
                        for function_name in clas.__dict__["ClassMethods"].__dict__.keys():
                            if not function_name.startswith("__"):
                                class_methods[function_name] = clas.__dict__["ClassMethods"].__dict__[function_name]
                    
                    if debug:
                        print "\t\tinherits_from" , inherits_from
                        print "\t\tholds" , holds
                        print "\t\tconstructors" , constructors
                        print "\t\tmethods" , methods
                        print "\t\tclass_methods" , class_methods
                    
                    #create an empty dict to store class data
                    class_map[class_name] = {}
                    class_map[class_name]["inherits"] = inherits_from
                    class_map[class_name]["holds"] = holds
                    class_map[class_name]["constructors"] = constructors
                    class_map[class_name]["methods"] = methods
                    class_map[class_name]["class_methods"] = class_methods                    
                    
                    
    return class_map

#===============================================================================
# Write the classes
#===============================================================================
def write_rhinoscript_classes(data_dict):
    #Some sub-functions
    #---------------------------------------------------------------------------
    def write_class_header(class_name, parent_class_name, class_dict, f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import pythoncom')
        w(f,'from exceptions import Exception')
        
        #import the parent
        parent_module_name = camel_to_underscore(parent_class_name)        
        if parent_class_name != 'object':
            w(f,('from py2rhino.', parent_module_name, ' import ', parent_class_name))
           
        #import the holds
        for hold_name in sorted(class_dict['holds'].keys()):
            hold_class_name = class_dict['holds'][hold_name]
            hold_module_name = camel_to_underscore(hold_class_name)
            w(f,('from py2rhino.', hold_module_name, ' import ', hold_class_name))
        
        w(f,'_rsf = None', nls=1, nle=2)   
        w(f,('class ', class_name,'(', parent_class_name,'):'), nle=2)
        
    #---------------------------------------------------------------------------
    def write_init(class_name, class_dict, f):
        w(f,'# Class constructor', tabs=1)
        w(f,'def __init__(self, rhino_id=None):', tabs=1)
        w(f,'if rhino_id==None:', tabs=2)
        if class_name.startswith('_'):
            w(f,'raise Exception("rhino_id is required.")', tabs=3)
        else:
            w(f,'raise Exception("Use the create... methods to create instances of this class.")', tabs=3)
        w(f,'self.rhino_id = rhino_id', tabs=2, nle=2)
        
        #write each hold to the class constructor
        for hold_name in sorted(class_dict['holds'].keys()):
            hold_class_name = class_dict['holds'][hold_name]
            w(f,('self.',hold_name,' = ',hold_class_name,'(rhino_id)'), tabs=2)
        
    #---------------------------------------------------------------------------
    def write_method(function_name, class_name, method_type, method_dict, f):
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
        if method_type in ('CONSTRUCTOR', 'CLASS_METHOD'):
            w(f, '@classmethod', tabs=1, nls=1, nle=0)
            self_or_cls = 'cls'
        else:
            self_or_cls = 'self'
            
        #create the method signature
        #TODO:add support for hidden parameters
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
                        raise Exception('Cannot understand array type')
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
            if return_type.startswith('_Object') or return_type.startswith('_Entity') or return_type == 'self':
                w(f, ('return '+class_name+'(rhino_id)'), tabs=2, nls=1, nle=2)
            elif return_type.startswith('array_of _Object') or return_type.startswith('array_of _Entity') or return_type == 'array_of self':
                w(f, ('return map(lambda i: '+class_name+'(i), rhino_id)'), tabs=2, nls=1, nle=2)
            else:
                raise Exception('Cannot understand return type')
        else:
            w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)#TODO: deal with return types
    #---------------------------------------------------------------------------
    for class_name in sorted(data_dict.keys()):
        print class_name
        
        class_dict = data_dict[class_name]
        
        #get the class parent
        parent_class_name = 'object'
        if class_dict["inherits"] != None:
            parent_class_list = class_dict["inherits"]
            assert len(parent_class_list) == 1#we assume single inheritance for the moment
            parent_class_name = parent_class_list[0].split(".")[-1]
            
        #get the module names
        module_name = camel_to_underscore(class_name)
        
        #open the file
        f = open(out_folder + module_name + '.py', mode='w')
        
        #write header and init
        write_class_header(class_name, parent_class_name, class_dict, f)
        write_init(class_name, class_dict, f)        
        
        #write each constructor to the class file
        for function_name in sorted(class_dict['constructors'].keys()):
            print function_name
            method_dict = class_dict['constructors'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CONSTRUCTOR', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'CONSTRUCTOR', method_dict, f)

        #write each method to the class file
        for function_name in sorted(class_dict['methods'].keys()):
            print function_name
            method_dict = class_dict['methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'METHOD', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'METHOD', method_dict, f)    

        #write each class method to the class file
        for function_name in sorted(class_dict['class_methods'].keys()):
            print function_name
            method_dict = class_dict['static_methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'STATIC_METHOD', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'STATIC_METHOD', method_dict, f)
            
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
    
    for class_name in sorted(data_dict.keys()):
        if not class_name.startswith('_'):
            #get the module name
            module_name = camel_to_underscore(class_name)
            w(f, ('import ', module_name))
            w(f, (module_name, '._rsf = _rsf'))        
            w(f, ('from ', module_name, ' import ', class_name))
    #close the file
    f.close()
#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_rhinoscript_classes(data_dict)
    write_init_file(data_dict)

    print "done generating classes"
    
    
    
    
    
    