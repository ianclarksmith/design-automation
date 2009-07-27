#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

enable_object_grips = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "enable_object_grips",
    "method_parameters": (("object","str","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","null")
    }
get_object_grips = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "get_object_grips",
    "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "method_returns": ("array","string","number","array","null")
    }
next_object_grip = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "next_object_grip",
    "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("number","null")
    }
object_grip_count = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "object_grip_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
object_grip_locations = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "object_grip_locations",
    "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","OPT")),
    "method_returns": ("array","array","null")
    }
object_grips_on = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "object_grips_on",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
object_grips_selected = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "object_grips_selected",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
prev_object_grip = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "prev_object_grip",
    "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("number","null")
    }
select_object_grips = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "select_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
selected_object_grips = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "selected_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
unselect_object_grips = {
    "method_location": "ObjectGrip",
    "method_type": "METHOD",
    "method_name": "unselect_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
