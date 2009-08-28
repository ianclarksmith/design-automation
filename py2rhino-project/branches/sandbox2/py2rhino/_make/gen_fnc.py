import keyword
from exceptions import Exception
from util import *
from py2rhino._make.data.gen_fnc_in import descriptors as des_fnc

out_folder = "..\\"

#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    
    module_map = {}
    for function_list_name in des_fnc.__dict__.keys():
        if function_list_name.endswith('_methods'):
            #print function_list_name
            function_list = des_fnc.__dict__[function_list_name]
            for module_name in function_list.__dict__.keys():
                if not module_name.startswith('__'):
                    module = function_list.__dict__[module_name]
                    
                    #create an empty dict to store class methods
                    if not module_name in module_map.keys():
                        module_map[module_name] = {}
                    
                    #folder
                    sub_folder_name = module.__dict__["folder"]
                    module_map[module_name]["folder"] = sub_folder_name
                                        
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
def write_modules(data_dict):
    
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
        w(f, ('def ', method_name), tabs=0, nls=1, nle=0)
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
            if len(params) > 0:
                params = ', '.join(params)
                w(f, ('(', params, '):'), tabs=0, nle=1)
            else:
                w(f, '():', tabs=0, nle=1)
        else:
            w(f, '():', tabs=0, nle=1)
        
        #TODO: write the documentation
        w(f, '"""', nls=1, tabs=1)
        w(f, ('For help, look up the Rhinoscript function: ', underscore_to_camel(function_name)), tabs=1)
        w(f, '"""', tabs=1)

        
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
                        w(f, ('if type(',params_name[i],') != list and type(',params_name[i],') != tuple:'), tabs=1)
                        w(f, (params_name[i],' = (',params_name[i],',)'), tabs=2)
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
            w(f, ('return base._rsf.',function_name,'()'), tabs=1)
        elif return_type in simple_types or return_type == 'number':
            w(f, ('return base._rsf.',function_name,'(', args, ')'), tabs=1)
        elif return_type.startswith('array_of') and (return_type[9:] in simple_types or return_type[9:] == 'number'):
            w(f, ('return base._rsf.',function_name,'(', args, ')'), tabs=1)
        else:
            print return_type
            raise Exception('The function returns something very strange')

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
    for module_name in sorted(data_dict.keys()):
    #open the base file
        module_dict = data_dict[module_name]
        sub_folder_name = module_dict['folder']
        if sub_folder_name != None:
            f = open(out_folder + sub_folder_name +'\\'+ module_name + '.py', mode='w')
        else:
            f = open(out_folder + module_name + '.py', mode='w')
        w(f,'# Auto-generated wrapper for Rhino4 RhinoScript functions', nle=2)
        w(f,'import pythoncom')
        w(f,'from py2rhino import _base') 
        
        write_module(module_dict, f)
        f.close()
    #---------------------------------------------------------------------------


#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_modules(data_dict)

    print "done generating modules"
    
    
    
    
    
    