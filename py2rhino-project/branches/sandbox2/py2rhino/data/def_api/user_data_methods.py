#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

attribute_data_count = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "attribute_data_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
delete_attribute_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "delete_attribute_data",
    "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("boolean","null")
    }
delete_document_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "delete_document_data",
    "method_parameters": (("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("boolean","null")
    }
delete_object_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "delete_object_data",
    "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("boolean","null")
    }
document_data_count = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "document_data_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
get_attribute_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "get_attribute_data",
    "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("array","array","string","null")
    }
get_document_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "get_document_data",
    "method_parameters": (("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("array","array","string","null")
    }
get_object_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "get_object_data",
    "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "method_returns": ("array","array","string","null")
    }
get_user_text = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "get_user_text",
    "method_parameters": (("object","str","REQ"),("key","str","OPT"),("attach_to_geometry","bln","OPT")),
    "method_returns": ("string","array","null")
    }
is_attribute_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "is_attribute_data",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_document_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "is_document_data",
    "method_parameters": (),
    "method_returns": ("boolean")
    }
is_object_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "is_object_data",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_user_text = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "is_user_text",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
object_data_count = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "object_data_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
set_attribute_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "set_attribute_data",
    "method_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "method_returns": ("string","null")
    }
set_document_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "set_document_data",
    "method_parameters": (("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "method_returns": ("string","null")
    }
set_object_data = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "set_object_data",
    "method_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "method_returns": ("string","null")
    }
set_user_text = {
    "method_location": "User_Data",
    "method_type": "METHOD",
    "method_name": "set_user_text",
    "method_parameters": (("object","str","REQ"),("key","str","REQ"),("value","str","OPT"),("attach_to_geometry","bln","OPT")),
    "method_returns": ("boolean","null")
    }
