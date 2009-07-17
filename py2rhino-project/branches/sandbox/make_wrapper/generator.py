import linecache
import os
import string
from ct  import rhinoscript as ct_rs
from pw32 import  rhinoscript as pw32_rs
import keyword

def parse_docs():
    data = {}
    #get all the folders
    all_folders = os.listdir("..\\docs\\RhinoScript")
    #remove svn folders
    folders = []
    for folder in all_folders:
        if folder != ".svn":
            folders.append(folder)
    #now process all non svn folders
    for folder in folders:
        
        data[folder]  = {}
        #get all the files
        all_files = os.listdir("..\\docs\\RhinoScript\\" + folder)
        #remove svn files
        files = []
        for file in all_files:
            if file != ".svn":
                files.append(file)
        for file in files:
            found_array_param = False
            #print file, " in ", folder
            file_name = file[:-4]
            if file_name != folder:
                
                
                #get all the lines in the file, ignoring the first line and any subsequent empty lines
                contents = linecache.getlines('..\\docs\\RhinoScript\\%s\\%s' % (folder, file))
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
                if (line_num_syntax - line_num_help) > 2:
                    for line_num in range(line_num_help+1, line_num_syntax):
                        content_help.append(contents[line_num])
                content_help = "\n\t\t".join(content_help)

                #get the first line of the syntax
                #TO DO: get all syntax lines
                content_syntax = contents[line_num_syntax + 1]
                
                #now get the parameters
                content_params = []                
                if (line_num_returns - line_num_params) > 2:
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
                            #split the next line into the right bits
                            next_line_word1 = next_line[:next_line.find(".")].strip()
                            next_line_temp = next_line[next_line.find(".")+1:].strip()
                            next_line_word2 = next_line_temp[:next_line_temp.find(".")].strip()
                            next_line_rest = next_line_temp[next_line_temp.find(".")+1:].strip()
                            #get the type from the param name
                            param_name = this_line_words[0].strip()
                            if param_name.startswith("bln"): 
                                param_name = param_name[3:]
                                param_prefix = "bln"
                                param_type_name = "Boolean"
                            elif param_name.startswith("int"): 
                                param_name = param_name[3:]
                                param_prefix = "int"
                                param_type_name = "Integer"
                            elif param_name.startswith("lng"): 
                                param_name = param_name[3:]
                                param_prefix = "lng"
                                param_type_name = "Integer"
                            elif param_name.startswith("dbl"): 
                                param_name = param_name[3:]
                                param_prefix = "dbl"
                                param_type_name = "Double"
                            elif param_name.startswith("str"): 
                                param_name = param_name[3:]
                                param_prefix = "str"
                                param_type_name = "String"
                            elif param_name.startswith("va"): 
                                param_name = param_name[2:]
                                param_prefix = "va"
                                param_type_name = "Array of ?"
                            elif param_name.startswith("n"): 
                                param_name = param_name[1:]
                                param_prefix = "n"
                                param_type_name = "Integer"
                            elif param_name.startswith("arrdbl"): 
                                param_name = param_name[6:]
                                param_type_name = "Array of Doubles"
                                found_array_param = True
                            elif param_name.startswith("arrstr"): 
                                param_name = param_name[6:]
                                param_type_name = "Array of Strings"
                                found_array_param = True                                
                            elif param_name.startswith("arr"): 
                                param_name = param_name[3:]
                                param_type_name = "Array of ?"
                                found_array_param = True
                                #Try to guess array type - warning... this is very error prone
                                if next_line_rest.lower().startswith("an array of string"):
                                    param_prefix = "arrstr"
                                    print "found string array..."
                                elif next_line_rest.lower().startswith("an array of number"):
                                    param_prefix = "arrdbl"
                                    print "found numbers array"
                                elif next_line_rest.lower().startswith("an array of point"):
                                    param_prefix = "arrdbl"
                                    print "found points array"
                                elif next_line_rest.lower().startswith("an array of 3-d point"):
                                    param_prefix = "arrdbl"
                                    print "found points array"  
                                elif next_line_rest.lower().startswith("an array of"):
                                    param_prefix = "arrdbl"
                                    print "***FOUND SOMETHING ELSE***"                                                                                    
                                else:
                                    param_prefix = "arrdbl"

                            #assign parameters
                            param_req = next_line_word1
                            param_vb_type = next_line_word2
                            param_text = next_line_rest
                            content_params.append((param_name, param_req, param_vb_type, param_prefix, param_type_name, param_text))
                
                #now get the returns
                content_returns = []
                if (line_num_example - line_num_returns) > 2:
                    for line_num in range(line_num_returns+1, line_num_example):
                        if contents[line_num] in ("Array", "Null", "Number", "Boolean", "String"):
                            returns_type = contents[line_num]
                            returns_text = contents[line_num+1]
                            content_returns.append([returns_type, returns_text]) 
                    
                #save the data
                data[folder][file_name] = {
                    "help": content_help,
                    "syntax": content_syntax,
                    "params": content_params,
                    "returns": content_returns
                }
                
            if found_array_param:
                print "FOUND ARRAY IN ", file_name, " in ", folder                
    
    #write a new help file      
    for folder in data:
        for file in data[folder]:
                f = open("..\\docs\\gen\\" + folder[:-8] + "\\" + file_name + ".txt", mode='w')
                #write help
                w(f, ["[", file,"]"], nls = 0, nle=2)
                w(f, data[folder][file]['help'], tabs = 1, nle=1)
                
                #write syntax
                w(f, ["[Syntax]"], nls = 0, nle=2)
                w(f, data[folder][file]['syntax'], tabs = 1, nle=1)
                
                #write parameters
                w(f, ["[Parameters]"], nls = 0, nle=2)
                for param in data[folder][file]['params']:
                    w(f, param[0], tabs = 1, nle=1)
                    print param
                    w(f, param, tabs = 1, nle=1)
                    
                f.close()
    return data

