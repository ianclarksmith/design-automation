#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

is_linetype = {
    "method_location": "Linetype",
    "method_type": "METHOD",
    "method_name": "is_linetype",
    "method_parameters": (("linetype","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_linetype_reference = {
    "method_location": "Linetype",
    "method_type": "METHOD",
    "method_name": "is_linetype_reference",
    "method_parameters": (("linetype","str","REQ")),
    "method_returns": ("boolean","null")
    }
linetype_count = {
    "method_location": "Linetype",
    "method_type": "METHOD",
    "method_name": "linetype_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
linetype_names = {
    "method_location": "Linetype",
    "method_type": "METHOD",
    "method_name": "linetype_names",
    "method_parameters": (("sort","bln","OPT")),
    "method_returns": ("array","null")
    }
