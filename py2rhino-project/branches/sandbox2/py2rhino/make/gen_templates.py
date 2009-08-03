from util import *
from py2rhino.make.data import parser_out as p2r
import keyword
in_folder =  ".\\data\\parser_out\\"
out_folder = ".\\data\\gen_templates\\"
#===============================================================================
# Get the data from the parser
#===============================================================================
def get_data_dictionary():
    data = {}
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(p2r.__dict__[i], dict):
                data[i] = {}
                mod = p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        data[i][j] = mod.__dict__[j]

    return data

#===============================================================================
# The method descriptors
#===============================================================================
def write_methods(data_dict):
    counter = 0
    init1 = open(out_folder + 'descriptors_api\\__init__.py', mode='w')
    init2 = open(out_folder + 'descriptors_fnc\\__init__.py', mode='w')    
    init3 = open(out_folder + 'docs\\__init__.py', mode='w')
    
    for module_name in sorted(data_dict.keys()):
        w(init1, ('import ',module_name, '_methods' ), tabs=0, nls=0, nle=1)
        w(init2, ('import ',module_name, '_functions' ), tabs=0, nls=0, nle=1)        
        w(init3, ('import ',module_name, '_docs' ), tabs=0, nls=0, nle=1)
        
        f1 = open(out_folder + 'descriptors_api\\' + module_name +"_methods.py", mode='w')
        f2 = open(out_folder + 'descriptors_fnc\\' + module_name +"_functions.py", mode='w')
        f3 = open(out_folder + 'docs\\' + module_name +"_docs.py", mode='w')        
        
        w(f1, '#The data below will be used to generate the Rhinoscript function wrappers', tabs=0, nls=0, nle=2)
        w(f1, '#Errors can be fixed by hand here', tabs=0, nls=0, nle=2)
        
        w(f2, '#The data below will be used to generate the Rhinoscript api', tabs=0, nls=0, nle=2)
        w(f2, '#Errors can be fixed by hand here', tabs=0, nls=0, nle=2)
        
        for method_name in sorted(data_dict[module_name].keys()):
            #get the method dict
            method_dict = data_dict[module_name][method_name]
            
            #get the location where this method will be created
            api_location = underscore_to_camel(method_dict['input_folder_name'][:-8])
            fnc_location = method_dict['input_folder_name'][:-8].lower()            
            fnc_com_id = method_dict['id_com']
            fnc_vb_name = method_dict['input_file_name']            
            
            #check the number of parameters for html and com
            num_html_params = len(method_dict['params_html'])
            num_com_params = len(method_dict['params_com'])
            num_syntax_examples = len(method_dict['syntax_html'])
            
            #if there is a mismatch, then create one method for each syntax example
            if num_html_params != num_com_params:
                for method_num in range(num_syntax_examples):
                    params_data = get_params_data(method_dict, method_num)
                    returns_data = get_returns_data(method_dict)
                    write_descriptor_for_api_methods(api_location, params_data, returns_data, f1)
                    write_descriptor_for_functions(fnc_location, fnc_com_id, fnc_vb_name, params_data, returns_data, f2)
            else:
                params_data = get_params_data(method_dict, -1)
                returns_data = get_returns_data(method_dict)
                write_descriptor_for_api_methods(api_location, params_data, returns_data, f1)
                write_descriptor_for_functions(fnc_location, fnc_com_id, fnc_vb_name, params_data, returns_data, f2)

        #close the files
        f1.close()
        f2.close()
        f3.close()
    init1.close()
    init2.close()
    init3.close()    

#------------------------------------------------------------------------------ 
def get_params_data(method_dict, method_num):
    
    #get the method name in py format
    py_method_name = method_dict['output_module_name']
    if method_num > 0:
        py_method_name = py_method_name + '_' + str(method_num + 1)
    if keyword.iskeyword(py_method_name):
        py_method_name += '_'
    
    #get the param data into a set of lists for easy access
    params_name = []
    params_type = []
    params_opt_or_req = []
    params_doc = []
 
    if len(method_dict['params_html']) > 0:
        for param_num in method_dict['params_html'].keys():
            param_dict = method_dict['params_html'][param_num]
            
            #get the right syntax example
            if (method_num == -1) or (param_dict['name'] in method_dict['syntax_html'][method_num]):
                
                #create a name for the parameter
                param_py_name = param_dict['py_name']
                if keyword.iskeyword(param_py_name):
                    param_py_name += "_"

                #add data to the lists
                params_name.append(param_py_name)
                params_type.append(param_dict['name_prefix'])
                params_opt_or_req.append( param_dict['opt_or_req'])
                params_doc.append(param_dict['doc'])
    
    return (py_method_name, params_name, params_type, params_opt_or_req, params_doc)
