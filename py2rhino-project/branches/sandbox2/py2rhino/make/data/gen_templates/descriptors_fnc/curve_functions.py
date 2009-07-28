#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_arc = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_arc",
    "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ")),
    "method_returns": ("string","null")
    }
add_arc3_pt = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_arc3_pt",
    "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_circle = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_circle",
    "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ")),
    "method_returns": ("string","null")
    }
add_circle3_pt = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_circle3_pt",
    "method_parameters": (("first","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_curve",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT")),
    "method_returns": ("string","null")
    }
add_ellipse = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_ellipse",
    "method_parameters": (("plane","array_of dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ")),
    "method_returns": ("string","null")
    }
add_ellipse3_pt = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_ellipse3_pt",
    "method_parameters": (("center","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_fillet_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_fillet_curve",
    "method_parameters": (("curve0","str","REQ"),("curve1","str","REQ"),("radius","dbl","OPT"),("point0","array_of dbl","OPT"),("point1","array_of dbl","OPT")),
    "method_returns": ("string","null")
    }
add_interp_crv_on_srf = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_interp_crv_on_srf",
    "method_parameters": (("object","str","REQ"),("points","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_interp_crv_on_srf_u_v = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_interp_crv_on_srf_u_v",
    "method_parameters": (("object","str","REQ"),("points","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_interp_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_interp_curve",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","array_of dbl","OPT"),("end_tan","array_of dbl","OPT")),
    "method_returns": ("string","null")
    }
add_interp_curve_ex = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_interp_curve_ex",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","array_of dbl","OPT"),("end_tangent","array_of dbl","OPT")),
    "method_returns": ("string","null")
    }
add_line = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_line",
    "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_nurbs_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_nurbs_curve",
    "method_parameters": (("points","array_of dbl","REQ"),("knots","array_of int","REQ"),("degree","int","REQ"),("weights","array_of int","OPT")),
    "method_returns": ("string","null")
    }
add_polyline = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_polyline",
    "method_parameters": (("points","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_sub_crv = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "add_sub_crv",
    "method_parameters": (("object","str","REQ"),("param0","dbl","REQ"),("param1","dbl","REQ")),
    "method_returns": ("string","null")
    }
arc_angle = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "arc_angle",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
arc_center_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "arc_center_point",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("null")
    }
arc_mid_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "arc_mid_point",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("null")
    }
arc_radius = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "arc_radius",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
circle_center_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "circle_center_point",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
circle_circumference = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "circle_circumference",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
circle_radius = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "circle_radius",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
close_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "close_curve",
    "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("string","null")
    }
convert_curve_to_polyline = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "convert_curve_to_polyline",
    "method_parameters": (("object","str","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT")),
    "method_returns": ("string","null")
    }
curve_arc_length_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_arc_length_point",
    "method_parameters": (("object","str","REQ"),("length","dbl","REQ"),("from_start","bln","OPT")),
    "method_returns": ("array","null")
    }
curve_area = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_area",
    "method_parameters": (("objects","array_of str","REQ")),
    "method_returns": ("array","number","number","null")
    }
curve_area_centroid = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_area_centroid",
    "method_parameters": (("objects","array_of str","REQ")),
    "method_returns": ("array","null")
    }
curve_arrows = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_arrows",
    "method_parameters": (("object","str","REQ"),("style","int","OPT")),
    "method_returns": ("number","number","null")
    }
curve_boolean_difference = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_boolean_difference",
    "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "method_returns": ("array","null")
    }
curve_boolean_intersection = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_boolean_intersection",
    "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "method_returns": ("array","null")
    }
curve_boolean_union = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_boolean_union",
    "method_parameters": (("curves","array_of str","REQ")),
    "method_returns": ("array","null")
    }
curve_brep_intersect = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_brep_intersect",
    "method_parameters": (("curve","str","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("array","null")
    }
curve_closest_object = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_closest_object",
    "method_parameters": (("curve","str","REQ"),("objects","array_of str","REQ")),
    "method_returns": ("array","string","array","array","null")
    }
curve_closest_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_closest_point",
    "method_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_contour_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_contour_points",
    "method_parameters": (("object","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT")),
    "method_returns": ("array","null")
    }
curve_curvature = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_curvature",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("array","number","null")
    }
curve_curve_intersection = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_curve_intersection",
    "method_parameters": (("object1","str","REQ"),("object2","str","OPT"),("tolerance","dbl","OPT")),
    "method_returns": ("array","number","number","number","number","number","null")
    }
curve_degree = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_degree",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_deviation = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_deviation",
    "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "method_returns": ("array","number","number","number","number","number","number","null")
    }
curve_dim = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_dim",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_directions_match = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_directions_match",
    "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ")),
    "method_returns": ("boolean","null")
    }
curve_discontinuity = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_discontinuity",
    "method_parameters": (("object","str","REQ"),("style","int","REQ")),
    "method_returns": ("array","null")
    }
curve_domain = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_domain",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_edit_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_edit_points",
    "method_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("index","int","OPT")),
    "method_returns": ("array","array","null")
    }
curve_end_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_end_point",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_evaluate = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_evaluate",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ")),
    "method_returns": ("array","array","array","array","array","null")
    }
curve_fillet_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_fillet_points",
    "method_parameters": (("curve0","str","REQ"),("curve1","str","REQ"),("radius","dbl","OPT"),("base_point0","array_of dbl","OPT"),("base_point1","array_of dbl","OPT")),
    "method_returns": ("array","string","null")
    }
