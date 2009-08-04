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
    def write_class_header(class_name, parent_class_list, class_dict, f):
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import pythoncom')
        w(f,'from exceptions import Exception')        
        w(f,'import py2rhino as p2r')   
        w(f,'from py2rhino import _util')   
        
        #import the parent
        for parent_class_name in parent_class_list:
            parent_module_name = camel_to_underscore(parent_class_name)        
            if parent_class_name != 'object':
                w(f,('from py2rhino.', parent_module_name, ' import ', parent_class_name))
        
        #write the global _rsf variable and set it to None    
        w(f,'_rsf = None', nls=2)   
           
        #import the holds
        for hold_name in sorted(class_dict['holds'].keys()):
            hold_class_name = class_dict['holds'][hold_name]
            hold_module_name = camel_to_underscore(hold_class_name)
            w(f,('from py2rhino.', hold_module_name, ' import ', hold_class_name))

        w(f,('class ', class_name,'(', parent_class_name,'):'), nls=2, nle=2)
        
    #---------------------------------------------------------------------------
    def write_init(class_name, module_name, class_dict, f):
        w(f,'# Class constructor', tabs=1)
        if class_name.startswith('_'):
            w(f,'def __init__(self, _rhino_id, _class, _rsf_in):', tabs=1)
            w(f,'if _rhino_id==None:', tabs=2)
            w(f,'raise Exception("_rhino_id is required.")', tabs=3)
            w(f,'self._rhino_id = _rhino_id', tabs=2)
            w(f,'self._class = _class', tabs=2)            
            w(f,'global _rsf', tabs=2)
            w(f,'_rsf = _rsf_in', tabs=2)            
        else:
            w(f,'def __init__(self, _rhino_id):', tabs=1)
            w(f,'if _rhino_id==None:', tabs=2)
            w(f,'raise Exception("Use the create... methods to create instances of this class.")', tabs=3)
            w(f,'self._rhino_id = _rhino_id', tabs=2, nle=2)
        
            #write each hold to the class constructor
            for hold_name in sorted(class_dict['holds'].keys()):
                hold_class_name = class_dict['holds'][hold_name]
                w(f,('self.',hold_name,' = ',hold_class_name,'(_rhino_id, ',class_name,', _rsf )'), tabs=2)
        
    #---------------------------------------------------------------------------
    def write_method(function_name, class_name, method_type, method_dict, f):
        
        #a list of simple types
        simple_types = ('bln', 'int', 'lng', 'dbl', 'str', 'n', 'va')
        
        #a list of class types
        class_types = (
                       'GenericObject',
                       
                       'GenericCurve',
                       'Arc', 
                       'Circle', 
                       'Ellipse', 
                       'NurbsCurve',
                       'Polyline',
                       'EllipticalArc',
                       
                       'Box',
                       'Sphere',
                       'Cone',
                       'Cylinder',
                       'Torus',
                       'NurbsSurface',
                       
                       )
                        #'PolygonMesh',

        
        #get the param data into a set of lists for easy access
        params_name = []
        params_opt_or_req = []
        params_type = []
        params_default = []
        params_hidden = []                
        
        param_list = method_dict['method_parameters']
        num_params = len(param_list)
        
        for param_num in range(num_params):
            #extract the data
            params_name.append(param_list[param_num][0])
            params_type.append(param_list[param_num][1])            
            params_opt_or_req.append(param_list[param_num][2])
            if len(param_list[param_num]) > 3:
                params_default.append(param_list[param_num][3])
            else:
                params_default.append(None)
            if len(param_list[param_num]) > 4 and param_list[param_num][4] == "HIDE":
                params_hidden.append(True)                   
            else:
                params_hidden.append(False)
                
                
        #if this is a constructor or a class method, make it a class method  
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
                if params_type[i] == 'SELF':
                    pass #skip the self parameters
                elif params_hidden[i]:
                    pass #skip the hidden parameters
                else:
                    param_str = params_name[i]
                    if params_opt_or_req[i] == 'OPT':
                        param_str = param_str + '=pythoncom.Empty'
                    params.append(param_str)
            if len(params) > 0:
                params = ', '.join(params)
                w(f, ('(',self_or_cls,', ', params, '):'), tabs=0, nle=1)
            else:
                w(f, ('(',self_or_cls, '):'), tabs=0, nle=1)
        else:
            w(f, ('(',self_or_cls,'):'), tabs=0, nle=1)
        
        #TODO: write the documentation
        
        print class_name, method_name

        
        #create the arguments
        args = []        
        if num_params > 0:
            for i in range(num_params):
                if params_hidden[i]:
                    if params_default[i] == 'EMPTY':
                        args.append('pythoncom.Empty')
                    elif params_default[i] == 'TRUE':
                        args.append('True')
                    elif params_default[i] == 'FALSE':
                        args.append('False')                                                
                    else:
                        raise Exception('Cannot understand default param value')
                elif params_type[i] == 'SELF':
                    args.append('self._rhino_id')
                elif params_type[i] in simple_types:
                    args.append(params_name[i])
                elif params_type[i].startswith('_Object'):
                    args.append(params_name[i] + '._rhino_id')
                elif params_type[i].startswith('_Entity'):
                    args.append(params_name[i] + '._rhino_id')             
                elif params_type[i].startswith('array_of'):
                    params_type_tail = params_type[i][9:]
                    if params_type_tail in simple_types:
                        args.append(params_name[i])
                    elif params_type_tail.startswith('_Object') or params_type_tail.startswith('_Entity'):
                        args.append('map(lambda i: i._rhino_id, '+params_name[i] + ')')
                    else:
                        #this will highlight anything I have forgotten
                        print params_name[i], params_type[i]
                        raise Exception('Cannot understand array type for parameter')
                else:
                    raise Exception('Cannot understand param type')
        args = ', '.join(args)

        
        #get the return type
        return_type = method_dict['method_returns']
        if len(return_type) == 0:
            return_type = None
        elif len(return_type) < 3:
            return_type = return_type[0]
        else:
            raise Exception('Method does not have the right number of returns')
        
        #the function call for constructors
        if method_type == 'CONSTRUCTOR':
            w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)
            if return_type == 'SELF':
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return '+class_name+'(_rhino_id)'), tabs=3)
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3)
            elif return_type == 'array_of SELF':
                w(f, ('return map(lambda i: '+class_name+'(i), _rhino_id)'), tabs=2, nls=1, nle=2)
            else:
                raise Exception('Cannot understand return type for constructor')
        
        #the function call for methods
        elif method_type == 'METHOD':
            assert class_name.startswith('_')
            if class_name.endswith('Mdfy'):#TODO: I think this can be deleted
                if return_type == 'str':
                    w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return True'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return False'), tabs=3)                             
                elif return_type == 'bln':
                    w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)#TODO: deal with return types
                else:
                    raise Exception('The Modify method is returning something strange')
            elif return_type == None:
                w(f, ('return _rsf.',function_name,'()'), tabs=2)
            elif return_type in simple_types or return_type == 'number':
                w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2)
            elif return_type.startswith('array_of') and return_type[9:] in simple_types or return_type[9:] == 'number':
                w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2)
            elif return_type.startswith('SELF'):
                    w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return self._class(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)  
            elif return_type.startswith('_Object') or return_type.startswith('_Entity'):
                return_class_name = return_type.split('.')[-1]
                if return_class_name in class_types:
                    w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return p2r.', return_class_name, '(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)  
                else:
                    w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return _util.wrap(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)
            elif return_type.startswith('array_of _Object') or return_type.startswith('array_of _Entity'):
                return_class_name = return_type.split('.')[-1]
                w(f, ('return map(lambda i: p2r.'+return_class_name+'(i), self._rhino_id)'), tabs=2, nls=1, nle=2)#TODO:this needs more work
            else:
                raise Exception('The method returns something very strange')
            
        #the function call for class methods
        elif method_type == 'CLASS_METHOD':
            pass #ignore these for the moment
            #w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)
            
            
        #anything else
        else:
            raise Exception('Cannot understand method type')
    #---------------------------------------------------------------------------
    for class_name in sorted(data_dict.keys()):
        
        class_dict = data_dict[class_name]
        
        #get the class parent
        parent_class_list = ('object', )
        if class_dict["inherits"] != None:
            parent_class_list = class_dict["inherits"]
            
        #get the module names
        module_name = camel_to_underscore(class_name)
        
        #open the file
        f = open(out_folder + module_name + '.py', mode='w')
        
        #write header and init
        write_class_header(class_name, parent_class_list, class_dict, f)
        write_init(class_name, module_name, class_dict, f)        
        
        #write each constructor to the class file
        for function_name in sorted(class_dict['constructors'].keys()):
            method_dict = class_dict['constructors'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CONSTRUCTOR', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'CONSTRUCTOR', method_dict, f)

        #write each method to the class file
        for function_name in sorted(class_dict['methods'].keys()):
            method_dict = class_dict['methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'METHOD', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'METHOD', method_dict, f)    

        #write each class method to the class file
        for function_name in sorted(class_dict['class_methods'].keys()):
            method_dict = class_dict['class_methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CLASS_METHOD', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'CLASS_METHOD', method_dict, f)
            
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
    
    w(f, ('import _util'))
    w(f, ('_util._rsf = _rsf'))
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
    
    
    
    
    
    