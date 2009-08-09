import keyword
from exceptions import Exception
from util import *
from py2rhino.make.data import tmp as des_obj
from py2rhino.make.data import parser_out as p2r
out_folder = ".\\data\\gen_docs_out\\"
#===============================================================================
# Get the data from the parser
#===============================================================================
def get_parser_data_dictionary():
    data = {}
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(p2r.__dict__[i], dict):
                data[i] = {}
                mod = p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        print i, j
                        data[j] = mod.__dict__[j]

    return data
#===============================================================================
# Run some checks
#===============================================================================
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
        returns = parser_data['returns_html']
        
        
        method_name = method_dict['method_name']
        
        w(f,(method_name, ' = """'), tabs=1)
        if method_type == 'CONSTRUCTOR':
            w(f,('Factory method:'), tabs=1)
        w(f,(doc.strip()), tabs=1)
        w(f,('Parameters'), tabs=1)
        w(f,('=========='), tabs=1)
        if num_params > 0:
            for i in range(num_params):
                if params_type[i] != 'SELF' and not params_hidden[i]:
                    w(f,('C{', params_name[i],'}', '(', params_type[i],', ', params_opt_or_req[i], ') - ', parser_data['params_html'][i]['doc'].strip()), tabs = 1)
        w(f,('Returns'), tabs=1)
        w(f,('======='), tabs=1)
        if len(returns) != 0:
            for i in returns.keys():
                w(f,(returns[i]['type'], ' - ', returns[i]['doc']), tabs=1)
                
            
        w(f,('"""'), tabs=1)
        

    #---------------------------------------------------------------------------
    def write_class(class_name, class_dict, parser_dict, f):
            
        write_class_name(class_name, f)            
        
        #write init
        module_name = camel_to_underscore(class_name)        
        
        #write each constructor to the class file
        for function_name in sorted(class_dict['constructors'].keys()):
            method_dict = class_dict['constructors'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CONSTRUCTOR', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'CONSTRUCTOR', method_dict, parser_dict, f)

        #write each method to the class file
        for function_name in sorted(class_dict['methods'].keys()):
            method_dict = class_dict['methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'METHOD', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'METHOD', method_dict, parser_dict, f)    

        #write each class method to the class file
        for function_name in sorted(class_dict['class_methods'].keys()):
            method_dict = class_dict['class_methods'][function_name]
            if 0 in method_dict.keys():
                for i in method_dict.keys():
                    write_method(function_name, class_name, 'CLASS_METHOD', method_dict[i], parser_dict, f)
            else:
                write_method(function_name, class_name, 'CLASS_METHOD', method_dict,  parser_dict,f)
            
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
    descriptors_dict = get_descriptors_data_dictionary()
    
    write_docs(descriptors_dict, parser_dict)

    print "done generating docs"
    
    
    
    
    
    