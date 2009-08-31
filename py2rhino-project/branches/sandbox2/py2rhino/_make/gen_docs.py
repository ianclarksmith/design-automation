import keyword
from exceptions import Exception
from util import *
from py2rhino._make.data.gen_obj_in import descriptors as des_obj
from py2rhino._make.data.gen_wrp_in import descriptors as des_wrp
from py2rhino._make.data import parser_out as p2r
out_folder = ".\\data\\gen_docs_out\\"
#===============================================================================
# Get the data from the parser
#===============================================================================
def get_wrp_data_dictionary():
    data_dict = {}
    for function_list_name in des_wrp.__dict__.keys():
        if function_list_name.endswith('_functions'):
            function_list = des_wrp.__dict__[function_list_name]
            data_dict[function_list_name] = {}
            for function_name in function_list.__dict__.keys():
                if not function_name.startswith('__'):
                    function = function_list.__dict__[function_name]
                    data_dict[function_list_name][function_name] = function
    return data_dict

def get_parser_data_dictionary():
    data = {}
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(p2r.__dict__[i], dict):
                data[i] = {}
                mod = p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        #print i, j
                        data[j] = mod.__dict__[j]

    return data
#===============================================================================
# Generate the docs
#===============================================================================


type_map = {
    "va":"list",
    "n":"integer",
    "int":"integer",
    "lng":"integer",    
    "dbl":"float",
    "bln":"boolean",
    "str":"string",
    "number":"number",
    "array_of dbl":"List of float",
    "array_of int":"List of integer",    
    "array_of bln":"List of boolean",
    "array_of str":"List of string",
    "_ObjectRoot":"object",
    "_CurveRoot":"curve object",
    "_SurfaceRoot":"surface object",
    "_MeshRoot":"mesh object"
            }
opt_req_map = {
    "REQ":"Required",
    "OPT":"Optional",
            }
