#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here
#===============================================================================
# Vector
#===============================================================================
class Vector(object):    
    inherits = None

    class Functions(object):

        is_vector_parallel_to = {
            "method_name": "is_parallel_to",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("number","null")
            }
        is_vector_perpendicular_to = {
            "method_name": "is_perpendicular_to",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("bln","null")
            }
        is_vector_tiny = {
            "method_name": "is_tiny",
            "method_parameters": (("vector","array_of dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        is_vector_zero = {
            "method_name": "is_zero",
            "method_parameters": (("vector","array_of dbl","REQ"),),
            "method_returns": ("bln","null")
            }
        

        vector_add = {
            "method_name": "add",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_compare = {
            "method_name": "compare",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("number", "null",)
            }
        vector_create = {
            "method_name": "create",
            "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_cross_product = {
            "method_name": "cross_product",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_divide = {
            "method_name": "divide",
            "method_parameters": (("vector","array_of dbl","REQ"),("divide","dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_dot_product = {
            "method_name": "dot_product",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("number", "null",)
            }
        vector_length = {
            "method_name": "length",
            "method_parameters": (("vector","array_of dbl","REQ"),),
            "method_returns": ("number", "null",)
            }
        vector_multiply = {
            "method_name": "multiply",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("number","null")
            }
        vector_reverse = {
            "method_name": "reverse",
            "method_parameters": (("vector","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }
        vector_rotate = {
            "method_name": "rotate",
            "method_parameters": (("vector","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_scale = {
            "method_name": "scale",
            "method_parameters": (("vector","array_of dbl","REQ"),("scale","dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_subtract = {
            "method_name": "subtract",
            "method_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_transform = {
            "method_name": "transform",
            "method_parameters": (("vector","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        vector_unitize = {
            "method_name": "unitize",
            "method_parameters": (("vector","array_of dbl","REQ"),),
            "method_returns": ("array_of number","null")
            }        
        
#===============================================================================
# Point
#===============================================================================
class Point(object):    
    inherits = None
    class Functions(object):
        point_compare = {
            "method_name": "compare",
            "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ"),("tolerance","dbl","OPT")),
            "method_returns": ("bln","null")
            }
        #the input is a list of points
        points_are_coplanar = {
            "method_name": "points_are_coplanar",
            "method_parameters": (("points","array_of dbl","REQ"),("tolerance","dbl","OPT")),
            "method_returns": ("bln","null")
            } 
        
        point_add = {
            "method_name": "add",
            "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        point_divide = {
            "method_name": "divide",
            "method_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        point_scale = {
            "method_name": "scale",
            "method_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        point_subtract = {
            "method_name": "subtract",
            "method_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        point_transform = {
            "method_name": "transform",
            "method_parameters": (("point","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        

        point_array_bounding_box = {
            "method_name": "points_bounding_box",
            "method_parameters": (("points","array_of dbl","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
            "method_returns": ("array_of number","null")
            }
        point_array_closest_point = {
            "method_name": "points_closest_point",
            "method_parameters": (("points","array_of dbl","REQ"),("point","array_of dbl","REQ")),
            "method_returns": ("number","null")
            }
        point_array_transform = {
            "method_name": "points_transform",
            "method_parameters": (("points","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        
        #these need to be added to object classes
        project_point_to_mesh = {
            "method_name": "project_point_to_mesh",
            "method_parameters": (("points","array_of dbl","REQ"),("meshes","array_of _ObjectRoot._MeshRoot","REQ"),("direction","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        project_point_to_surface = {
            "method_name": "project_point_to_surface",
            "method_parameters": (("points","array_of dbl","REQ"),("surfaces","array_of _ObjectRoot.SurfaceRoot","REQ"),("direction","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }
        pull_points = {
            "method_name": "pull_points",
            "method_parameters": (("object","_ObjectRoot","REQ"),("points","array_of dbl","REQ")),
            "method_returns": ("array_of number","null")
            }        