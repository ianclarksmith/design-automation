import keyword
from exceptions import Exception
from util import *
from py2rhino._make.data.gen_obj_in import descriptors as des_obj
from py2rhino._make.data.gen_obj_in.docs import obj as docs_obj
from py2rhino._make.data.gen_obj_in.custom import custom_methods 

out_folder = "..\\obj\\"

#===============================================================================
# Run some checks
#===============================================================================
def get_data_dictionary():
    
    print des_obj.__dict__.keys()
    
    class_map = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            #print function_list_name
            function_list = des_obj.__dict__[function_list_name]
            for class_name in function_list.__dict__.keys():
                if not class_name.startswith('__'):
                    clas = function_list.__dict__[class_name]
                    
                    #create an empty dict to store class methods
                    if not class_name in class_map.keys():
                        class_map[class_name] = {}
                    
                    #inherits
                    inherits_from = clas.__dict__["inherits"]
                    class_map[class_name]["inherits"] = inherits_from
                    
                    #holds
                    if "holds" in clas.__dict__.keys():
                        class_map[class_name]["holds"] = clas.__dict__["holds"]
                       
                    #==============================================================
                    #constructors
                    if "constructors" in class_map[class_name].keys():
                        constructors = class_map[class_name]["constructors"]
                    else:                    
                        constructors = {}
                    if "Constructors" in clas.__dict__.keys():
                        for function_name in clas.__dict__["Constructors"].__dict__.keys():
                            if not function_name.startswith("__"):
                                constructors[function_name] = clas.__dict__["Constructors"].__dict__[function_name]
                         
                    #==============================================================          
                    #methods
                    if "methods" in class_map[class_name].keys():
                        methods = class_map[class_name]["methods"]
                    else:                                     
                        methods = {}
                    if "Methods" in clas.__dict__.keys():
                        for function_name in clas.__dict__["Methods"].__dict__.keys():
                            if not function_name.startswith("__"):
                                methods[function_name] = clas.__dict__["Methods"].__dict__[function_name]
                        
                    #==============================================================
                    #class methods - I think this can be deleted
                    if "class_methods" in class_map[class_name].keys():
                        class_methods = class_map[class_name]["class_methods"]
                    else:                                     
                        class_methods = {}
                    if "ClassMethods" in clas.__dict__.keys():
                        for function_name in clas.__dict__["ClassMethods"].__dict__.keys():
                            if not function_name.startswith("__"):
                                class_methods[function_name] = clas.__dict__["ClassMethods"].__dict__[function_name]
                    
                    #==============================================================
                    #add the methods
                    class_map[class_name]["constructors"] = constructors
                    class_map[class_name]["methods"] = methods
                    class_map[class_name]["class_methods"] = class_methods                    
                    
                    
    return class_map

