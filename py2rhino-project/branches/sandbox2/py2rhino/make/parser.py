import linecache
import keyword
import os
import string
from util import * #@UnusedWildImport

from py2rhino.make.data.parser_in.gen_comtypes import rhinoscript as ct_rs
from py2rhino.make.data.parser_in.functions_data import array_types_updated as types

#file paths
in_folder = ".\\data\\parser_in\\gen_html\\supported\\"
out_folder = ".\\data\\parser_out\\"

#===============================================================================
# The main function to parse txt files generated from html
#===============================================================================

def parse_docs():
    data = {}
    #get all the folders for the html files
    all_folders = os.listdir(in_folder)
    
    #list non svn folders
    folders = []
    for folder_name in all_folders:
        if folder_name != ".svn":
            folders.append(folder_name)
            
    #now process all non svn folders
    for folder_name in folders:
    
        data[folder_name]  = {}
        #get all the files
        all_files = os.listdir(in_folder + folder_name)
        #remove svn files
        non_svn_files = []
        for file in all_files:
            if file != ".svn":
                non_svn_files.append(file)
                
        #now start parsing
        for file in non_svn_files:
            
            file_name = file[:-4]
            if file_name != folder_name:
                
                #get all the lines in the file, ignoring the first line and any subsequent empty lines
                contents = linecache.getlines(in_folder + folder_name +"\\"+ file)
                contents = contents[1:]
                contents = filter(lambda i: len(i)>1, contents)
                contents = map(lambda i: i.strip(string.whitespace), contents)
                
                #debug 
                """
                ct = 0
                for i in contents:
                    print ct, " ", i
                    ct += 1 """
                
                #set some things to None so we can do some checks later
                line_num_help = None
                line_num_syntax = None
                line_num_params = None
                line_num_returns = None
                line_num_example = None
                line_num_see = None   
                
                count = 0
                for line in contents:
                    if (line_num_help == None) and line==file_name: line_num_help = count
                    if (line_num_syntax == None) and line=="Syntax": line_num_syntax = count
                    if (line_num_params == None) and line=="Parameters": line_num_params = count
                    if (line_num_returns == None) and line=="Returns": line_num_returns = count
                    if (line_num_example == None) and line=="Example": line_num_example = count
                    if (line_num_see == None) and line=="Also See": line_num_see = count
                    count += 1
                
                #do some checks
                assert line_num_help != None
                assert line_num_syntax != None
                assert line_num_params != None
                assert line_num_returns != None
                assert line_num_example != None
                assert contents[line_num_help] == file_name
                assert contents[line_num_syntax] == "Syntax"
                assert contents[line_num_params] == "Parameters"
                assert contents[line_num_returns] == "Returns"
                assert contents[line_num_example] == "Example"
                assert line_num_help < line_num_syntax
                assert line_num_syntax < line_num_params
                assert line_num_params < line_num_returns                                
                assert line_num_returns < line_num_example              
                
                
                
                #get the help
                content_help = []
                if (line_num_syntax - line_num_help) > 1:
                    for line_num in range(line_num_help+1, line_num_syntax):
                        content_help.append(contents[line_num])
                content_help = "\n\t\t".join(content_help)

                #get the first line of the syntax
                content_syntax = contents[line_num_syntax + 1]
                content_syntax = []
                if (line_num_params - line_num_syntax) > 1:
                    for line_num in range(line_num_syntax+1, line_num_params):
                        assert contents[line_num].startswith('Rhino.')
                        #strip out [ and ]
                        line = filter(lambda i: (i!='[' and i!=']'), contents[line_num])
                        if line.count('(') == 1:
                            start_of_args = line.index('(')
                            end_of_args = line.index(')')
                            args = line[start_of_args+1: end_of_args]
                            args = args.split(',')
                            args = map(lambda i: i.strip(), args)
                            content_syntax.append(args)
                        
                
                #now get the parameters
                content_params = []                
                if (line_num_returns - line_num_params) > 2:
                    line_num_each_param = []
                    
                    #get the line numbers for each parameter
                    for line_num in range(line_num_params+1, line_num_returns):
                        #check is this line is a single word (i.e. the name of the param)
                        this_line_words = contents[line_num].split()
                        is_word = False
                        if (len(this_line_words) == 1) and (not this_line_words[0].isdigit()) and this_line_words[0] != "Array":
                            is_word = True
                        #check is this line starts with either 'Required' or 'Optional'
                        next_line = contents[line_num + 1]
                        has_flag = False
                        if (next_line.startswith("Required") or next_line.startswith("Optional")):
                            has_flag = True
                        if is_word and has_flag:
                            line_num_each_param.append(line_num)
                    
                    #get the values for each parameter
                    for param_num in range(len(line_num_each_param)):
                        #get the start line
                        param_start = line_num_each_param[param_num]
                        #get the end line
                        if param_num == len(line_num_each_param) - 1:
                            param_end = line_num_returns - 1
                        else:
                            param_end = line_num_each_param[param_num + 1] - 1
                        #get the type from the param name
                        param_name = contents[param_start].strip()
                        
                        if param_name.startswith("bln"): 
                            param_main = param_name[3:]
                            param_prefix = "bln"
                        elif param_name.startswith("int"): 
                            param_main = param_name[3:]
                            param_prefix = "int"
                        elif param_name.startswith("lng"): 
                            param_main = param_name[3:]
                            param_prefix = "lng"
                        elif param_name.startswith("dbl"): 
                            param_main = param_name[3:]
                            param_prefix = "dbl"
                        elif param_name.startswith("str"): 
                            param_main = param_name[3:]
                            param_prefix = "str"
                        elif param_name.startswith("va"): 
                            param_main = param_name[2:]
                            param_prefix = "va"
                        elif param_name.startswith("n"): 
                            param_main = param_name[1:]
                            param_prefix = "n"
                        elif param_name.startswith("arr"): 
                            param_main = param_name[3:]
                            param_prefix = "arr"
                        else:
                            print "Prefix is missing", file_name, folder_name
                            param_main = param_name
                            param_prefix = 'none'
                        #get the python version of the name
                        param_py_name = camel_to_underscore(param_main)
                        #split the next line into the right bits
                        line2 = contents[param_start + 1]
                        line2_word1 = line2[:line2.find(".")].strip()
                        line2_rest = line2[line2.find(".")+1:].strip()
                        line2_word2 = line2_rest[:line2_rest.find(".")].strip()
                        line2_rest = line2_rest[line2_rest.find(".")+1:].strip()
                        #get the help text for the parameter
                        content_param_help = [line2_rest]
                        if (param_end - param_start) > 2:
                            for line_num in range(param_start+2, param_end):
                                content_param_help.append(contents[line_num])
                        content_param_help = "\n\t\t".join(content_param_help)
                        #assign parameters
                        param_req = line2_word1
                        param_vb_type = line2_word2
                        content_params.append({
                                               'name':param_name, 
                                               'py_name':param_py_name,
                                               'opt_or_req':param_req, 
                                               'type':param_vb_type, 
                                               'name_prefix':param_prefix, 
                                               'name_main':param_main, 
                                               'doc':content_param_help})
                
                #now check for duplicate parameters, e.g strObject and arrObjects
                num_com_params = get_com_num_params(file_name)
                num_html_params = len(content_params)
                #print num_html_params, num_com_params
                if num_html_params>num_com_params:
                    list_of_param_names = map(lambda i: i['name_main'], content_params)
                    tmp_params = []
                    for param in content_params:
                        if not (((param['name_main'] + 's') in list_of_param_names) or  
                            ((param['name_main'] + 'es') in list_of_param_names)):
                            tmp_params.append(param)
                    content_params = tmp_params         
                
                #now check to see if there are any changes specified in the types file
                module_name = folder_name[:-8].lower() #TODO: fix this naming - this is getting messy
                method_name = camel_to_underscore(file_name)
                module_methods = types.__dict__[module_name][0] #@UndefinedVariable
                if method_name in module_methods.keys():
                    for param in content_params:
                        #print param
                        #print module_methods[method_name]
                        param['name_prefix'] = module_methods[method_name][param['py_name']]
                            
                #now get the returns
                #TODO: get the full test - not just the first line
                content_returns = []
                if (line_num_example - line_num_returns) > 2:
                    for line_num in range(line_num_returns+1, line_num_example):
                        if contents[line_num] in ("Array", "Null", "Number", "Boolean", "String"):
                            returns_type = contents[line_num]
                            returns_text = contents[line_num+1]
                            content_returns.append([returns_type, returns_text]) 
                    
                #save the data
                data[folder_name][file_name] = {
                    "help": content_help,
                    "syntax": content_syntax,
                    "params": content_params,
                    "returns": content_returns
                }             
    return data

