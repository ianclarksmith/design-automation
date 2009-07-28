import keyword
from util import *
from py2rhino.make.data.templates_fnc import descriptors as fnc

out_folder = "..\\functions\\"
#===============================================================================
# Get the data
#===============================================================================
def get_data_dictionary():
    data_dict = {}
    for method_set_name in fnc.__dict__.keys():
        if method_set_name.endswith('_methods'):
            method_set = fnc.__dict__[method_set_name]

            for method_name in method_set.__dict__.keys():
                if not method_name.startswith('__'):
                    method = method_set.__dict__[method_name]
                    
                    location = method['method_location']
                    
                    if not location in data_dict.keys():
                        data_dict[location] = {}
                    data_dict[location][method_name] = method
    return data_dict

#===============================================================================
# Run
#===============================================================================
if __name__ == '__main__':
    data_dict = get_data_dictionary()

    print "done"