curve_frame = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_frame",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("array","null")
    }
curve_knot_count = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_knot_count",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_knots = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_knots",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_length = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_length",
    "method_parameters": (("object","str","REQ"),("index","int","OPT"),("sub_domain","array_of int","OPT")),
    "method_returns": ("number","null")
    }
curve_mid_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_mid_point",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
curve_normal = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_normal",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
curve_perp_frame = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_perp_frame",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("array","null")
    }
curve_plane = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_plane",
    "method_parameters": (("curve","str","REQ")),
    "method_returns": ("array","null")
    }
curve_point_count = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_point_count",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_points",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_radius = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_radius",
    "method_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
curve_seam = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_seam",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("boolean","null")
    }
curve_start_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_start_point",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_surface_intersection = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_surface_intersection",
    "method_parameters": (("curve","str","REQ"),("surface","str","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
    "method_returns": ("array","number","number","number","number","number","number","number","null")
    }
curve_tangent = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_tangent",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
curve_weights = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "curve_weights",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
divide_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "divide_curve",
    "method_parameters": (("object","str","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "method_returns": ("array","array","null")
    }
divide_curve_equidistant = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "divide_curve_equidistant",
    "method_parameters": (("object","str","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "method_returns": ("array","array","null")
    }
divide_curve_length = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "divide_curve_length",
    "method_parameters": (("object","str","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "method_returns": ("array","array","null")
    }
ellipse_center_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "ellipse_center_point",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
ellipse_quad_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "ellipse_quad_points",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
evaluate_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "evaluate_curve",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
explode_curves = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "explode_curves",
    "method_parameters": (("objects","array_of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
extend_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "extend_curve",
    "method_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("objects","array_of str","REQ")),
    "method_returns": ("string","null")
    }
extend_curve_length = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "extend_curve_length",
    "method_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("length","dbl","REQ")),
    "method_returns": ("string","null")
    }
extend_curve_point = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "extend_curve_point",
    "method_parameters": (("object","str","REQ"),("side","int","REQ"),("point","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
fair_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "fair_curve",
    "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
fit_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "fit_curve",
    "method_parameters": (("object","str","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
    "method_returns": ("string","null")
    }
insert_curve_knot = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "insert_curve_knot",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT")),
    "method_returns": ("boolean","null")
    }
is_arc = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_arc",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_circle = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_circle",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_closable = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_closable",
    "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_closed = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_closed",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_in_plane = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_in_plane",
    "method_parameters": (("object","str","REQ"),("plane","array_of dbl","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_linear = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_linear",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_periodic = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_periodic",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_planar = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_planar",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_curve_rational = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_curve_rational",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_ellipse = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_ellipse",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_line = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_line",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_point_on_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_point_on_curve",
    "method_parameters": (("object","str","REQ"),("point","array_of int","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_poly_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_poly_curve",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_polyline = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "is_polyline",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("boolean","null")
    }
join_curves = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "join_curves",
    "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
line_fit_from_points = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "line_fit_from_points",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
make_curve_non_periodic = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "make_curve_non_periodic",
    "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","string","null")
    }
make_curve_periodic = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "make_curve_periodic",
    "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","string","null")
    }
mesh_polyline = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "mesh_polyline",
    "method_parameters": (("polyline","str","REQ")),
    "method_returns": ("string","null")
    }
offset_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "offset_curve",
    "method_parameters": (("object","str","REQ"),("direction","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT")),
    "method_returns": ("array","null")
    }
offset_curve_on_surface = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "offset_curve_on_surface",
    "method_parameters": (("curve","str","REQ"),("surface","str","REQ"),("distance","dbl","REQ")),
    "method_returns": ("array","null")
    }
offset_curve_on_surface_2 = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "offset_curve_on_surface_2",
    "method_parameters": (("curve","str","REQ"),("surface","str","REQ"),("parameter","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
planar_closed_curve_containment = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "planar_closed_curve_containment",
    "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "method_returns": ("number","null")
    }
planar_curve_collision = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "planar_curve_collision",
    "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "method_returns": ("null")
    }
point_in_planar_closed_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "point_in_planar_closed_curve",
    "method_parameters": (("point","array_of dbl","REQ"),("curve","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "method_returns": ("number","null")
    }
poly_curve_count = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "poly_curve_count",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("number","null")
    }
polyline_vertices = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "polyline_vertices",
    "method_parameters": (("object","str","REQ"),("index","int","OPT")),
    "method_returns": ("array","null")
    }
project_curve_to_mesh = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "project_curve_to_mesh",
    "method_parameters": (("curves","array_of str","REQ"),("meshes","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
project_curve_to_surface = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "project_curve_to_surface",
    "method_parameters": (("curves","array_of str","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
rebuild_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "rebuild_curve",
    "method_parameters": (("object","str","REQ"),("degree","int","OPT"),("point_count","int","OPT")),
    "method_returns": ("boolean","null")
    }
remove_curve_knot = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "remove_curve_knot",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("boolean","null")
    }
reverse_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "reverse_curve",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
simplify_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "simplify_curve",
    "method_parameters": (("object","str","REQ"),("flags","int","OPT")),
    "method_returns": ("boolean","null")
    }
split_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "split_curve",
    "method_parameters": (("object","str","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
trim_curve = {
    "method_location": "curve",
    "method_type": "FUNCTION",
    "method_name": "trim_curve",
    "method_parameters": (("object","str","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","null")
    }