#===============================================================================
# Write the classes
#===============================================================================
def write_obj_classes(data_dict):
    
    #---------------------------------------------------------------------------
    def write_class_header_and_init(class_name, parent_class_list, module_name, class_dict, f):
        #write the class signature
        w(f,('class ', class_name,'(', ','.join(parent_class_list),'):'))
        
        if not class_name.startswith('_'):
            #create an inner class for each hold
            for hold_name in sorted(class_dict['holds'].keys()):
                hold_class_name = class_dict['holds'][hold_name]
                w(f,('class ',hold_name,'(',hold_class_name,'):'), tabs=1)
                w(f,('def __init__(self, _rhino_id):'), tabs=2)
                w(f,('self._rhino_id = _rhino_id'), tabs=3)
                w(f,('self._class = ', class_name), tabs=3) 
            
            w(f,'# Class constructor', tabs=1)
            w(f,'def __init__(self, _rhino_id):', tabs=1)
            w(f,'if _rhino_id==None:', tabs=2)
            w(f,'raise Exception("Use the create... methods to create instances of this class.")', tabs=3)
            w(f,'self._rhino_id = _rhino_id', tabs=2, nle=2)
        
            #write each hold to the class constructor
            for hold_name in sorted(class_dict['holds'].keys()):
                hold_class_name = class_dict['holds'][hold_name]
                w(f,('self.',hold_name,' = ',class_name, '.', hold_name,'(_rhino_id)'), tabs=2)
        
    #---------------------------------------------------------------------------
    def write_method(function_name, class_name, method_type, method_dict, f):
        
        #a list of simple types
        simple_types = ('bln', 'int', 'lng', 'dbl', 'str', 'n', 'va')
        
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
            w(f, '@staticmethod', tabs=1, nls=1, nle=0)
            self_or_cls = None #'cls'
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
                if self_or_cls:
                    w(f, ('(',self_or_cls,', ', params, '):'), tabs=0, nle=1)
                else:
                    w(f, ('(', params, '):'), tabs=0, nle=1)
            else:
                if self_or_cls:
                    w(f, ('(',self_or_cls, '):'), tabs=0, nle=1)
                else:
                    w(f, '():', tabs=0, nle=1)
        else:
            if self_or_cls:
                w(f, ('(',self_or_cls,'):'), tabs=0, nle=1)
            else:
                w(f, '():', tabs=0, nle=1)
        
        #Write the documentation
        w(f, '"""', tabs=2)
        w(f,(docs_obj.__dict__[class_name].__dict__[method_name]), tabs=2)
        w(f, '"""', tabs=2)
        
        
        #Check if there is a custom impl for this method
        if class_name in custom_methods.__dict__.keys():
            if method_name in custom_methods.__dict__[class_name].__dict__.keys():
                impl = custom_methods.__dict__[class_name].__dict__[method_name]
                w(f, impl)
                return
                
        
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
                        w(f, ('if type(',params_name[i],') != list and type(',params_name[i],') != tuple:'), tabs=2)
                        w(f, (params_name[i],' = (',params_name[i],',)'), tabs=3)
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
        
        #the function call for CONSTRUCTORS
        if method_type == 'CONSTRUCTOR':
            w(f, ('_rhino_id = _base._rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)
            if return_type == 'SELF':
                assert not class_name.startswith('_')
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return '+class_name+'(_rhino_id)'), tabs=3)
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3)
            elif return_type == 'array_of SELF':
                assert not class_name.startswith('_')
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return map(lambda i: '+class_name+'(i), _rhino_id)'), tabs=3, nls=1, nle=2)
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3)                
            elif return_type == 'first_in_array_of SELF':
                assert not class_name.startswith('_')
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return '+class_name+'(_rhino_id[0])'), tabs=3)
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3)               
            else:
                raise Exception('Cannot understand return type for constructor')
        
        #the function call for METHODS
        elif method_type == 'METHOD':
            assert class_name.startswith('_')
            if return_type == None:
                w(f, ('return _base._rsf.',function_name,'()'), tabs=2)
            elif return_type in simple_types or return_type == 'number':
                w(f, ('return _base._rsf.',function_name,'(', args, ')'), tabs=2)
            elif return_type.startswith('array_of') and return_type[9:] in simple_types or return_type[9:] == 'number':
                w(f, ('return _base._rsf.',function_name,'(', args, ')'), tabs=2)
            elif return_type.startswith('SELF'):
                    w(f, ('_rhino_id = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return self._class(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)  
            elif return_type.startswith('_Object') or return_type.startswith('_Entity'):
                return_class_name = return_type.split('.')[-1]
                if return_class_name.startswith('_') and return_class_name.endswith('Root'):
                    w(f, ('_rhino_id = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return self._class(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3) 
                elif return_class_name.startswith('_'):
                    w(f, ('_rhino_id = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return _util.cast(_rhino_id)'), tabs=3)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)
                else:
                    w(f, ('_rhino_id = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_id:'), tabs=2)
                    w(f, ('return p2r.obj.', return_class_name, '(_rhino_id)'), tabs=3)#TODO:this needs more work
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3) 
            elif return_type.startswith('array_of _Object') or return_type.startswith('array_of _Entity'):
                return_class_name = return_type[9:].split('.')[-1]
                if return_class_name.startswith('_') and return_class_name.endswith('Root'):
                    w(f, ('_rhino_ids = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_ids:'), tabs=2)                    
                    w(f, ('return map(lambda i: self._class(i), _rhino_ids)'), tabs=3, nle=1)#TODO:this needs more work
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)                     
                elif return_class_name.startswith('_'):
                    w(f, ('_rhino_ids = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_ids:'), tabs=2)                    
                    w(f, ('return map(lambda i: _util.cast(i), _rhino_ids)'), tabs=3, nle=1)
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)                     
                else:
                    w(f, ('_rhino_ids = _base._rsf.',function_name,'(', args, ')'), tabs=2)
                    w(f, ('if _rhino_ids:'), tabs=2)                    
                    w(f, ('return map(lambda i: p2r.obj.'+return_class_name+'(i), _rhino_ids)'), tabs=3, nle=1)#TODO:this needs more work
                    w(f, ('else:'), tabs=2)
                    w(f, ('return None'), tabs=3)                     
            else:
                raise Exception('The method returns something very strange')
            
        #the function call for class methods
        elif method_type == 'CLASS_METHOD':
            pass #ignore these for the moment
            #w(f, ('return _base._rsf.',function_name,'(', args, ')'), tabs=2, nls=1, nle=2)
            
            
        #anything else
        else:
            raise Exception('Cannot understand method type')
    #---------------------------------------------------------------------------
    def write_class(class_name, class_dict, f):
        #get the class parent
        parent_class_list = ('object', )
        if class_dict["inherits"] != None:
            parent_class_list = class_dict["inherits"]
            
        #write header and init
        module_name = camel_to_underscore(class_name)
        write_class_header_and_init(class_name, parent_class_list, module_name, class_dict, f)        
        
        #write 'pass' if there are no methods
        if class_name.startswith('_') and \
            not class_dict['constructors'] and \
            not class_dict['methods'] and \
            not class_dict['class_methods']: 
            w(fb,'pass', tabs=1)
        
        #write each constructor to the class file
        for function_name in sorted(class_dict['constructors'].keys()):
            method_dict = class_dict['constructors'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CONSTRUCTOR', method_dict[i], f)
            else:
                write_method(function_name, class_name, 'CONSTRUCTOR', method_dict, f)

        #write each instance method to the class file
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
            
    #---------------------------------------------------------------------------
    #open the base file
    fb = open(out_folder + '_rhinoscript_classes.py', mode='w')
    
    w(fb,'# Auto-generated wrapper for Rhino4 RhinoScript classes')
    w(fb,'import pythoncom')
    w(fb,'from exceptions import Exception')
    
    w(fb,'import _util')
           
    w(fb,'import py2rhino as p2r')     
    w(fb,'from py2rhino import _base') 
    
    list_of_class_name = []
    for class_name in sorted(data_dict.keys()):
        list_of_class_name.append(class_name)
    
    
    sorted_list = []
    
    #add _classes that do not inherit anything
    for class_name_num in range(len(list_of_class_name)):
        class_name = list_of_class_name[class_name_num]
        if class_name.startswith("_"):
            class_dict = data_dict[class_name]
            inherits = class_dict['inherits']
            if inherits == None:
                sorted_list.append(class_name)
    
    #add _classes that do inherit
    for i in range(3):
        for class_name_num in range(len(list_of_class_name)):
            class_name = list_of_class_name[class_name_num]
            if class_name.startswith("_"):
                class_dict = data_dict[class_name]
                inherits = class_dict['inherits']
                if inherits != None:
                    if len(inherits) == 1:
                        if not class_name in sorted_list and inherits[0] in sorted_list:
                            sorted_list.append(class_name)
                    elif len(inherits) == 2:
                        if not class_name in sorted_list and inherits[0] in sorted_list and inherits[1] in sorted_list:
                            sorted_list.append(class_name)
                    else:
                        raise Exception

    #add all other
    for class_name_num in range(len(list_of_class_name)):
        class_name = list_of_class_name[class_name_num]
        class_dict = data_dict[class_name]
        inherits = class_dict['inherits']
        if inherits != None:
            if len(inherits) == 1:
                if not class_name in sorted_list and inherits[0] in sorted_list:
                    sorted_list.append(class_name)
            elif len(inherits) == 2:
                if not class_name in sorted_list and inherits[0] in sorted_list and inherits[1] in sorted_list:
                    sorted_list.append(class_name)
            else:
                print class_name
                raise Exception
                    
    for i in list_of_class_name:
        if not i in sorted_list:
            print "Class has been lost", i    
    assert len(sorted_list) == len(list_of_class_name)

    
    for class_name in sorted_list:
        class_dict = data_dict[class_name]
        write_class(class_name, class_dict, fb)

    fb.close()
    #---------------------------------------------------------------------------
#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_obj_classes(data_dict)

    print "done generating classes"
    
    
    
    
    
    