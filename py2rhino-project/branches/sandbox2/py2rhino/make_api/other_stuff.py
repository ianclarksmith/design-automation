from ct  import rhinoscript as ct_rs
from pw32 import  rhinoscript as pw32_rs
    
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