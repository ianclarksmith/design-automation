#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

is_vector_parallel_to = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "is_vector_parallel_to",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("number","null")
    }
is_vector_perpendicular_to = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "is_vector_perpendicular_to",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_vector_tiny = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "is_vector_tiny",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_vector_zero = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "is_vector_zero",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
point_add = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_add",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
point_array_bounding_box = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_array_bounding_box",
    "method_parameters": (("points","arr_of_dbl","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
    "method_returns": ("array","null")
    }
point_array_closest_point = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_array_closest_point",
    "method_parameters": (("points","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("number","null")
    }
point_array_transform = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_array_transform",
    "method_parameters": (("points","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
point_compare = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_compare",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
point_divide = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_divide",
    "method_parameters": (("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
point_scale = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_scale",
    "method_parameters": (("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
point_subtract = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_subtract",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
point_transform = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "point_transform",
    "method_parameters": (("point","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
points_are_coplanar = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "points_are_coplanar",
    "method_parameters": (("points","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
project_point_to_mesh = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "project_point_to_mesh",
    "method_parameters": (("points","arr_of_dbl","REQ"),("meshes","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
project_point_to_surface = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "project_point_to_surface",
    "method_parameters": (("points","arr_of_dbl","REQ"),("surfaces","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
pull_points = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "pull_points",
    "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_add = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_add",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_compare = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_compare",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("null")
    }
vector_create = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_create",
    "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_cross_product = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_cross_product",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_divide = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_divide",
    "method_parameters": (("vector","arr_of_dbl","REQ"),("divide","dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_dot_product = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_dot_product",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("null")
    }
vector_length = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_length",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("null")
    }
vector_multiply = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_multiply",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("number","null")
    }
vector_reverse = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_reverse",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_rotate = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_rotate",
    "method_parameters": (("vector","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_scale = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_scale",
    "method_parameters": (("vector","arr_of_dbl","REQ"),("scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_subtract = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_subtract",
    "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_transform = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_transform",
    "method_parameters": (("vector","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
vector_unitize = {
    "method_location": "PointAndVector",
    "method_type": "METHOD",
    "method_name": "vector_unitize",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
