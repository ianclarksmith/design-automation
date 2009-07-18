import linecache
import os
import string
from util import *

def parse_docs():
    data = {}
    #get all the folders
    all_folders = os.listdir("..\\docs\\RhinoScript")
    
    #list non svn folders
    folders = []
    for folder_name in all_folders:
        if folder_name != ".svn":
            folders.append(folder_name)
            
    #now process all non svn folders
    for folder_name in folders:
    
        data[folder_name]  = {}
        #get all the files
        all_files = os.listdir("..\\docs\\RhinoScript\\" + folder_name)
        #remove svn files
        files = []
        for file in all_files:
            if file != ".svn":
                files.append(file)
        for file in files:
            
            file_name = file[:-4]
            if file_name != folder_name:
                
                
                #get all the lines in the file, ignoring the first line and any subsequent empty lines
                contents = linecache.getlines('..\\docs\\RhinoScript\\%s\\%s' % (folder_name, file))
                contents = contents[1:]
                contents = filter(lambda i: len(i)>1, contents)
                contents = map(lambda i: i.strip(string.whitespace), contents)
                
                #set some things to None so we can do some checks later
                line_num_syntax = None
                line_num_params = None
                line_num_returns = None
                line_num_example = None            
                
                count = 0
                for line in contents:
                    if line==file_name: line_num_help = count
                    if line=="Syntax": line_num_syntax = count
                    if line=="Parameters": line_num_params = count
                    if line=="Returns": line_num_returns = count
                    if line=="Example": line_num_example = count
                    if line=="Also See": line_num_see = count
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
                

                #get the help
                content_help = []
                if (line_num_syntax - line_num_help) > 1:
                    for line_num in range(line_num_help+1, line_num_syntax):
                        content_help.append(contents[line_num])
                content_help = "\n\t\t".join(content_help)

                #get the first line of the syntax
                #TO DO: get all syntax lines
                content_syntax = contents[line_num_syntax + 1]
                
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
                            param_name = param_name[3:]
                            param_prefix = "bln"
                        elif param_name.startswith("int"): 
                            param_name = param_name[3:]
                            param_prefix = "int"
                        elif param_name.startswith("lng"): 
                            param_name = param_name[3:]
                            param_prefix = "lng"
                        elif param_name.startswith("dbl"): 
                            param_name = param_name[3:]
                            param_prefix = "dbl"
                        elif param_name.startswith("str"): 
                            param_name = param_name[3:]
                            param_prefix = "str"
                        elif param_name.startswith("va"): 
                            param_name = param_name[2:]
                            param_prefix = "var"
                        elif param_name.startswith("n"): 
                            param_name = param_name[1:]
                            param_prefix = "int"
                        elif param_name.startswith("arrdbl"): 
                            param_name = param_name[6:]
                            param_prefix = "arr"
                        elif param_name.startswith("arrstr"): 
                            param_name = param_name[6:]
                            param_prefix = "arr"                             
                        elif param_name.startswith("arr"): 
                            param_name = param_name[3:]
                            param_prefix = "arr"
                        #split the next line into the right bits
                        line2 = contents[param_start + 1]
                        line2_word1 = line2[:line2.find(".")].strip()
                        line2_rest = line2[line2.find(".")+1:].strip()
                        line2_word2 = line2_rest[:line2_rest.find(".")].strip()
                        line2_rest = line2_rest[line2_rest.find(".")+1:].strip()
                        #get the help text for the parameter
                        content_param_help = [line2_rest]
                        if (param_end - param_start) > 2:
                            
                            print "long docs:  ", file_name, folder_name
                            
                            for line_num in range(param_start+2, param_end):
                                content_param_help.append(contents[line_num])
                        content_param_help = "\n\t\t".join(content_param_help)
                        #assign parameters
                        param_req = line2_word1
                        param_vb_type = line2_word2
                        content_params.append((param_name, param_req, param_vb_type, param_prefix, content_param_help))
                
                #now get the returns
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
    
    #folder_parent_path
    folder_parent_path = "..\\docs\\gen\\" 
    
    #create init file
    parent_init = open(folder_parent_path + "__init__.py", mode='w')
    
    #write a new help file      
    for folder_name in data:
        
        #write to the init file
        w(parent_init, ("from ", folder_name[:-8].lower(), " import *"), tabs=0, nls=0, nle=1)
        
        #folder path
        folder_path = folder_parent_path + folder_name[:-8].lower() + "\\"
        
        #delete all files in the folder
        all_files = os.listdir(folder_path)
        for file in all_files:
            if file != ".svn":
                os.remove(folder_path + file) 
        
        #create an __init__ file
        folder_init = open(folder_path + "__init__.py", mode='w')
        
        #now recreate all the files
        for file_name in data[folder_name]:
                
            f = open(folder_path + camel_to_underscore(file_name) + '.py', mode='w')
            #import the new file into the init
            w(folder_init, ('from ', camel_to_underscore(file_name), ' import *'), tabs=0, nls=0, nle=1)
            
            w(f, camel_to_underscore(file_name)+' = {', tabs = 0, nls = 0, nle=1)
            
            #folder name
            w(f, ('"class": "', folder_name[:-8], '",'), tabs = 1, nls = 1, nle=0)
            
            #file name
            w(f, ('"method": "', camel_to_underscore(file_name), '",'), tabs = 1, nls = 1, nle=0)
            
            #write help
            w(f, '"doc": """', tabs = 1, nls = 1, nle=1)
            w(f, data[folder_name][file_name]['help'], tabs = 2, nle=1)
            w(f, '""",', tabs = 1, nls = 0, nle=0)
            
            #write syntax
            w(f, '"syntax": """', tabs = 1, nls = 2, nle=1)
            w(f, data[folder_name][file_name]['syntax'], tabs = 2, nle=1)
            w(f, '""",', tabs = 1, nls = 0, nle=0)
            
            #write parameters
            w(f, '"params": {', tabs = 1, nls = 2, nle=0)
            counter = 0
            for param in data[folder_name][file_name]['params']:
                #check if param is required
                optional = "False"
                if param[1] == "Optional":
                    optional = "True"
                w(f, (str(counter), ": {"), tabs = 2, nls=1, nle=1)
                w(f, ('"name": "', camel_to_underscore(param[0]), '",'), tabs=3, nls=0, nle=1)
                w(f, ('"optional": ', optional, ','), tabs=3, nls=0, nle=1)
                w(f, ('"type_vb": "', param[2].lower(), '",'), tabs=3, nls=0, nle=1)
                w(f, ('"type_string": "', param[3], '",'), tabs=3, nls=0, nle=1)
                w(f, '"doc": """', tabs=3, nls=0, nle=1)   
                w(f, param[4], tabs = 2,  nls = 0, nle=1)
                w(f, '"""', tabs = 3, nls = 0, nle=1)
                w(f, ('},'), tabs = 2, nls=0, nle=0)
                counter += 1
            w(f, '},', tabs = 1, nls = 1, nle=0)
            
            #write returns
            w(f, '"returns": {', tabs = 1, nls = 2, nle=0)
            counter = 0
            for return_val in data[folder_name][file_name]['returns']:
                w(f, (str(counter), ": {"), tabs = 2, nls=1, nle=1)
                w(f, ('"type_vb": "', return_val[0], '",'), tabs=3, nls=0, nle=1)
                w(f, ('"doc": "', return_val[1], '"'), tabs=3, nls=0, nle=1)                    
                w(f, ('},'), tabs = 2, nls=0, nle=0)
                counter += 1
            w(f, '}', tabs = 1, nls = 1, nle=2)                

            w(f, '}', tabs = 0, nls = 0, nle=2)
            
            f.close()
        folder_init.close()
    parent_init.close()
    return data

#===============================================================================
# Run the parser
#===============================================================================
if __name__ == '__main__':
    parse_docs()
