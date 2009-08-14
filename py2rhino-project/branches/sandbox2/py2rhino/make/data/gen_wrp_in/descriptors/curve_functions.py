#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_arc = {
    "function_location": "curve",
    "function_com_id": 651,
    "function_vb_name": "AddArc",
    "function_name": "add_arc",
    "function_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_arc_3_pt = {
    "function_location": "curve",
    "function_com_id": 82,
    "function_vb_name": "AddArc3Pt",
    "function_name": "add_arc_3_pt",
    "function_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_circle = {
    "function_location": "curve",
    "function_com_id": 83,
    "function_vb_name": "AddCircle",
    "function_name": "add_circle",
    "function_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_circle_3_pt = {
    "function_location": "curve",
    "function_com_id": 84,
    "function_vb_name": "AddCircle3Pt",
    "function_name": "add_circle_3_pt",
    "function_parameters": (("first","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_curve = {
    "function_location": "curve",
    "function_com_id": 77,
    "function_vb_name": "AddCurve",
    "function_name": "add_curve",
    "function_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT")),
    "function_returns": ("string","null")
    }
add_ellipse = {
    "function_location": "curve",
    "function_com_id": 679,
    "function_vb_name": "AddEllipse",
    "function_name": "add_ellipse",
    "function_parameters": (("plane","array_of dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_ellipse_3_pt = {
    "function_location": "curve",
    "function_com_id": 680,
    "function_vb_name": "AddEllipse3Pt",
    "function_name": "add_ellipse_3_pt",
    "function_parameters": (("center","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_fillet_curve = {
    "function_location": "curve",
    "function_com_id": 574,
    "function_vb_name": "AddFilletCurve",
    "function_name": "add_fillet_curve",
    "function_parameters": (("curve_0","str","REQ"),("curve_1","str","REQ"),("radius","dbl","OPT"),("point_0","array_of dbl","OPT"),("point_1","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_interp_crv_on_srf = {
    "function_location": "curve",
    "function_com_id": 513,
    "function_vb_name": "AddInterpCrvOnSrf",
    "function_name": "add_interp_crv_on_srf",
    "function_parameters": (("object","str","REQ"),("points","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_interp_crv_on_srf_u_v = {
    "function_location": "curve",
    "function_com_id": 641,
    "function_vb_name": "AddInterpCrvOnSrfUV",
    "function_name": "add_interp_crv_on_srf_u_v",
    "function_parameters": (("object","str","REQ"),("points","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_interp_curve = {
    "function_location": "curve",
    "function_com_id": 268,
    "function_vb_name": "AddInterpCurve",
    "function_name": "add_interp_curve",
    "function_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","array_of dbl","OPT"),("end_tan","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_interp_curve_ex = {
    "function_location": "curve",
    "function_com_id": 520,
    "function_vb_name": "AddInterpCurveEx",
    "function_name": "add_interp_curve_ex",
    "function_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","array_of dbl","OPT"),("end_tangent","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_line = {
    "function_location": "curve",
    "function_com_id": 70,
    "function_vb_name": "AddLine",
    "function_name": "add_line",
    "function_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_nurbs_curve = {
    "function_location": "curve",
    "function_com_id": 309,
    "function_vb_name": "AddNurbsCurve",
    "function_name": "add_nurbs_curve",
    "function_parameters": (("points","array_of dbl","REQ"),("knots","array_of dbl","REQ"),("degree","int","REQ"),("weights","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_polyline = {
    "function_location": "curve",
    "function_com_id": 85,
    "function_vb_name": "AddPolyline",
    "function_name": "add_polyline",
    "function_parameters": (("points","array_of dbl","REQ"),),
    "function_returns": ("string","null")
    }
add_sub_crv = {
    "function_location": "curve",
    "function_com_id": 681,
    "function_vb_name": "AddSubCrv",
    "function_name": "add_sub_crv",
    "function_parameters": (("object","str","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ")),
    "function_returns": ("string","null")
    }
arc_angle = {
    "function_location": "curve",
    "function_com_id": 86,
    "function_vb_name": "ArcAngle",
    "function_name": "arc_angle",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
arc_center_point = {
    "function_location": "curve",
    "function_com_id": 87,
    "function_vb_name": "ArcCenterPoint",
    "function_name": "arc_center_point",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("null",)
    }
arc_mid_point = {
    "function_location": "curve",
    "function_com_id": 88,
    "function_vb_name": "ArcMidPoint",
    "function_name": "arc_mid_point",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("null",)
    }
arc_radius = {
    "function_location": "curve",
    "function_com_id": 89,
    "function_vb_name": "ArcRadius",
    "function_name": "arc_radius",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
circle_center_point = {
    "function_location": "curve",
    "function_com_id": 90,
    "function_vb_name": "CircleCenterPoint",
    "function_name": "circle_center_point",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
circle_circumference = {
    "function_location": "curve",
    "function_com_id": 91,
    "function_vb_name": "CircleCircumference",
    "function_name": "circle_circumference",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
circle_radius = {
    "function_location": "curve",
    "function_com_id": 92,
    "function_vb_name": "CircleRadius",
    "function_name": "circle_radius",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
close_curve = {
    "function_location": "curve",
    "function_com_id": 440,
    "function_vb_name": "CloseCurve",
    "function_name": "close_curve",
    "function_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("string","null")
    }
convert_curve_to_polyline = {
    "function_location": "curve",
    "function_com_id": 377,
    "function_vb_name": "ConvertCurveToPolyline",
    "function_name": "convert_curve_to_polyline",
    "function_parameters": (("object","str","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT")),
    "function_returns": ("string","null")
    }
curve_arc_length_point = {
    "function_location": "curve",
    "function_com_id": 658,
    "function_vb_name": "CurveArcLengthPoint",
    "function_name": "curve_arc_length_point",
    "function_parameters": (("object","str","REQ"),("length","dbl","REQ"),("from_start","bln","OPT")),
    "function_returns": ("array","null")
    }
curve_area = {
    "function_location": "curve",
    "function_com_id": 643,
    "function_vb_name": "CurveArea",
    "function_name": "curve_area",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("array","number","number","null")
    }
curve_area_centroid = {
    "function_location": "curve",
    "function_com_id": 677,
    "function_vb_name": "CurveAreaCentroid",
    "function_name": "curve_area_centroid",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("array","null")
    }
curve_arrows = {
    "function_location": "curve",
    "function_com_id": 578,
    "function_vb_name": "CurveArrows",
    "function_name": "curve_arrows",
    "function_parameters": (("object","str","REQ"),("style","int","OPT")),
    "function_returns": ("number","number","null")
    }
curve_boolean_difference = {
    "function_location": "curve",
    "function_com_id": 811,
    "function_vb_name": "CurveBooleanDifference",
    "function_name": "curve_boolean_difference",
    "function_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "function_returns": ("array","null")
    }
curve_boolean_intersection = {
    "function_location": "curve",
    "function_com_id": 810,
    "function_vb_name": "CurveBooleanIntersection",
    "function_name": "curve_boolean_intersection",
    "function_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "function_returns": ("array","null")
    }
curve_boolean_union = {
    "function_location": "curve",
    "function_com_id": 809,
    "function_vb_name": "CurveBooleanUnion",
    "function_name": "curve_boolean_union",
    "function_parameters": (("curves","array_of str","REQ"),),
    "function_returns": ("array","null")
    }
curve_brep_intersect = {
    "function_location": "curve",
    "function_com_id": 545,
    "function_vb_name": "CurveBrepIntersect",
    "function_name": "curve_brep_intersect",
    "function_parameters": (("curve","str","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","null")
    }
curve_closest_object = {
    "function_location": "curve",
    "function_com_id": 870,
    "function_vb_name": "CurveClosestObject",
    "function_name": "curve_closest_object",
    "function_parameters": (("curve","str","REQ"),("objects","array_of str","REQ")),
    "function_returns": ("array","string","array","array","null")
    }
curve_closest_point = {
    "function_location": "curve",
    "function_com_id": 93,
    "function_vb_name": "CurveClosestPoint",
    "function_name": "curve_closest_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_contour_points = {
    "function_location": "curve",
    "function_com_id": 748,
    "function_vb_name": "CurveContourPoints",
    "function_name": "curve_contour_points",
    "function_parameters": (("object","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT")),
    "function_returns": ("array","null")
    }
curve_curvature = {
    "function_location": "curve",
    "function_com_id": 379,
    "function_vb_name": "CurveCurvature",
    "function_name": "curve_curvature",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("array","number","null")
    }
curve_curve_intersection = {
    "function_location": "curve",
    "function_com_id": 423,
    "function_vb_name": "CurveCurveIntersection",
    "function_name": "curve_curve_intersection",
    "function_parameters": (("object_1","str","REQ"),("object_2","str","OPT"),("tolerance","dbl","OPT")),
    "function_returns": ("array","number","number","number","number","number","null")
    }
curve_degree = {
    "function_location": "curve",
    "function_com_id": 94,
    "function_vb_name": "CurveDegree",
    "function_name": "curve_degree",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_deviation = {
    "function_location": "curve",
    "function_com_id": 687,
    "function_vb_name": "CurveDeviation",
    "function_name": "curve_deviation",
    "function_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
    "function_returns": ("array","number","number","number","number","number","number","null")
    }
curve_dim = {
    "function_location": "curve",
    "function_com_id": 381,
    "function_vb_name": "CurveDim",
    "function_name": "curve_dim",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_directions_match = {
    "function_location": "curve",
    "function_com_id": 543,
    "function_vb_name": "CurveDirectionsMatch",
    "function_name": "curve_directions_match",
    "function_parameters": (("curve_1","str","REQ"),("curve_2","str","REQ")),
    "function_returns": ("boolean","null")
    }
curve_discontinuity = {
    "function_location": "curve",
    "function_com_id": 579,
    "function_vb_name": "CurveDiscontinuity",
    "function_name": "curve_discontinuity",
    "function_parameters": (("object","str","REQ"),("style","int","REQ")),
    "function_returns": ("array","null")
    }
curve_domain = {
    "function_location": "curve",
    "function_com_id": 95,
    "function_vb_name": "CurveDomain",
    "function_name": "curve_domain",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_edit_points = {
    "function_location": "curve",
    "function_com_id": 442,
    "function_vb_name": "CurveEditPoints",
    "function_name": "curve_edit_points",
    "function_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("index","int","OPT")),
    "function_returns": ("array","array","null")
    }
curve_end_point = {
    "function_location": "curve",
    "function_com_id": 96,
    "function_vb_name": "CurveEndPoint",
    "function_name": "curve_end_point",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_evaluate = {
    "function_location": "curve",
    "function_com_id": 489,
    "function_vb_name": "CurveEvaluate",
    "function_name": "curve_evaluate",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ")),
    "function_returns": ("array","array","array","array","array","null")
    }
curve_fillet_points = {
    "function_location": "curve",
    "function_com_id": 572,
    "function_vb_name": "CurveFilletPoints",
    "function_name": "curve_fillet_points",
    "function_parameters": (("curve_0","str","REQ"),("curve_1","str","REQ"),("radius","dbl","OPT"),("base_point_0","array_of dbl","OPT"),("base_point_1","array_of dbl","OPT")),
    "function_returns": ("array","string","null")
    }
curve_frame = {
    "function_location": "curve",
    "function_com_id": 675,
    "function_vb_name": "CurveFrame",
    "function_name": "curve_frame",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("array","null")
    }
curve_knot_count = {
    "function_location": "curve",
    "function_com_id": 310,
    "function_vb_name": "CurveKnotCount",
    "function_name": "curve_knot_count",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_knots = {
    "function_location": "curve",
    "function_com_id": 311,
    "function_vb_name": "CurveKnots",
    "function_name": "curve_knots",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_length = {
    "function_location": "curve",
    "function_com_id": 97,
    "function_vb_name": "CurveLength",
    "function_name": "curve_length",
    "function_parameters": (("object","str","REQ"),("index","int","OPT"),("sub_domain","array_of int","OPT")),
    "function_returns": ("number","null")
    }
curve_mid_point = {
    "function_location": "curve",
    "function_com_id": 577,
    "function_vb_name": "CurveMidPoint",
    "function_name": "curve_mid_point",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
curve_normal = {
    "function_location": "curve",
    "function_com_id": 521,
    "function_vb_name": "CurveNormal",
    "function_name": "curve_normal",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
curve_perp_frame = {
    "function_location": "curve",
    "function_com_id": 676,
    "function_vb_name": "CurvePerpFrame",
    "function_name": "curve_perp_frame",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("array","null")
    }
curve_plane = {
    "function_location": "curve",
    "function_com_id": 609,
    "function_vb_name": "CurvePlane",
    "function_name": "curve_plane",
    "function_parameters": (("curve","str","REQ"),),
    "function_returns": ("array","null")
    }
curve_point_count = {
    "function_location": "curve",
    "function_com_id": 98,
    "function_vb_name": "CurvePointCount",
    "function_name": "curve_point_count",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_points = {
    "function_location": "curve",
    "function_com_id": 308,
    "function_vb_name": "CurvePoints",
    "function_name": "curve_points",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_radius = {
    "function_location": "curve",
    "function_com_id": 80,
    "function_vb_name": "CurveRadius",
    "function_name": "curve_radius",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
curve_seam = {
    "function_location": "curve",
    "function_com_id": 527,
    "function_vb_name": "CurveSeam",
    "function_name": "curve_seam",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("boolean","null")
    }
curve_start_point = {
    "function_location": "curve",
    "function_com_id": 99,
    "function_vb_name": "CurveStartPoint",
    "function_name": "curve_start_point",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_surface_intersection = {
    "function_location": "curve",
    "function_com_id": 424,
    "function_vb_name": "CurveSurfaceIntersection",
    "function_name": "curve_surface_intersection",
    "function_parameters": (("curve","str","REQ"),("surface","str","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
    "function_returns": ("array","number","number","number","number","number","number","number","null")
    }
curve_tangent = {
    "function_location": "curve",
    "function_com_id": 363,
    "function_vb_name": "CurveTangent",
    "function_name": "curve_tangent",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
curve_weights = {
    "function_location": "curve",
    "function_com_id": 314,
    "function_vb_name": "CurveWeights",
    "function_name": "curve_weights",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
divide_curve = {
    "function_location": "curve",
    "function_com_id": 78,
    "function_vb_name": "DivideCurve",
    "function_name": "divide_curve",
    "function_parameters": (("object","str","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "function_returns": ("array","array","null")
    }
divide_curve_equidistant = {
    "function_location": "curve",
    "function_com_id": 913,
    "function_vb_name": "DivideCurveEquidistant",
    "function_name": "divide_curve_equidistant",
    "function_parameters": (("object","str","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "function_returns": ("array","array","null")
    }
divide_curve_length = {
    "function_location": "curve",
    "function_com_id": 374,
    "function_vb_name": "DivideCurveLength",
    "function_name": "divide_curve_length",
    "function_parameters": (("object","str","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
    "function_returns": ("array","array","null")
    }
ellipse_center_point = {
    "function_location": "curve",
    "function_com_id": 524,
    "function_vb_name": "EllipseCenterPoint",
    "function_name": "ellipse_center_point",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
ellipse_quad_points = {
    "function_location": "curve",
    "function_com_id": 525,
    "function_vb_name": "EllipseQuadPoints",
    "function_name": "ellipse_quad_points",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
evaluate_curve = {
    "function_location": "curve",
    "function_com_id": 100,
    "function_vb_name": "EvaluateCurve",
    "function_name": "evaluate_curve",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
explode_curves = {
    "function_location": "curve",
    "function_com_id": 446,
    "function_vb_name": "ExplodeCurves",
    "function_name": "explode_curves",
    "function_parameters": (("objects","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
extend_curve = {
    "function_location": "curve",
    "function_com_id": 438,
    "function_vb_name": "ExtendCurve",
    "function_name": "extend_curve",
    "function_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("objects","array_of str","REQ")),
    "function_returns": ("string","null")
    }
extend_curve_length = {
    "function_location": "curve",
    "function_com_id": 436,
    "function_vb_name": "ExtendCurveLength",
    "function_name": "extend_curve_length",
    "function_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("length","dbl","REQ")),
    "function_returns": ("string","null")
    }
extend_curve_point = {
    "function_location": "curve",
    "function_com_id": 437,
    "function_vb_name": "ExtendCurvePoint",
    "function_name": "extend_curve_point",
    "function_parameters": (("object","str","REQ"),("side","int","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
fair_curve = {
    "function_location": "curve",
    "function_com_id": 599,
    "function_vb_name": "FairCurve",
    "function_name": "fair_curve",
    "function_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
fit_curve = {
    "function_location": "curve",
    "function_com_id": 813,
    "function_vb_name": "FitCurve",
    "function_name": "fit_curve",
    "function_parameters": (("object","str","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
    "function_returns": ("string","null")
    }
insert_curve_knot = {
    "function_location": "curve",
    "function_com_id": 515,
    "function_vb_name": "InsertCurveKnot",
    "function_name": "insert_curve_knot",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT")),
    "function_returns": ("boolean","null")
    }
is_arc = {
    "function_location": "curve",
    "function_com_id": 101,
    "function_vb_name": "IsArc",
    "function_name": "is_arc",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_circle = {
    "function_location": "curve",
    "function_com_id": 102,
    "function_vb_name": "IsCircle",
    "function_name": "is_circle",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve = {
    "function_location": "curve",
    "function_com_id": 103,
    "function_vb_name": "IsCurve",
    "function_name": "is_curve",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_closable = {
    "function_location": "curve",
    "function_com_id": 441,
    "function_vb_name": "IsCurveClosable",
    "function_name": "is_curve_closable",
    "function_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_closed = {
    "function_location": "curve",
    "function_com_id": 104,
    "function_vb_name": "IsCurveClosed",
    "function_name": "is_curve_closed",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_in_plane = {
    "function_location": "curve",
    "function_com_id": 483,
    "function_vb_name": "IsCurveInPlane",
    "function_name": "is_curve_in_plane",
    "function_parameters": (("object","str","REQ"),("plane","array_of dbl","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_linear = {
    "function_location": "curve",
    "function_com_id": 105,
    "function_vb_name": "IsCurveLinear",
    "function_name": "is_curve_linear",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_periodic = {
    "function_location": "curve",
    "function_com_id": 106,
    "function_vb_name": "IsCurvePeriodic",
    "function_name": "is_curve_periodic",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_planar = {
    "function_location": "curve",
    "function_com_id": 107,
    "function_vb_name": "IsCurvePlanar",
    "function_name": "is_curve_planar",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_curve_rational = {
    "function_location": "curve",
    "function_com_id": 380,
    "function_vb_name": "IsCurveRational",
    "function_name": "is_curve_rational",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_ellipse = {
    "function_location": "curve",
    "function_com_id": 523,
    "function_vb_name": "IsEllipse",
    "function_name": "is_ellipse",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_line = {
    "function_location": "curve",
    "function_com_id": 108,
    "function_vb_name": "IsLine",
    "function_name": "is_line",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_point_on_curve = {
    "function_location": "curve",
    "function_com_id": 318,
    "function_vb_name": "IsPointOnCurve",
    "function_name": "is_point_on_curve",
    "function_parameters": (("object","str","REQ"),("point","array_of int","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_poly_curve = {
    "function_location": "curve",
    "function_com_id": 368,
    "function_vb_name": "IsPolyCurve",
    "function_name": "is_poly_curve",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_polyline = {
    "function_location": "curve",
    "function_com_id": 110,
    "function_vb_name": "IsPolyline",
    "function_name": "is_polyline",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("boolean","null")
    }
join_curves = {
    "function_location": "curve",
    "function_com_id": 111,
    "function_vb_name": "JoinCurves",
    "function_name": "join_curves",
    "function_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
line_fit_from_points = {
    "function_location": "curve",
    "function_com_id": 726,
    "function_vb_name": "LineFitFromPoints",
    "function_name": "line_fit_from_points",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
make_curve_non_periodic = {
    "function_location": "curve",
    "function_com_id": 925,
    "function_vb_name": "MakeCurveNonPeriodic",
    "function_name": "make_curve_non_periodic",
    "function_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","string","null")
    }
make_curve_periodic = {
    "function_location": "curve",
    "function_com_id": 444,
    "function_vb_name": "MakeCurvePeriodic",
    "function_name": "make_curve_periodic",
    "function_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","string","null")
    }
mesh_polyline = {
    "function_location": "curve",
    "function_com_id": 546,
    "function_vb_name": "MeshPolyline",
    "function_name": "mesh_polyline",
    "function_parameters": (("polyline","str","REQ"),),
    "function_returns": ("string","null")
    }
offset_curve = {
    "function_location": "curve",
    "function_com_id": 634,
    "function_vb_name": "OffsetCurve",
    "function_name": "offset_curve",
    "function_parameters": (("object","str","REQ"),("direction","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT")),
    "function_returns": ("array","null")
    }
offset_curve_on_surface = {
    "function_location": "curve",
    "function_com_id": 906,
    "function_vb_name": "OffsetCurveOnSurface",
    "function_name": "offset_curve_on_surface",
    "function_parameters": (("curve","str","REQ"),("surface","str","REQ"),("distance","dbl","REQ")),
    "function_returns": ("array","null")
    }
offset_curve_on_surface_2 = {
    "function_location": "curve",
    "function_com_id": 906,
    "function_vb_name": "OffsetCurveOnSurface",
    "function_name": "offset_curve_on_surface_2",
    "function_parameters": (("curve","str","REQ"),("surface","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
planar_closed_curve_containment = {
    "function_location": "curve",
    "function_com_id": 480,
    "function_vb_name": "PlanarClosedCurveContainment",
    "function_name": "planar_closed_curve_containment",
    "function_parameters": (("curve_1","str","REQ"),("curve_2","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "function_returns": ("number","null")
    }
planar_curve_collision = {
    "function_location": "curve",
    "function_com_id": 481,
    "function_vb_name": "PlanarCurveCollision",
    "function_name": "planar_curve_collision",
    "function_parameters": (("curve_1","str","REQ"),("curve_2","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "function_returns": ("null",)
    }
point_in_planar_closed_curve = {
    "function_location": "curve",
    "function_com_id": 482,
    "function_vb_name": "PointInPlanarClosedCurve",
    "function_name": "point_in_planar_closed_curve",
    "function_parameters": (("point","array_of dbl","REQ"),("curve","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT")),
    "function_returns": ("number","null")
    }
poly_curve_count = {
    "function_location": "curve",
    "function_com_id": 369,
    "function_vb_name": "PolyCurveCount",
    "function_name": "poly_curve_count",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
polyline_vertices = {
    "function_location": "curve",
    "function_com_id": 112,
    "function_vb_name": "PolylineVertices",
    "function_name": "polyline_vertices",
    "function_parameters": (("object","str","REQ"),("index","int","OPT")),
    "function_returns": ("array","null")
    }
project_curve_to_mesh = {
    "function_location": "curve",
    "function_com_id": 911,
    "function_vb_name": "ProjectCurveToMesh",
    "function_name": "project_curve_to_mesh",
    "function_parameters": (("curves","array_of str","REQ"),("meshes","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
project_curve_to_surface = {
    "function_location": "curve",
    "function_com_id": 891,
    "function_vb_name": "ProjectCurveToSurface",
    "function_name": "project_curve_to_surface",
    "function_parameters": (("curves","array_of str","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
rebuild_curve = {
    "function_location": "curve",
    "function_com_id": 814,
    "function_vb_name": "RebuildCurve",
    "function_name": "rebuild_curve",
    "function_parameters": (("object","str","REQ"),("degree","int","OPT"),("point_count","int","OPT")),
    "function_returns": ("boolean","null")
    }
remove_curve_knot = {
    "function_location": "curve",
    "function_com_id": 916,
    "function_vb_name": "RemoveCurveKnot",
    "function_name": "remove_curve_knot",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("boolean","null")
    }
reverse_curve = {
    "function_location": "curve",
    "function_com_id": 542,
    "function_vb_name": "ReverseCurve",
    "function_name": "reverse_curve",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
simplify_curve = {
    "function_location": "curve",
    "function_com_id": 573,
    "function_vb_name": "SimplifyCurve",
    "function_name": "simplify_curve",
    "function_parameters": (("object","str","REQ"),("flags","int","OPT")),
    "function_returns": ("boolean","null")
    }
split_curve = {
    "function_location": "curve",
    "function_com_id": 504,
    "function_vb_name": "SplitCurve",
    "function_name": "split_curve",
    "function_parameters": (("object","str","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
trim_curve = {
    "function_location": "curve",
    "function_com_id": 505,
    "function_vb_name": "TrimCurve",
    "function_name": "trim_curve",
    "function_parameters": (("object","str","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","null")
    }
