import keyword
from exceptions import Exception
from util import *
from py2rhino.make.data.gen_fnc_in import descriptors as des_obj

out_folder = "..\\"

#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    
    print des_obj.__dict__.keys()
    
    module_map = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            #print function_list_name
            function_list = des_obj.__dict__[function_list_name]
            for module_name in function_list.__dict__.keys():
                if not module_name.startswith('__'):
                    module = function_list.__dict__[module_name]
                    
                    #create an empty dict to store class methods
                    if not module_name in module_map.keys():
                        module_map[module_name] = {}
                    
                    #==============================================================
                    #functions
                    if "functions" in module_map[module_name].keys():
                        functions = module_map[module_name]["functions"]
                    else:                    
                        functions = {}
                    if "Functions" in module.__dict__.keys():
                        for function_name in module.__dict__["Functions"].__dict__.keys():
                            if not function_name.startswith("__"):
                                functions[function_name] = module.__dict__["Functions"].__dict__[function_name]
                         
                    #add the methods
                    module_map[module_name]["functions"] = functions

    return module_map


#===============================================================================
# Write the module
#===============================================================================
def write_function_module(data_dict):
    


        
    #---------------------------------------------------------------------------
    def write_function(function_name, method_dict, f):
        
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
                
            
        #create the function signature
        method_name = method_dict['method_name']
        w(f, ('def ', method_name), tabs=1, nls=1, nle=0)
        if num_params > 0:
            params = []
            for i in range(num_params):
                param_str = ''
                if params_hidden[i]:
                    pass #skip the hidden parameters
                else:
                    param_str = params_name[i]
                    if params_opt_or_req[i] == 'OPT':
                        param_str = param_str + '=pythoncom.Empty'
                    params.append(param_str)

        
        #TODO: write the documentation
        w(f, '"""', tabs=2)
        w(f, ('For help, look up the Rhinoscript function: ', underscore_to_camel(function_name)), tabs=2)
        w(f, '"""', tabs=2)

        
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
        
        if return_type == None:
            w(f, ('return _rsf.',function_name,'()'), tabs=2)
        elif return_type in simple_types or return_type == 'number':
            w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2)
        elif return_type.startswith('array_of') and return_type[9:] in simple_types or return_type[9:] == 'number':
            w(f, ('return _rsf.',function_name,'(', args, ')'), tabs=2)
        
            return_class_name = return_type.split('.')[-1]
            if return_class_name.startswith('_'):
                w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return p2r._util.wrap(_rhino_id)'), tabs=3)
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3)
            else:
                w(f, ('_rhino_id = _rsf.',function_name,'(', args, ')'), tabs=2)
                w(f, ('if _rhino_id:'), tabs=2)
                w(f, ('return p2r.obj.', return_class_name, '(_rhino_id)'), tabs=3)#TODO:this needs more work
                w(f, ('else:'), tabs=2)
                w(f, ('return None'), tabs=3) 
        elif return_type.startswith('array_of _Object') or return_type.startswith('array_of _Entity'):
            return_class_name = return_type[9:].split('.')[-1]
            if return_class_name.startswith('_') and return_class_name.endswith('Root'):
                w(f, ('_rhino_ids = _rsf.',function_name,'(', args, ')'), tabs=2)
                w(f, ('return map(lambda i: self._class(i), _rhino_ids)'), tabs=2, nle=1)#TODO:this needs more work
            elif return_class_name.startswith('_'):
                w(f, ('_rhino_ids = _rsf.',function_name,'(', args, ')'), tabs=2)
                w(f, ('return map(lambda i: p2r._util.wrap(i), _rhino_ids)'), tabs=2, nle=1)
            else:
                w(f, ('_rhino_ids = _rsf.',function_name,'(', args, ')'), tabs=2)
                w(f, ('return map(lambda i: p2r.obj.'+return_class_name+'(i), _rhino_ids)'), tabs=2, nle=1)#TODO:this needs more work
        else:
            raise Exception('The method returns something very strange')

            

    #---------------------------------------------------------------------------
    def write_module(module_dict, f):          
         
        #write each function to the  file
        for function_name in sorted(module_dict['functions'].keys()):
            method_dict = module_dict['functions'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_function(function_name, method_dict[i], f)
            else:
                write_function(function_name, method_dict, f)

    #---------------------------------------------------------------------------

    list_of_modules = []
    for module_name in sorted(data_dict.keys()):
        list_of_modules.append(module_name)
    
    for module_name in list_of_modules:
    #open the base file
        f = open(out_folder + '_rhinoscript_classes.py', mode='w')

        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import pythoncom')
        w(f,'from exceptions import Exception')
        w(f,'from py2rhino import _util')   
        
        #write the global _rsf variable and set it to None    
        w(f,'_rsf = None', nls=2)           
        
        module_dict = data_dict[module_name]
        write_module(module_dict, f)
        f.close()
    #---------------------------------------------------------------------------


#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_rhinoscript_functions(data_dict)

    print "done generating classes"
    
    
    
    
    
    