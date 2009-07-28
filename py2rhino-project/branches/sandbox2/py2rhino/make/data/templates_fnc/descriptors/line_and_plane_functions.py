#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

distance_to_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 628,
    "function_vb_name": "DistanceToPlane",
    "function_name": "distance_to_plane",
    "function_parameters": (("plane","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("number","null")
    }
evaluate_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 751,
    "function_vb_name": "EvaluatePlane",
    "function_name": "evaluate_plane",
    "function_parameters": (("plane","array_of dbl","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
intersect_planes = {
    "function_location": "line_and_plane",
    "function_com_id": 745,
    "function_vb_name": "IntersectPlanes",
    "function_name": "intersect_planes",
    "function_parameters": (("plane1","array_of dbl","REQ"),("plane2","array_of dbl","REQ"),("plane3","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
line_closest_point = {
    "function_location": "line_and_plane",
    "function_com_id": 899,
    "function_vb_name": "LineClosestPoint",
    "function_name": "line_closest_point",
    "function_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
line_is_farther_than = {
    "function_location": "line_and_plane",
    "function_com_id": 902,
    "function_vb_name": "LineIsFartherThan",
    "function_name": "line_is_farther_than",
    "function_parameters": (("line","array_of dbl","REQ"),("distance","dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_is_farther_than_2 = {
    "function_location": "line_and_plane",
    "function_com_id": 902,
    "function_vb_name": "LineIsFartherThan",
    "function_name": "line_is_farther_than_2",
    "function_parameters": (("line","array_of dbl","REQ"),("distance","dbl","REQ"),("line2","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_line_intersection = {
    "function_location": "line_and_plane",
    "function_com_id": 736,
    "function_vb_name": "LineLineIntersection",
    "function_name": "line_line_intersection",
    "function_parameters": (("line_a","array_of dbl","REQ"),("line_b","array_of dbl","REQ"),("planar","bln","OPT")),
    "function_returns": ("array","array","null")
    }
line_max_distance_to = {
    "function_location": "line_and_plane",
    "function_com_id": 901,
    "function_vb_name": "LineMaxDistanceTo",
    "function_name": "line_max_distance_to",
    "function_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_max_distance_to_2 = {
    "function_location": "line_and_plane",
    "function_com_id": 901,
    "function_vb_name": "LineMaxDistanceTo",
    "function_name": "line_max_distance_to_2",
    "function_parameters": (("line","array_of dbl","REQ"),("line2","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_min_distance_to = {
    "function_location": "line_and_plane",
    "function_com_id": 900,
    "function_vb_name": "LineMinDistanceTo",
    "function_name": "line_min_distance_to",
    "function_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_min_distance_to_2 = {
    "function_location": "line_and_plane",
    "function_com_id": 900,
    "function_vb_name": "LineMinDistanceTo",
    "function_name": "line_min_distance_to_2",
    "function_parameters": (("line","array_of dbl","REQ"),("line2","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
line_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 898,
    "function_vb_name": "LinePlane",
    "function_name": "line_plane",
    "function_parameters": (("line","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
line_plane_intersection = {
    "function_location": "line_and_plane",
    "function_com_id": 743,
    "function_vb_name": "LinePlaneIntersection",
    "function_name": "line_plane_intersection",
    "function_parameters": (("line","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
line_transform = {
    "function_location": "line_and_plane",
    "function_com_id": 897,
    "function_vb_name": "LineTransform",
    "function_name": "line_transform",
    "function_parameters": (("line","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
move_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 631,
    "function_vb_name": "MovePlane",
    "function_name": "move_plane",
    "function_parameters": (("plane","array_of dbl","REQ"),("origin","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_closest_point = {
    "function_location": "line_and_plane",
    "function_com_id": 629,
    "function_vb_name": "PlaneClosestPoint",
    "function_name": "plane_closest_point",
    "function_parameters": (("plane","array_of dbl","REQ"),("point","array_of dbl","REQ"),("return_point","bln","OPT")),
    "function_returns": ("array","null")
    }
plane_equation = {
    "function_location": "line_and_plane",
    "function_com_id": 642,
    "function_vb_name": "PlaneEquation",
    "function_name": "plane_equation",
    "function_parameters": (("plane","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_fit_from_points = {
    "function_location": "line_and_plane",
    "function_com_id": 725,
    "function_vb_name": "PlaneFitFromPoints",
    "function_name": "plane_fit_from_points",
    "function_parameters": (("points","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_from_frame = {
    "function_location": "line_and_plane",
    "function_com_id": 627,
    "function_vb_name": "PlaneFromFrame",
    "function_name": "plane_from_frame",
    "function_parameters": (("origin","array_of dbl","REQ"),("xaxis","array_of dbl","REQ"),("yaxis","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_from_normal = {
    "function_location": "line_and_plane",
    "function_com_id": 626,
    "function_vb_name": "PlaneFromNormal",
    "function_name": "plane_from_normal",
    "function_parameters": (("origin","array_of dbl","REQ"),("normal","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_from_points = {
    "function_location": "line_and_plane",
    "function_com_id": 649,
    "function_vb_name": "PlaneFromPoints",
    "function_name": "plane_from_points",
    "function_parameters": (("origin","array_of dbl","REQ"),("point_x","array_of dbl","REQ"),("point_y","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_plane_intersection = {
    "function_location": "line_and_plane",
    "function_com_id": 744,
    "function_vb_name": "PlanePlaneIntersection",
    "function_name": "plane_plane_intersection",
    "function_parameters": (("plane1","array_of dbl","REQ"),("point2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
plane_transform = {
    "function_location": "line_and_plane",
    "function_com_id": 801,
    "function_vb_name": "PlaneTransform",
    "function_name": "plane_transform",
    "function_parameters": (("plane","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
rotate_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 630,
    "function_vb_name": "RotatePlane",
    "function_name": "rotate_plane",
    "function_parameters": (("plane","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
world_x_y_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 652,
    "function_vb_name": "WorldXYPlane",
    "function_name": "world_x_y_plane",
    "function_parameters": (),
    "function_returns": ("array")
    }
world_y_z_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 653,
    "function_vb_name": "WorldYZPlane",
    "function_name": "world_y_z_plane",
    "function_parameters": (),
    "function_returns": ("array")
    }
world_z_x_plane = {
    "function_location": "line_and_plane",
    "function_com_id": 654,
    "function_vb_name": "WorldZXPlane",
    "function_name": "world_z_x_plane",
    "function_parameters": (),
    "function_returns": ("array")
    }
