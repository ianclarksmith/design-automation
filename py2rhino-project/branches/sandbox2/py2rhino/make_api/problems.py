from py2rhino.data import gen_py2rhino as p2r 

def print_method_names():
    count = 0
    for i in sorted(p2r.__dict__.keys()):
        if not i.startswith("__"):
            if isinstance(rs_p2r.__dict__[i], dict):
                print i

def print_module_names():
    count = 0
    for i in sorted(rs_p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(rs_p2r.__dict__[i], dict):
                print i
                
def print_module_and_method_names():
    count = 0
    for i in sorted(rs_p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(rs_p2r.__dict__[i], dict):
                print i
                mod = rs_p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        print "\t", j
                

def get_data_dictionary():
    data = {}
    for i in sorted(rs_p2r.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(rs_p2r.__dict__[i], dict):
                data[i] = {}
                mod = rs_p2r.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        data[i][j] = mod.__dict__[j]
    return data


def find_arrays_with_missing_type():
    count = 0
    for i in sorted(rs_p2r.__dict__.keys()):
        if not i.startswith("__"):
            count += 1
            d = rs_p2r.__dict__[i]
            print count, "\t", d['class'], d['method']
    

#===============================================================================
# Run problem solver
#===============================================================================
if __name__ == '__main__':
    print print_method_names()