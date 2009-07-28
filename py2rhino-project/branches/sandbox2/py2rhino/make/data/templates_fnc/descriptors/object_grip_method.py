#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

enable_object_grips = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "enable_object_grips",
    "method_parameters": (("object","str","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","null")
    }
get_object_grips = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "get_object_grips",
    "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "method_returns": ("array","string","number","array","null")
    }
next_object_grip = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "next_object_grip",
    "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("number","null")
    }
object_grip_count = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "object_grip_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
object_grip_locations = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "object_grip_locations",
    "method_parameters": (("object","str","REQ"),("points","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
object_grips_on = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "object_grips_on",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
object_grips_selected = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "object_grips_selected",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
prev_object_grip = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "prev_object_grip",
    "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("number","null")
    }
select_object_grips = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "select_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
selected_object_grips = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "selected_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
unselect_object_grips = {
    "method_location": "object_grip",
    "method_type": "FUNCTION",
    "method_name": "unselect_object_grips",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
