from util import *
from py2rhino.data import gen_py2rhino as p2r 
in_folder = "..\\data\\gen_py2rhino\\"
out_folder = "..\\"
#===============================================================================
# Get the data
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
# The method with parameter mismatch problem
#===============================================================================
def write_methods_with_param_mismatch(data_dict):
    counter_tm = 0
    counter_tf = 0
    f1 = open(in_folder + "_methods_with_too_many_params.py", mode='w')
    f2 = open(in_folder + "_methods_with_too_few_params.py", mode='w')
    w(f1, '#These methods have too many parameters when compared to the COM definition', tabs=0, nls=0, nle=2)
    w(f2, '#These methods have too few parameters when compared to the COM definition', tabs=0, nls=0, nle=2)
    
    for module_name in sorted(data_dict.keys()):
        w(f1, (module_name, ' = {'), tabs=0, nls=0, nle=1)
        w(f2, (module_name, ' = {'), tabs=0, nls=0, nle=1)
        for method_name in sorted(data_dict[module_name].keys()):
            has_mismatch = False
            param_html_dict = data_dict[module_name][method_name]['params_html']
            param_com_dict = data_dict[module_name][method_name]['params_com']
            if len(param_html_dict) > len(param_com_dict):
                has_mismatch = True
                f = f1
                counter_tm += 1
            elif len(param_html_dict) < len(param_com_dict):   
                has_mismatch = True
                f = f2
                counter_tf += 1
            if has_mismatch:
                w(f, ('"', method_name, '": {'), tabs=1, nls=0, nle=1)
                w(f, '\t# The COM object lists the following parameters', tabs=1, nls=0, nle=1)
                for param_num in param_com_dict.keys():
                    name = param_com_dict[param_num]['name']
                    opt_or_req = param_com_dict[param_num]['opt_or_req']
                    w(f, ('\t# ', str(param_num), ': ', name, ', ', opt_or_req), tabs=1, nls=0, nle=1)
                for param_num in param_html_dict.keys():
                    name = param_html_dict[param_num]['name']
                    type_string = param_html_dict[param_num]['type_string']
                    opt_or_req = param_html_dict[param_num]['opt_or_req']
                    if type_string == 'arr':
                        type_string += '_of_???'
                    w(f, ('"', name, '": \t("', opt_or_req, '", "', type_string, '"),'), tabs=2, nls=0, nle=1)
                w(f, '},', tabs=1, nls=0, nle=1)
        w(f1, '},', tabs=0, nls=0, nle=1)
        w(f2, '},', tabs=0, nls=0, nle=1)
    f1.close()
    f2.close()
    print "methods with too many params = ", counter_tm
    print "methods with too many params = ", counter_tf
    
#===============================================================================
# The array with missing type problem
#===============================================================================
def write_array_type_strings(data_dict):
    counter = 0
    f = open(in_folder + "_array_type_strings.py", mode='w')
    w(f, '#Replace in the ??? with either "bln", "int", "dbl", or "str"', tabs=0, nls=0, nle=2)

    for module_name in sorted(data_dict.keys()):
        w(f, (module_name, ' = {'), tabs=0, nls=0, nle=1)
        for method_name in sorted(data_dict[module_name].keys()):
            has_array = False
            param_html_dict = data_dict[module_name][method_name]['params_html']
            param_com_dict = data_dict[module_name][method_name]['params_com']            
            for param_num in param_html_dict.keys():
                type_string = param_html_dict[param_num]['name_prefix']
                if type_string.startswith('arr'):
                    has_array = True
                    counter += 1
            if has_array:
                w(f, ('"', method_name, '": {'), tabs=1, nls=0, nle=1)
                for param_num in data_dict[module_name][method_name]['params_html'].keys():
                    py_name = param_html_dict[param_num]['py_name']
                    type_string = param_html_dict[param_num]['name_prefix']
                    if type_string == 'arr':
                        type_string += '_of_???'
                    w(f, ('"', py_name, '": "', type_string, '",'), tabs=2, nls=0, nle=1)
                w(f, '},', tabs=1, nls=0, nle=1)
        w(f, '},', tabs=0, nls=0, nle=1)
    f.close()
    print counter
    
#===============================================================================
# Run problem finder
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    write_array_type_strings(data_dict)
    
    print 'done'