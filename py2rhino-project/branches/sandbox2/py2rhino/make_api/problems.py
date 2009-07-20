from py2rhino.data import gen_py2rhino as p2r 

def print_method_names():
    count = 0
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if isinstance(p2r.__dict__[i], dict):
                print i

def print_module_names():
    count = 0
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(p2r.__dict__[i], dict):
                print i
                
def print_module_and_method_names():
    count = 0
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(p2r.__dict__[i], dict):
                print i
                mod = p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        print "\t", j
                

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

def find_methods_with_param_mismatch(data_dict):
    counter = 0
    for module_name in sorted(data_dict.keys()):
        for method_name in sorted(data_dict[module_name].keys()):
            param_html_dict = data_dict[module_name][method_name]['params_html']
            param_com_dict = data_dict[module_name][method_name]['params_com']
            if len(param_html_dict) != len(param_com_dict):
                print module_name, method_name
                counter += 1
    print counter

def find_arrays_with_missing_type():
    count = 0
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            count += 1
            d = p2r.__dict__[i]
            print count, "\t", d['class'], d['method']
    

#===============================================================================
# Run problem finder
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()
    find_methods_with_param_mismatch(data_dict)