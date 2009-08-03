#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

enable_object_grips = {
    "function_location": "object_grip",
    "function_com_id": 499,
    "function_vb_name": "EnableObjectGrips",
    "function_name": "enable_object_grips",
    "function_parameters": (("object","str","REQ"),("enable","bln","OPT")),
    "function_returns": ("boolean","null")
    }
get_object_grip = {
    "function_location": "object_grip",
    "function_com_id": 561,
    "function_vb_name": "GetObjectGrip",
    "function_name": "get_object_grip",
    "function_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "function_returns": ("array","string","number","array","null")
    }
get_object_grips = {
    "function_location": "object_grip",
    "function_com_id": 562,
    "function_vb_name": "GetObjectGrips",
    "function_name": "get_object_grips",
    "function_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "function_returns": ("array","string","number","array","null")
    }
next_object_grip = {
    "function_location": "object_grip",
    "function_com_id": 558,
    "function_vb_name": "NextObjectGrip",
    "function_name": "next_object_grip",
    "function_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "function_returns": ("number","null")
    }
object_grip_count = {
    "function_location": "object_grip",
    "function_com_id": 500,
    "function_vb_name": "ObjectGripCount",
    "function_name": "object_grip_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
object_grip_location = {
    "function_location": "object_grip",
    "function_com_id": 556,
    "function_vb_name": "ObjectGripLocation",
    "function_name": "object_grip_location",
    "function_parameters": (("object","str","REQ"),("index","int","REQ"),("point","arr","OPT")),
    "function_returns": ("array","array","null")
    }
object_grip_locations = {
    "function_location": "object_grip",
    "function_com_id": 557,
    "function_vb_name": "ObjectGripLocations",
    "function_name": "object_grip_locations",
    "function_parameters": (("object","str","REQ"),("points","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
object_grips_on = {
    "function_location": "object_grip",
    "function_com_id": 497,
    "function_vb_name": "ObjectGripsOn",
    "function_name": "object_grips_on",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
object_grips_selected = {
    "function_location": "object_grip",
    "function_com_id": 498,
    "function_vb_name": "ObjectGripsSelected",
    "function_name": "object_grips_selected",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
prev_object_grip = {
    "function_location": "object_grip",
    "function_com_id": 559,
    "function_vb_name": "PrevObjectGrip",
    "function_name": "prev_object_grip",
    "function_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
    "function_returns": ("number","null")
    }
select_object_grip = {
    "function_location": "object_grip",
    "function_com_id": 554,
    "function_vb_name": "SelectObjectGrip",
    "function_name": "select_object_grip",
    "function_parameters": (("object","str","REQ"),("index","int","REQ")),
    "function_returns": ("boolean","null")
    }
select_object_grips = {
    "function_location": "object_grip",
    "function_com_id": 501,
    "function_vb_name": "SelectObjectGrips",
    "function_name": "select_object_grips",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
selected_object_grips = {
    "function_location": "object_grip",
    "function_com_id": 560,
    "function_vb_name": "SelectedObjectGrips",
    "function_name": "selected_object_grips",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
unselect_object_grip = {
    "function_location": "object_grip",
    "function_com_id": 555,
    "function_vb_name": "UnselectObjectGrip",
    "function_name": "unselect_object_grip",
    "function_parameters": (("object","str","REQ"),("index","int","REQ")),
    "function_returns": ("boolean","null")
    }
unselect_object_grips = {
    "function_location": "object_grip",
    "function_com_id": 502,
    "function_vb_name": "UnselectObjectGrips",
    "function_name": "unselect_object_grips",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
