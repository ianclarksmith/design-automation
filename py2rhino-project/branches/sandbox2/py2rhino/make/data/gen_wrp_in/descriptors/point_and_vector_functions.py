#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

is_vector_parallel_to = {
    "function_location": "point_and_vector",
    "function_com_id": 660,
    "function_vb_name": "IsVectorParallelTo",
    "function_name": "is_vector_parallel_to",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("number","null")
    }
is_vector_perpendicular_to = {
    "function_location": "point_and_vector",
    "function_com_id": 661,
    "function_vb_name": "IsVectorPerpendicularTo",
    "function_name": "is_vector_perpendicular_to",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
is_vector_tiny = {
    "function_location": "point_and_vector",
    "function_com_id": 610,
    "function_vb_name": "IsVectorTiny",
    "function_name": "is_vector_tiny",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("boolean","null")
    }
is_vector_zero = {
    "function_location": "point_and_vector",
    "function_com_id": 611,
    "function_vb_name": "IsVectorZero",
    "function_name": "is_vector_zero",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("boolean","null")
    }
point_add = {
    "function_location": "point_and_vector",
    "function_com_id": 666,
    "function_vb_name": "PointAdd",
    "function_name": "point_add",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
point_array_bounding_box = {
    "function_location": "point_and_vector",
    "function_com_id": 746,
    "function_vb_name": "PointArrayBoundingBox",
    "function_name": "point_array_bounding_box",
    "function_parameters": (("points","array_of dbl","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
    "function_returns": ("array","null")
    }
point_array_closest_point = {
    "function_location": "point_and_vector",
    "function_com_id": 742,
    "function_vb_name": "PointArrayClosestPoint",
    "function_name": "point_array_closest_point",
    "function_parameters": (("points","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("number","null")
    }
point_array_transform = {
    "function_location": "point_and_vector",
    "function_com_id": 802,
    "function_vb_name": "PointArrayTransform",
    "function_name": "point_array_transform",
    "function_parameters": (("points","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
point_compare = {
    "function_location": "point_and_vector",
    "function_com_id": 667,
    "function_vb_name": "PointCompare",
    "function_name": "point_compare",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
point_divide = {
    "function_location": "point_and_vector",
    "function_com_id": 668,
    "function_vb_name": "PointDivide",
    "function_name": "point_divide",
    "function_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
point_scale = {
    "function_location": "point_and_vector",
    "function_com_id": 669,
    "function_vb_name": "PointScale",
    "function_name": "point_scale",
    "function_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
point_subtract = {
    "function_location": "point_and_vector",
    "function_com_id": 670,
    "function_vb_name": "PointSubtract",
    "function_name": "point_subtract",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
point_transform = {
    "function_location": "point_and_vector",
    "function_com_id": 671,
    "function_vb_name": "PointTransform",
    "function_name": "point_transform",
    "function_parameters": (("point","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
points_are_coplanar = {
    "function_location": "point_and_vector",
    "function_com_id": 593,
    "function_vb_name": "PointsAreCoplanar",
    "function_name": "points_are_coplanar",
    "function_parameters": (("points","array_of dbl","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
project_point_to_mesh = {
    "function_location": "point_and_vector",
    "function_com_id": 912,
    "function_vb_name": "ProjectPointToMesh",
    "function_name": "project_point_to_mesh",
    "function_parameters": (("points","array_of dbl","REQ"),("meshes","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
project_point_to_surface = {
    "function_location": "point_and_vector",
    "function_com_id": 892,
    "function_vb_name": "ProjectPointToSurface",
    "function_name": "project_point_to_surface",
    "function_parameters": (("points","array_of dbl","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
pull_points = {
    "function_location": "point_and_vector",
    "function_com_id": 716,
    "function_vb_name": "PullPoints",
    "function_name": "pull_points",
    "function_parameters": (("object","str","REQ"),("points","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_add = {
    "function_location": "point_and_vector",
    "function_com_id": 612,
    "function_vb_name": "VectorAdd",
    "function_name": "vector_add",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_compare = {
    "function_location": "point_and_vector",
    "function_com_id": 613,
    "function_vb_name": "VectorCompare",
    "function_name": "vector_compare",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("null",)
    }
vector_create = {
    "function_location": "point_and_vector",
    "function_com_id": 614,
    "function_vb_name": "VectorCreate",
    "function_name": "vector_create",
    "function_parameters": (("point_1","array_of dbl","REQ"),("point_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_cross_product = {
    "function_location": "point_and_vector",
    "function_com_id": 615,
    "function_vb_name": "VectorCrossProduct",
    "function_name": "vector_cross_product",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_divide = {
    "function_location": "point_and_vector",
    "function_com_id": 625,
    "function_vb_name": "VectorDivide",
    "function_name": "vector_divide",
    "function_parameters": (("vector","array_of dbl","REQ"),("divide","dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_dot_product = {
    "function_location": "point_and_vector",
    "function_com_id": 616,
    "function_vb_name": "VectorDotProduct",
    "function_name": "vector_dot_product",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("null",)
    }
vector_length = {
    "function_location": "point_and_vector",
    "function_com_id": 617,
    "function_vb_name": "VectorLength",
    "function_name": "vector_length",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("null",)
    }
vector_multiply = {
    "function_location": "point_and_vector",
    "function_com_id": 624,
    "function_vb_name": "VectorMultiply",
    "function_name": "vector_multiply",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("number","null")
    }
vector_reverse = {
    "function_location": "point_and_vector",
    "function_com_id": 618,
    "function_vb_name": "VectorReverse",
    "function_name": "vector_reverse",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
vector_rotate = {
    "function_location": "point_and_vector",
    "function_com_id": 678,
    "function_vb_name": "VectorRotate",
    "function_name": "vector_rotate",
    "function_parameters": (("vector","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_scale = {
    "function_location": "point_and_vector",
    "function_com_id": 619,
    "function_vb_name": "VectorScale",
    "function_name": "vector_scale",
    "function_parameters": (("vector","array_of dbl","REQ"),("scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_subtract = {
    "function_location": "point_and_vector",
    "function_com_id": 620,
    "function_vb_name": "VectorSubtract",
    "function_name": "vector_subtract",
    "function_parameters": (("vector_1","array_of dbl","REQ"),("vector_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_transform = {
    "function_location": "point_and_vector",
    "function_com_id": 800,
    "function_vb_name": "VectorTransform",
    "function_name": "vector_transform",
    "function_parameters": (("vector","array_of dbl","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
vector_unitize = {
    "function_location": "point_and_vector",
    "function_com_id": 621,
    "function_vb_name": "VectorUnitize",
    "function_name": "vector_unitize",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
