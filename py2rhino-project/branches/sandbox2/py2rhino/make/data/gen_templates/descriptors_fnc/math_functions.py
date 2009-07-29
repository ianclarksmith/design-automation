#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

angle = {
    "function_location": "math",
    "function_com_id": 115,
    "function_vb_name": "Angle",
    "function_name": "angle",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ"),("world","bln","OPT")),
    "function_returns": ("array","null")
    }
angle_2 = {
    "function_location": "math",
    "function_com_id": 116,
    "function_vb_name": "Angle2",
    "function_name": "angle_2",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
deviation = {
    "function_location": "math",
    "function_com_id": 773,
    "function_vb_name": "Deviation",
    "function_name": "deviation",
    "function_parameters": (("numbers","array_of int","REQ"),),
    "function_returns": ("number","null")
    }
distance = {
    "function_location": "math",
    "function_com_id": 118,
    "function_vb_name": "Distance",
    "function_name": "distance",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "function_returns": ("number","array","null")
    }
distance_2 = {
    "function_location": "math",
    "function_com_id": 118,
    "function_vb_name": "Distance",
    "function_name": "distance_2",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_array","array_of dbl","REQ")),
    "function_returns": ("number","array","null")
    }
hypot = {
    "function_location": "math",
    "function_com_id": 765,
    "function_vb_name": "Hypot",
    "function_name": "hypot",
    "function_parameters": (("number_x","dbl","REQ"),("number_y","dbl","REQ")),
    "function_returns": ("number","null")
    }
max = {
    "function_location": "math",
    "function_com_id": 768,
    "function_vb_name": "Max",
    "function_name": "max",
    "function_parameters": (("numbers","array_of int","REQ"),),
    "function_returns": ("number","null")
    }
mean = {
    "function_location": "math",
    "function_com_id": 771,
    "function_vb_name": "Mean",
    "function_name": "mean",
    "function_parameters": (("numbers","array_of int","REQ"),),
    "function_returns": ("number","null")
    }
median = {
    "function_location": "math",
    "function_com_id": 772,
    "function_vb_name": "Median",
    "function_name": "median",
    "function_parameters": (("numbers","array_of int","REQ"),),
    "function_returns": ("number","null")
    }
min = {
    "function_location": "math",
    "function_com_id": 769,
    "function_vb_name": "Min",
    "function_name": "min",
    "function_parameters": (("numbers","array_of int","REQ"),),
    "function_returns": ("number","null")
    }
polar = {
    "function_location": "math",
    "function_com_id": 662,
    "function_vb_name": "Polar",
    "function_name": "polar",
    "function_parameters": (("point","array_of dbl","REQ"),("angle","dbl","REQ"),("distance","dbl","REQ"),("plane","array_of dbl","OPT")),
    "function_returns": ("array","null")
    }
