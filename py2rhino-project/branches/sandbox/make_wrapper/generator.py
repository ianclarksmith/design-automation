import linecache
import os
import string
from ct  import rhinoscript as ct_rs
from pw32 import  rhinoscript as pw32_rs

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
            #print file, " in ", folder
            file_name = file[:-4]
            if file_name != folder:
                contents = linecache.getlines('..\\docs\\RhinoScript\\%s\\%s' % (folder, file))
                contents = filter(lambda i: len(i)>1, contents)
                contents = map(lambda i: i.strip(string.whitespace), contents)
                #set some things to None so we can do some checks later
                line_num_syntax = None
                line_num_params = None
                line_num_returns = None
                line_num_example = None            
                
                count = 0
                for line in contents:
                    if line=="Syntax": line_num_syntax = count
                    if line=="Parameters": line_num_params = count
                    if line=="Returns": line_num_returns = count
                    if line=="Example": line_num_example = count
                    if line=="Also See": line_num_see = count
                    count += 1
                
                #do some checks
                assert line_num_syntax != None
                assert line_num_params != None
                assert line_num_returns != None
                assert line_num_example != None
                assert contents[line_num_syntax] == "Syntax"
                assert contents[line_num_params] == "Parameters"
                assert contents[line_num_returns] == "Returns"
                assert contents[line_num_example] == "Example"
                
                #get the simple stuff
                content_help = contents[line_num_syntax - 1]
                content_syntax = contents[line_num_syntax + 1]
                
                #now get the parameters
                content_params = []                
                if (line_num_returns - line_num_params) > 2:
                    for line_num in range(line_num_params+1, line_num_returns):
                        #check is this line is a single word (i.e. the name of the param)
                        this_line_words = contents[line_num].split()
                        is_word = False
                        if (len(this_line_words) == 1) and (not this_line_words[0].isdigit()):
                            is_word = True
                        #check is this line starts with either 'Required' or 'Optional'
                        next_line = contents[line_num + 1]
                        has_flag = False
                        if (next_line.startswith("Required") or next_line.startswith("Optional")):
                            has_flag = True
                        if is_word and has_flag:
                            next_line_phrases = next_line.split(".")
                            param_name = this_line_words[0].strip()
                            param_req = next_line_phrases[0].strip()
                            param_type = next_line_phrases[1].strip()
                            param_text = next_line_phrases[2].strip()
                            content_params.append((param_name, param_req, param_type, param_text))
                
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
    w(f,"# Auto-generated wrapper for Rhino4 RhinoScript functions")
    w(f,"import win32com.client.CLSIDToClass, pythoncom")
    w(f,"import win32com.client.util")
    w(f,"from pywintypes import IID")
    w(f,"from win32com.client import Dispatch")
    w(f,"from win32com.client import DispatchBaseClass")
    w(f,"class %s(DispatchBaseClass):" % class_name, nle=4)

def write_class_method(file_name, file_data, f):
    #get the names into the right format
    #TODO: underscores in py naming
    vb_method_name = file_name
    py_method_name = file_name.lower()
    vb_params = []
    py_params = []
    if file_data["params"]:
        for param in file_data["params"]:
            vb_params.append(param[0])
            py_params.append(param[0].lower())
            
    #create the method signature
    w(f, ["def ", py_method_name, "(self, ", ", ".join(py_params), "):"], tabs=1, nle=1)

    #create the method documentation
    #TODO: add syntax example here
    #TODO: use the py_params format in the doc string
    w(f, '"""', tabs=2, nle=2)    
    w(f, file_data["help"], tabs=2, nle=2)
    if file_data["params"]:
        w(f, "Parameters", tabs=2, nle=2)
        for param in file_data["params"]:
            w(f, [param[0], " : ", param[1],", ", param[2], ", ", param[3]], tabs=2, nle=1)
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
    
    #now call the function
    #TODO: figure out the magic numbers
    magic_numbers = "id, 1, (returns), (params)" #for example: 77, 1, (12, 0), ((12, 0), (12, 16))
    w(f, ["return self._ApplyTypes_(", magic_numbers,", u'",vb_method_name,"', None, ", ", ".join(vb_params), ")"], tabs=2, nle=2)

def pretty_print_data(data):
    space = "    "
    for folder in sorted(data.keys()):
        print folder
        for file_name in sorted(data[folder].keys()):
            print space, file_name
            print space, space, "Help = ", data[folder][file_name]["help"]
            print space, space, "Syntax = ", data[folder][file_name]["syntax"]
            print space, space, "Parameters : "
            counter = 1
            for param in data[folder][file_name]["params"]:
                print space, space, "  ", counter, ") ", param[0], " = ", param[1], param[2], param[3]
                counter += 1
            print space, space, "Returns : "
            counter = 1            
            for return_val in data[folder][file_name]["returns"]: 
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
            #if not is_in_ct(file_name):
            #    print "ct \t", file_name, " in ", folder_name
            if not is_in_pw32(file_name):
                print "pw32 \t", file_name, " in ", folder_name

def is_in_pw32(name):
    return name in pw32_rs.IRhinoScript.__dict__.keys()

def is_in_ct(name):
    if get_ct_id_by_name(name) == None: 
        return False
    return True

data = parse_docs()
find_methods_mismatch(data)
compare_with_ct(data)


#pretty_print_data(data) 
#write_classes(data)

#print methods.get_method_by_id(905)
#print methods.get_method_by_name("GetRectangle")