#===============================================================================
# Some functions to extract data from the comtypes generated file
#===============================================================================

def get_com_name_by_id(id):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]: #@UndefinedVariable
        if id == i[2][0]:
            return i[1]
    return None

def get_com_id_by_name(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]: #@UndefinedVariable
        if name == i[1]:
            return i[2][0]
    return None

def get_com_num_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]: #@UndefinedVariable
        if name == i[1]:
            return len(i[-1])
    return None

def get_com_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]: #@UndefinedVariable
        if name == i[1]:
            params = []
            for j in i[-1]:
                if j[0] == []:
                    flag = "Required"
                else:
                    flag = "Optional"
                params.append((j[2], flag, j[1].__name__))
            return params
    return None

def get_com_returns(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]: #@UndefinedVariable
        if name == i[1]:
            return i[3].__name__
    return None

#===============================================================================
# The function to write one file for each rhino method
#===============================================================================

def write_modules(data):
    #create init file
    out_folder_init = open(out_folder + "__init__.py", mode='w')
    
    #write a new help file      
    for folder_name in data:
        #create the name for the package to be created
        pack_name = folder_name[:-8].lower()
        pack_path = out_folder + pack_name + "\\"
        #create the package folder if it does not exist
        if not os.path.isdir(pack_path):
            os.mkdir(pack_path)
        #write to the main init file to inport this package
        w(out_folder_init, ("from ", pack_name, " import *"), tabs=0, nls=0, nle=1)
        #delete all files in the package folder
        all_files = os.listdir(pack_path)
        for file in all_files:
            if file != ".svn":
                os.remove(pack_path + file) 
        #create an __init__ file in the package folder
        pack_init = open(pack_path + "__init__.py", mode='w')
        
        #now create all the files in the package folder
        for file_name in data[folder_name]:
            
            #create the file for the module
            mod_name = camel_to_underscore(file_name)
            if keyword.iskeyword(mod_name):
                mod_name = mod_name + "_"
            f = open(pack_path + mod_name + '.py', mode='w')
            #import the new module into the init
            w(pack_init, ('from ', mod_name, ' import *'), tabs=0, nls=0, nle=1)
            
            #===============================================
            #Start writing the data to the file
            w(f, mod_name+' = {', tabs = 0, nls = 0, nle=0)
            #write folder name where the text file was douns
            w(f, ('"input_folder_name": "', folder_name, '",'), tabs = 1, nls = 1, nle=0)         
            #write file name
            w(f, ('"input_file_name": "', file_name, '",'), tabs = 1, nls = 1, nle=0)            
            #write the name of the package this file is in
            w(f, ('"output_package_name": "', pack_name, '",'), tabs = 1, nls = 1, nle=0)         
            #write the name of this file
            w(f, ('"output_module_name": "', mod_name, '",'), tabs = 1, nls = 1, nle=0)            

            #write help
            w(f, '"doc_html": """', tabs = 1, nls = 2, nle=1)
            w(f, data[folder_name][file_name]['help'], tabs = 2, nle=1)
            w(f, '""",', tabs = 1, nls = 0, nle=0)
            
            #write syntax
            w(f, '"syntax_html": {', tabs = 1, nls = 2, nle=1)
            sig_num = 0
            
            for signature in data[folder_name][file_name]['syntax']:
                #sig_strs = map(lambda i:str(i), signature)
                w(f, (str(sig_num), ': ('), tabs = 2, nle=0)
                if data[folder_name][file_name]['params']:
                    w(f, ('"','", "'.join(signature), '"'), tabs = 0, nle=0)
                w(f, '),', tabs = 0, nle=1)
                sig_num += 1
            w(f, '},', tabs = 1, nls = 0, nle=0)
            
            #write parameters extracted from html docs
            w(f, '"params_html": {', tabs = 1, nls = 2, nle=0)
            counter = 0
            html_params = data[folder_name][file_name]['params']
            for param in html_params:
                #check if param is required
                w(f, (str(counter), ": {"), tabs = 2, nls=1, nle=1)
                w(f, ('"name": "', param['name'], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"py_name": "', param['py_name'], '",'), tabs=3, nls=0, nle=1)                
                w(f, ('"opt_or_req": "', param['opt_or_req'], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"type": "', param['type'], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"name_prefix": "', param['name_prefix'], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"name_main": "', param['name_main'], '",'), tabs=3, nls=0, nle=1)
                w(f, '"doc": """', tabs=3, nls=0, nle=1)   
                w(f, param['doc'], tabs = 2,  nls = 0, nle=1)
                w(f, '"""', tabs = 3, nls = 0, nle=1)
                w(f, ('},'), tabs = 2, nls=0, nle=0)
                counter += 1
            w(f, '},', tabs = 1, nls = 1, nle=0)
            
            #write returns extracted from html docs
            w(f, '"returns_html": {', tabs = 1, nls = 2, nle=0)
            counter = 0
            for return_val in data[folder_name][file_name]['returns']:
                w(f, (str(counter), ": {"), tabs = 2, nls=1, nle=1)
                w(f, ('"type": "', return_val[0].lower(), '",'), tabs=3, nls=0, nle=1)
                w(f, ('"doc": "', return_val[1], '"'), tabs=3, nls=0, nle=1)                    
                w(f, ('},'), tabs = 2, nls=0, nle=0)
                counter += 1
            w(f, '},', tabs = 1, nls = 1, nle=0)
            
            #write id extracted from com interface (via comtypes)
            com_id = get_com_id_by_name(file_name)
            w(f, ('"id_com": ', str(com_id), ','), tabs = 1, nls = 2, nle=0)
            
            #write params extracted from com interface (via comtypes)
            w(f, '"params_com": {', tabs = 1, nls = 2, nle=0)
            counter = 0
            com_params = get_com_params(file_name)
            for param in com_params:
                #check if param is required              
                w(f, (str(counter), ": {"), tabs = 2, nls=1, nle=1)
                w(f, ('"name": "', param[0], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"opt_or_req": "', param[1], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"type": "', param[2], '",'), tabs=3, nls=0, nle=1)
                w(f, ('},'), tabs = 2, nls=0, nle=0)
                counter += 1
            w(f, '},', tabs = 1, nls = 1, nle=0)
            #write returns extracted from com interface (via comtypes)
            com_returns = get_com_returns(file_name)
            w(f, ('"returns_com": "', com_returns, '",'), tabs = 1, nls = 2, nle=2)            

            #the end
            w(f, '}', tabs = 0, nls = 0, nle=2)
            #===============================================
            
            f.close()
        pack_init.close()
    out_folder_init.close()


#===============================================================================
# Run the parser and write the modules
#===============================================================================
if __name__ == '__main__':
    data = parse_docs()
    write_modules(data)
    print "done"
