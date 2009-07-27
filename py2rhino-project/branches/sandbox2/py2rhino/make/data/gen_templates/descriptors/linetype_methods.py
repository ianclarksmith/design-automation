#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

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
