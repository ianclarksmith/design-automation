#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

angle = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "angle",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("world","bln","OPT")),
    "method_returns": ("array","null")
    }
angle2 = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "angle2",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
deviation = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "deviation",
    "method_parameters": (("numbers","arr_of_int","REQ")),
    "method_returns": ("number","null")
    }
distance = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "distance",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("point_array","arr_of_dbl","REQ")),
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
    "method_parameters": (("numbers","arr_of_int","REQ")),
    "method_returns": ("number","null")
    }
mean = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "mean",
    "method_parameters": (("numbers","arr_of_int","REQ")),
    "method_returns": ("number","null")
    }
median = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "median",
    "method_parameters": (("numbers","arr_of_int","REQ")),
    "method_returns": ("number","null")
    }
min = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "min",
    "method_parameters": (("numbers","arr_of_int","REQ")),
    "method_returns": ("number","null")
    }
polar = {
    "method_location": "Math",
    "method_type": "METHOD",
    "method_name": "polar",
    "method_parameters": (("point","arr_of_dbl","REQ"),("angle","dbl","REQ"),("distance","dbl","REQ"),("plane","arr_of_dbl","OPT")),
    "method_returns": ("array","null")
    }