def write_classes(folders):
    for folder_name in folders.keys():
        write_class(folder_name, folders[folder_name])

def write_class(folder_name, folder_data):
    #get the names formatted in the right way
    class_file_name = folder_name[:-8].lower()
    class_name = ''.join(map(lambda i: i.capitalize(), class_file_name.split("_")))
    
    #open, write, and close
    f = open("..\\gen\\" + class_file_name + ".py", mode='w')
    write_class_header(class_name, f)
    for file_name in sorted(folder_data.keys()):
        write_class_method(file_name, folder_data[file_name], f)
    f.close()
    
def write_class_header(class_name, f):
    w(f,"# Auto-generated wrapper for Rhino4 RhinoScript functions", nle=2)
    w(f,"import exceptions")
    w(f,"from _utils import *")
    w(f,"from _rhinoscript import IRhinoScript", nle=2)
    w(f,"class %s(IRhinoScript):" % class_name, nle=4)

def write_class_method(file_name, file_data, f):

    #get the names into the right format
    vb_method_name = file_name
    py_method_name = camel_to_underscore(file_name)
    if keyword.iskeyword(py_method_name):
        py_method_name += "_rh"
    vb_params = []
    py_params = []
    if file_data["params"]:
        for param in file_data["params"]:
            vb_params.append(param[0])
            py_param = camel_to_underscore(param[0])
            if keyword.iskeyword(py_param):
                py_param += "_param"
            py_params.append(py_param)
        
    #first check if this is a method with mismatch in parameters
    if not params_match_ct(file_name, file_data):
        w(f, ["def ", py_method_name, "(self):"], tabs=1, nle=1)
        w(f, '"""', tabs=2, nle=2)
        w(f, "METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH", tabs=2, nls=1, nle=2)
        w(f, '"""', tabs=2, nls=1, nle=2)
        w(f, "raise exceptions.NotImplementedError", tabs=2, nle=2)
        return
            
    #create the method signature
    w(f, ["def ", py_method_name, "(self"], tabs=1, nle=0)
    if py_params:
        w(f, [", ", ", ".join(py_params), "):"], tabs=0, nle=1)
    else:
        w(f, "):", tabs=0, nle=1)

    #create the method documentation
    #TODO: add syntax example here
    #TODO: use the py_params format in the doc string
    w(f, '"""', tabs=2, nle=2)    
    w(f, file_data["help"], tabs=2, nle=2)
    if file_data["params"]:
        w(f, "Parameters", tabs=2, nle=2)
        for param in file_data["params"]:
            w(f, [param[0], " : ", param[1],", ", param[2], ", ", param[3], ", ", param[-1]], tabs=2, nle=1)
    else:
        w(f, "No parameters", tabs=2, nle=1)
    if file_data["returns"]:
        w(f, "Returns", tabs=2, nls=1, nle=2)
        for returns in file_data["returns"]:
            w(f, [returns[0], " : ", returns[1]], tabs=2, nle=1)
    else:
        w(f, "No returns", tabs=2, nls=1, nle=2)        
    w(f, '"""', tabs=2, nls=1, nle=2)
    #w(f, "pass", tabs=2, nle=2)
    
    #mapping from type to magic numbers
    #VT_I2 = 2 = signed short
    #VT_I4 = 3 = signed long
    #VT_R4 = 4 = signed float
    #VT_R8 = 5 = signed double  
    type_map = {
        "bln":"VT_BOOL",
        "int":"VT_I2",        
        "lng":"VT_I4",
        "dbl":"VT_R8",
        "str":"VT_BSTR",        
        "arrdbl":"VT_ARRAY + VT_R8",
        "arrstr":"VT_ARRAY + VT_BSTR",       
        "va":"VT_VARIANT",
        "n":"VT_I2"
    }
    
    #figure out the params, adding in flatten for all arrays
    py_params_flattened = []
    if file_data["params"]:
        for param in file_data["params"]:
            py_param = camel_to_underscore(param[0])
            if keyword.iskeyword(py_param):
                py_param += "_param"
            if param[3].startswith("arr"):
                py_param = "flatten(" + py_param + ")"
            py_params_flattened.append(py_param)
    py_params_flattened = ", ".join(py_params_flattened)

    #figure out the magic numbers
    magic_id = get_ct_id_by_name(vb_method_name)
    magic_returns = "(VT_VARIANT, 0)"
    magic_params = []
    for i in file_data["params"]:
        if i[3] in type_map.keys():
            param = "(" + str(type_map[i[3]]) + ", 1)"
        else:
            param = i[3]
            print "ERROR FINDING TYPE: ", i[3], file_name
        magic_params.append(param)
    magic_params = ", ".join(magic_params)
    
    #now write the function    
    magic = str(magic_id) + ", 1, "+magic_returns+", ("+magic_params+",)"
    w(f, ["return self._ApplyTypes_(", magic,", u'",vb_method_name,"', None, ", py_params_flattened, ")"], tabs=2, nle=2)

