#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

angle = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "angle",
    "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ"),("world","bln","OPT")),
    "method_returns": ("array","null")
    }
angle_2 = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "angle_2",
    "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
deviation = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "deviation",
    "method_parameters": (("numbers","array_of int","REQ"),),
    "method_returns": ("number","null")
    }
distance = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "distance",
    "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "method_returns": ("number","array","null")
    }
distance_2 = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "distance_2",
    "method_parameters": (("point_1","array_of dbl","REQ"),("point_array","array_of dbl","REQ")),
    "method_returns": ("number","array","null")
    }
hypot = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "hypot",
    "method_parameters": (("number_x","dbl","REQ"),("number_y","dbl","REQ")),
    "method_returns": ("number","null")
    }
max = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "max",
    "method_parameters": (("numbers","array_of int","REQ"),),
    "method_returns": ("number","null")
    }
mean = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "mean",
    "method_parameters": (("numbers","array_of int","REQ"),),
    "method_returns": ("number","null")
    }
median = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "median",
    "method_parameters": (("numbers","array_of int","REQ"),),
    "method_returns": ("number","null")
    }
min = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "min",
    "method_parameters": (("numbers","array_of int","REQ"),),
    "method_returns": ("number","null")
    }
polar = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "polar",
    "method_parameters": (("point","array_of dbl","REQ"),("angle","dbl","REQ"),("distance","dbl","REQ"),("plane","array_of dbl","OPT")),
    "method_returns": ("array","null")
    }