def get_descriptors_data_dictionary(debug=False):
    
    class_map = {}
    for function_list_name in des_obj.__dict__.keys():
        if function_list_name.endswith('_methods'):
            #print function_list_name
            function_list = des_obj.__dict__[function_list_name]
            for class_name in function_list.__dict__.keys():
                if not class_name.startswith('__'):
                    clas = function_list.__dict__[class_name]
                    #print "\t", class_name
                    
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
def write_docs(data_dict, parser_dict):
            
    #---------------------------------------------------------------------------
    def write_class_name(class_name, f):
        w(f,('class ', class_name,'():'), nls=2, nle=2)

    #---------------------------------------------------------------------------
    def write_method(function_name, class_name, method_type, method_dict, parser_dict, f):

        #print function_name, class_name, method_type
        
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
        
        
        
        parser_data = {}
        if function_name in parser_dict.keys():
            parser_data = parser_dict[function_name]
        elif function_name[-1].isdigit():
            parser_data = parser_dict[function_name[:-2]]
        else:
            print "ERROR :", function_name, class_name, method_type
            raise Exception
        
        doc = parser_data['doc_html']

        method_name = method_dict['method_name']
        
        
        w(f,(method_name, ' = """'), tabs=2)
        if method_type == 'CONSTRUCTOR':
            w(f,('Factory method:'), tabs=2)
        w(f,(doc.strip()), tabs=2)
        w(f,('Parameters'), tabs=2, nls=1)
        w(f,('=========='), tabs=2)
        if num_params >0:
            param_counter = 0
            for i in range(num_params):
                if params_type[i] != 'SELF' and not params_hidden[i]:
                    param_counter += 1
                    
                    #get the type string
                    is_object = False
                    type_str = params_type[i]
                    if type_str.startswith('_'):
                        is_object = True
                        type_list = type_str.split('.')
                        type_str = type_list[-1]
                        if type_str.startswith('_'):
                            type_str = type_map[type_str]
                    elif type_str.startswith('array_of _'):
                        is_object = True
                        type_list = type_str.split('.')
                        type_str = type_list[-1]
                        if type_str.startswith('_'):
                            type_str = type_map[type_str]                        
                        type_str = "list of " + type_str
                    else:
                        type_str = type_map[params_type[i]]
                        
                    #get the opt/req string
                    opt_req_str = opt_req_map[params_opt_or_req[i]]
                    
                    #get the doc string from the parser data
                    doc_str = None
                    print parser_data['output_package_name'], function_name, i
                    original_param_name = wrp_dict[parser_data['output_package_name'] + '_functions'][function_name]['function_parameters'][i][0]
                    for parser_param_num in parser_data['params_html'].keys():
                        if parser_data['params_html'][parser_param_num]['py_name'] == original_param_name:
                            doc_str = parser_data['params_html'][parser_param_num]['doc'].strip()
                    if doc_str == None:
                        print params_name[i], parser_data['params_html']
                        print "ERROR: doc string not found for parameter"
                    
                    if is_object:
                        doc_str = doc_str.replace("An array of strings identifying the ", "A list of ")
                        doc_str = doc_str.replace("A string identifying the ", "The ")
                        doc_str = doc_str.replace("An array of object identifier","A list of objects")
                        doc_str = doc_str.replace("An array of object identifiers","A list of objects")
                        
                    doc_str = doc_str.replace("array","list")
                    doc_str = doc_str.replace("null","None")                    
                    
                    w(f,(params_name[i], '  (', type_str,', ', opt_req_str, ') - ', doc_str), tabs = 2)
                    
        if param_counter == 0:
            w(f,'No parameters', tabs = 2)
            
            
        parser_returns = parser_data['returns_html']
        parser_params = parser_data['params_html']
        param_map = {}
        for i in parser_params.keys():
            param_map[parser_params[i]['name']] = parser_params[i]['py_name']
            
        returns_list = method_dict['method_returns']
                    
        w(f,('Returns'), tabs=2, nls=1)
        w(f,('======='), tabs=2)
        if method_type == 'CONSTRUCTOR':
            if returns_list[0].startswith("array_of "):
                w(f,"list of objects - The new objects if successful.", tabs=2)
                w(f,"None - If not successful, or on error.", tabs=2)
            else:
                w(f,"object - The new object if successful.", tabs=2)
                w(f,"None - If not successful, or on error.", tabs=2)
        else:
            if len(parser_returns) == 0:
                w(f,'No returns', tabs=2)
            else:
                for i in parser_returns.keys():
                    
                    #get the return type
                    type_str = parser_returns[i]['type']
                    if type_str == 'string' and returns_list[0].startswith("_"):
                        type_str = 'object'
                    elif type_str == 'array' and returns_list[0].startswith("array_of _"):
                        type_str = 'list of objects'                        
                    elif type_str == 'array':
                        type_str = 'list'
                    elif type_str == 'null':
                        type_str = 'None'
                              
                    #get the return doc string 
                    doc_str = doc_str = parser_returns[i]['doc']
                    doc_str = doc_str.replace("An array","A list")
                    doc_str = doc_str.replace("an array","a list")                    
                    doc_str = doc_str.replace("array","list")
                    doc_str = doc_str.replace("null","None")
                    doc_str = doc_str.replace(" the identifier of "," ")
                    doc_str = doc_str.replace("The identifier of the ","The ")
                    doc_str = doc_str.replace("An array of strings identifying the ", "A list of ")
                    doc_str = doc_str.replace("A string identifying the ", "The ")
                    for i in param_map.keys():
                        doc_str = doc_str.replace(i, param_map[i])
                    
                    
                    
                    w(f,(type_str, ' - ', doc_str), tabs=2)
                
        w(f,('Rhinoscript'), tabs=2, nls=1)
        w(f,('==========="""'), tabs=2)
        

        

    #---------------------------------------------------------------------------
    def write_class(class_name, class_dict, parser_dict, f):
            
        write_class_name(class_name, f)            
        
        #write init
        module_name = camel_to_underscore(class_name) 
        
        #counter
        count = 0       
        
        #write each constructor to the class file
        for function_name in sorted(class_dict['constructors'].keys()):
            method_dict = class_dict['constructors'][function_name]
            count += 1
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CONSTRUCTOR', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'CONSTRUCTOR', method_dict, parser_dict, f)

        #write each method to the class file
        for function_name in sorted(class_dict['methods'].keys()):
            method_dict = class_dict['methods'][function_name]
            count += 1
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'METHOD', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'METHOD', method_dict, parser_dict, f)    

        #write each class method to the class file
        for function_name in sorted(class_dict['class_methods'].keys()):
            method_dict = class_dict['class_methods'][function_name]
            count += 1
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CLASS_METHOD', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'CLASS_METHOD', method_dict,  parser_dict,f)
            
        if count == 0:
            w(f,('pass'), tabs=1)
    #---------------------------------------------------------------------------
    #open the base file
    f = open(out_folder + 'docs_data.py', mode='w')

    for class_name in sorted(data_dict.keys()):
        class_dict = data_dict[class_name]
        write_class(class_name, class_dict,  parser_dict, f)

    f.close()
    #---------------------------------------------------------------------------

#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    parser_dict = get_parser_data_dictionary()
    wrp_dict = get_wrp_data_dictionary()
    print wrp_dict.keys()
    descriptors_dict = get_descriptors_data_dictionary()
    
    write_docs(descriptors_dict, parser_dict)

    print "done generating docs"
    
    
    
    
    
    