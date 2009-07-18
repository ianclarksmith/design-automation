import docs.gen

def print_method_names():
    count = 0
    for i in sorted(docs.gen.__dict__.keys()):
        if not i.startswith("__"):
            if isinstance(docs.gen.__dict__[i], dict):
                print i

def print_module_names():
    count = 0
    for i in sorted(docs.gen.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(docs.gen.__dict__[i], dict):
                print i
                
def print_module_and_method_names():
    count = 0
    for i in sorted(docs.gen.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(docs.gen.__dict__[i], dict):
                print i
                mod = docs.gen.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        print "\t", j
                

def get_data_dictionary():
    data = {}
    for i in sorted(docs.gen.__dict__.keys()):
        if not i.startswith("__"):
            if not isinstance(docs.gen.__dict__[i], dict):
                data[i] = {}
                mod = docs.gen.__dict__[i]
                for j in sorted(mod.__dict__.keys()):
                    if not j.startswith("__"):
                        data[i][j] = mod.__dict__[j]
    return data


def find_arrays_with_missing_type():
    count = 0
    for i in sorted(docs.gen.__dict__.keys()):
        if not i.startswith("__"):
            count += 1
            d = docs.gen.__dict__[i]
            print count, "\t", d['class'], d['method']
    

#===============================================================================
# Run problem solver
#===============================================================================
if __name__ == '__main__':
    print get_data_dictionary()