#------------------------------------------------------------------------------ 
def get_returns_data(method_dict):
    
    #get the returns data into two lists
    returns_type = []
    returns_doc = []
    
    returns_dict = method_dict['returns_html']
    if returns_dict:
        for returns_num in returns_dict.keys():
            
            #get the data
            type = returns_dict[returns_num]['type']
            doc = returns_dict[returns_num]['doc']
            
            #add data to the lists
            returns_type.append(type)
            returns_doc.append(doc)
            
    return (returns_type, returns_doc)   
#------------------------------------------------------------------------------ 
def write_descriptor_for_api_methods(location, params_data, returns_data, f):
    #get the data
    py_method_name, params_name, params_type, params_opt_or_req, params_doc = params_data
    returns_type, returns_doc = returns_data
    num_params = len(params_name)
    num_returns = len(returns_type)
    
    #write key data
    w(f, (py_method_name, ' = {'), tabs=0, nls=0, nle=1)
    w(f, ('"method_location": "', location, '",'), tabs=1, nls=0, nle=1)
    w(f, ('"method_type": "METHOD",'), tabs=1, nls=0, nle=1)             
    w(f, ('"method_name": "', py_method_name, '",'), tabs=1, nls=0, nle=1)

    #write the parameters
    w(f, ('"method_parameters": ('), tabs=1, nls=0, nle=0) 
    write_parameters(params_name, params_type, params_opt_or_req, f)
        
    #write the returns returns
    w(f, ('"method_returns": ('), tabs=1, nls=0, nle=0) 
    write_returns(returns_type, f)
    
    
    w(f, '}', tabs=1, nls=0, nle=1)
#------------------------------------------------------------------------------ 
def write_descriptor_for_functions(location, id, vb_name, params_data, returns_data, f):
    
    #get the data
    py_method_name, params_name, params_type, params_opt_or_req, params_doc = params_data
    returns_type, returns_doc = returns_data
    num_params = len(params_name)
    num_returns = len(returns_type)
    
    #write key data
    w(f, (py_method_name, ' = {'), tabs=0, nls=0, nle=1)
    w(f, ('"function_location": "', location , '",'), tabs=1, nls=0, nle=1)
    w(f, ('"function_com_id": ', str(id), ','), tabs=1, nls=0, nle=1)
    w(f, ('"function_vb_name": "', vb_name, '",'), tabs=1, nls=0, nle=1)
    w(f, ('"function_name": "', py_method_name, '",'), tabs=1, nls=0, nle=1)

    #write the parameters
    w(f, ('"function_parameters": ('), tabs=1, nls=0, nle=0) 
    write_parameters(params_name, params_type, params_opt_or_req, f)
        
    #write the returns returns
    w(f, ('"function_returns": ('), tabs=1, nls=0, nle=0) 
    write_returns(returns_type, f)
    
    w(f, '}', tabs=1, nls=0, nle=1)
#------------------------------------------------------------------------------ 
def write_parameters(params_name, params_type, params_opt_or_req, f):
    num_params = len(params_name)
    if num_params > 0:
        params_list = []
        for param_num in range(num_params):
            py_name = params_name[param_num]
            type_string = get_type_string(params_type[param_num])
            opt_or_req = params_opt_or_req[param_num][:3].upper()
            params_list.append('("' + py_name +'","'+ type_string +'","'+ opt_or_req + '")')
        params_list =  ','.join(params_list)
        if num_params == 1:
            params_list += ','
        w(f, params_list, tabs=0, nls=0, nle=0) 
    w(f, '),', tabs=0, nls=0, nle=1)
#------------------------------------------------------------------------------ 
def write_returns(returns_type, f):
    num_returns = len(returns_type)
    if num_returns > 0:
        returns_list = []
        for returns_num in range(num_returns):
            type_string = returns_type[returns_num]
            returns_list.append('"' + type_string + '"')
        returns_list =  ','.join(returns_list)
        if num_returns == 1:
            returns_list += ','        
        w(f, returns_list, tabs=0, nls=0, nle=0) 
    w(f, ')', tabs=0, nls=0, nle=1)   
#------------------------------------------------------------------------------ 
def write_method_docs(location, method_data, f):
    pass #TODO: add some docs somewhere
#------------------------------------------------------------------------------ 
def get_type_string(str):
    if str.startswith("arr_of_"):
        str = 'array_of ' + str[7:]
    return str
#===============================================================================
# Run 
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_methods(data_dict)
    
    print 'done'