def pretty_print_data(folder_data):
    space = "    "
    for folder in sorted(folder_data.keys()):
        print folder
        for file_name in sorted(folder_data[folder].keys()):
            print space, file_name
            print space, space, "Help = ", folder_data[folder][file_name]["help"]
            print space, space, "Syntax = ", folder_data[folder][file_name]["syntax"]
            print space, space, "Parameters : "
            counter = 1
            for param in folder_data[folder][file_name]["params"]:
                print space, space, "  ", counter, ") ", param[0], " = ", param[1], param[2], param[3]
                counter += 1
            print space, space, "Returns : "
            counter = 1            
            for return_val in folder_data[folder][file_name]["returns"]: 
                print space, space, "  ", counter, ") ", return_val[0], " = ", return_val[1]
                counter += 1
            
def w(f, text, tabs = 0, nls=0, nle=1):
    if not isinstance(text, list):
        text = [text]
    if tabs != 0:
        tab_str = ["    " * tabs]
        text = tab_str + text
    if nls != 0:
        nls_str = ["\n" * nls]
        text =  nls_str + text          
    if nle != 0:
        nle_str = ["\n" * nle]
        text = text + nle_str
    f.writelines(text)
    
def params_match_ct(file_name, file_data):
    num_ct_params = get_ct_num_params(file_name)
    num_doc_params = len(file_data['params'])
    return num_ct_params == num_doc_params 
    
def compare_with_ct(folder_data):
    count_mis = 0
    count_ok = 0
    for folder_name in folder_data.keys():
        for file_name in folder_data[folder_name]:
            if is_in_ct(file_name):
                num_ct_params = get_ct_num_params(file_name)
                num_doc_params = len(folder_data[folder_name][file_name]['params'])            
                if ( num_doc_params != num_ct_params ):
                    count_mis += 1
                    print "============================================"
                    print "MISMATCH IN PARAMETERS"
                    print file_name + " in " + folder_name
                    print "params from docs files:" 
                    for i in folder_data[folder_name][file_name]['params']:
                        print "\t", i
                    print "params from comtypes file : "
                    for i in get_ct_params(file_name):
                        print "\t", i
                    print "============================================"
                else:
                    count_ok += 1
            else:
                print "MISSING: ", file_name, " in ", folder_name
    
    print "number of mismatches = ", count_mis, " out of ", count_ok
                    
def get_ct_name_by_id(id):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if id == i[2][0]:
            return i[1]
    return None

def get_ct_id_by_name(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if name == i[1]:
            return i[2][0]
    return None

def get_ct_num_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
        if name == i[1]:
            return len(i[-1])
    return None

def get_ct_params(name):
    for i in ct_rs.IRhinoScript.__dict__["_disp_methods_"]:
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
    
def find_methods_mismatch(folder_data):
    print "MISSING METHODS"
    for folder_name in folder_data.keys():
        for file_name in folder_data[folder_name]:
            if not is_in_ct(file_name):
                print "ct \t", file_name, " in ", folder_name
            if not is_in_pw32(file_name):
                print "pw32 \t", file_name, " in ", folder_name

def is_in_pw32(name):
    return name in pw32_rs.IRhinoScript.__dict__.keys()

def is_in_ct(name):
    if get_ct_id_by_name(name) == None: 
        return False
    return True


def camel_to_underscore(name_cc):
    name_us = ""
    #get list of letters
    for i in range(len(name_cc)):
        if (name_cc[i].isupper()):
            name_us += "_"
            name_us += name_cc[i].lower()
        else:
            name_us += name_cc[i]
    #check we are not starting with an underscore
    if name_us.startswith("_"):
        name_us = name_us[1:]
    return name_us


#===============================================================================
# Run
#===============================================================================

data = parse_docs()
find_methods_mismatch(data)
#compare_with_ct(data)
write_classes(data)

#pretty_print_data(data) 


