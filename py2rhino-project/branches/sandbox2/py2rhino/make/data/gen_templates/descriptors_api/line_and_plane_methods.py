#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

distance_to_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "distance_to_plane",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("number","null")
    }
evaluate_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "evaluate_plane",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
intersect_planes = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "intersect_planes",
    "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("plane3","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
line_closest_point = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_closest_point",
    "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
line_is_farther_than = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_is_farther_than",
    "method_parameters": (("line","arr_of_dbl","REQ"),("distance","dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_is_farther_than_2 = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_is_farther_than_2",
    "method_parameters": (("line","arr_of_dbl","REQ"),("distance","dbl","REQ"),("line2","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_line_intersection = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_line_intersection",
    "method_parameters": (("line_a","arr_of_dbl","REQ"),("line_b","arr_of_dbl","REQ"),("planar","bln","OPT")),
    "method_returns": ("array","array","null")
    }
line_max_distance_to = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_max_distance_to",
    "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_max_distance_to_2 = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_max_distance_to_2",
    "method_parameters": (("line","arr_of_dbl","REQ"),("line2","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_min_distance_to = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_min_distance_to",
    "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_min_distance_to_2 = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_min_distance_to_2",
    "method_parameters": (("line","arr_of_dbl","REQ"),("line2","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
line_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_plane",
    "method_parameters": (("line","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
line_plane_intersection = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_plane_intersection",
    "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
line_transform = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "line_transform",
    "method_parameters": (("line","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
move_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "move_plane",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("origin","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_closest_point = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_closest_point",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("return_point","bln","OPT")),
    "method_returns": ("array","null")
    }
plane_equation = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_equation",
    "method_parameters": (("plane","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_fit_from_points = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_fit_from_points",
    "method_parameters": (("points","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_from_frame = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_from_frame",
    "method_parameters": (("origin","arr_of_dbl","REQ"),("xaxis","arr_of_dbl","REQ"),("yaxis","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_from_normal = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_from_normal",
    "method_parameters": (("origin","arr_of_dbl","REQ"),("normal","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_from_points = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_from_points",
    "method_parameters": (("origin","arr_of_dbl","REQ"),("point_x","arr_of_dbl","REQ"),("point_y","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_plane_intersection = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_plane_intersection",
    "method_parameters": (("plane1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
plane_transform = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "plane_transform",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
rotate_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "rotate_plane",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
world_x_y_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "world_x_y_plane",
    "method_parameters": (),
    "method_returns": ("array")
    }
world_y_z_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "world_y_z_plane",
    "method_parameters": (),
    "method_returns": ("array")
    }
world_z_x_plane = {
    "method_location": "LineAndPlane",
    "method_type": "METHOD",
    "method_name": "world_z_x_plane",
    "method_parameters": (),
    "method_returns": ("array")
    }
