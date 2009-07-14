import linecache
import os
import string

def parse_docs():
    data = {}
    #get all the folders
    folders = os.listdir("..\\docs\\RhinoScript")
    for folder in folders:
        data[folder]  = {}
        #get all the files
        files = os.listdir("..\\docs\\RhinoScript\\" + folder)
        for file in files:
            #print file, " in ", folder
            file_name = file[:-4]
            if file_name != folder:
                contents = linecache.getlines('..\\docs\\RhinoScript\\%s\\%s' % (folder, file))
                contents = filter(lambda i: len(i)>1, contents)
                contents = map(lambda i: i.strip(string.whitespace), contents)
                #set some thinsg to None so we can do some checks later
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
                
                #get the simple stuff
                content_help = contents[line_num_syntax - 1]
                content_syntax = contents[line_num_syntax + 1]
                
                #now get the parameters
                if (line_num_returns - line_num_params) > 2:
                    content_params = {}
                    #set some flags
                    found_array_with_table = False
                    more_params_after_array = False
                    for line_num in range(line_num_params+1, line_num_returns, 2):
                        param_name = contents[line_num]
                        param_text = contents[line_num + 1]                    
                        #check if we have an array
                        if (param_name[:3] == "arr"):
                            start_line_num = line_num + 2
                            #with a table of contents
                            if ((contents[start_line_num] == "Element") and 
                                (contents[start_line_num + 1] == "Type") and
                                (contents[start_line_num + 2] == "Description")):    
                                found_array_with_table = True     
                                #need to figure out where the end of the table is
                                test = 0
                                end_found = False
                                while True:
                                    next_row = contents[start_line_num + 3 + (test * 3)]
                                    if (not next_row.isdigit()) or (int(next_row) != test):
                                        end_found = True
                                    if end_found: break
                                    test += 1
                                    assert test != 15
                                end_line_num = start_line_num + 2 + (test * 3)
                                #now get all that text into one line
                                for i in range(start_line_num, end_line_num):
                                    param_text = param_text + " " + contents[i] 
                                #check if there are any more parameters
                                if (contents[end_line_num + 1] != "Returns"):
                                    line_num_params = end_line_num + 1
                                    more_params_after_array = True
                        #get the parameters
                        content_params[param_name] = param_text
                        if found_array_with_table: 
                            break
                    #if there are more params after this array, we will need to keep going
                    if more_params_after_array:
                        for line_num in range(line_num_params+1, line_num_returns, 2):
                            param_name = contents[line_num]
                            param_text = contents[line_num + 1]
                            assert param_name[:3] != "arr"
                            content_params[param_name] = param_text
                
                
                #now get the return value
                #there are three possibilities - an array, a simple type, or null
                if (line_num_example - line_num_returns) > 2:
                    content_returns = {}
                    #is an array returned?
                    if contents[line_num_returns + 1] == "Array":
                        returns_array = line_num_returns + 1
                        ret_name = "Array"
                        count = 0
                        ret_text = ""
                        for line_num in range(line_num_returns+2, line_num_example):
                            if contents[line_num] == "Null":
                                break
                            ret_text = ret_text + " " + line
                            count += 1
                        content_returns[ret_name] = ret_text
                    #now see what else is returned
                    count = 0
                    for line_num in range(line_num_returns+1, line_num_example):
                        if contents[line_num] in ("Null", "Number", "Boolean", "String") :
                            ret_name = contents[line_num]
                            ret_text = contents[line_num + 1]
                        content_returns[ret_name] = ret_text
                        count = count + 1 
                    
                    
                #save the data
                data[folder][file_name] = {
                    "help": content_help,
                    "syntax": content_syntax,
                    "params": content_params,
                    "returns": content_returns
                }
    return data

def write_classes():
    pass

def write_class():
    fout = open ("application.py", mode='w')

def pretty_print_data(data):
    space = "    "
    for folder in data:
        print folder
        for file_name in data[folder]:
            print space, file_name
            print space, space, "Help = ", data[folder][file_name]["help"]
            print space, space, "Syntax = ", data[folder][file_name]["syntax"]
            print space, space, "Parameters : "
            for param in data[folder][file_name]["params"]:
                print space, space, space, param, " = ", data[folder][file_name]["params"][param]
            print space, space, "Returns : "
            for return_val in data[folder][file_name]["returns"]: 
                print space, space, space, return_val, " = ", data[folder][file_name]["returns"][return_val]
            
            
            
data = parse_docs()
pretty_print_data(data) 
