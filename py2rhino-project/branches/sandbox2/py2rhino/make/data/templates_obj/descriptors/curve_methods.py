#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here
         
#===============================================================================
# NurbsCurve
#===============================================================================

#constructors

add_curve = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_curve_by_points",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}
add_nurbs_curve = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_curve",
    "method_parameters": (("points","array_of dbl","REQ"),("knots","array_of int","REQ"),("degree","int","REQ"),("weights","array_of int","OPT"),),
    "method_returns": ("_Object._CurveType.NurbsCurve","null")
}
add_fillet_curve = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_fillet_curve",
    "method_parameters": (("curve_0","_Object._CurveType.NurbsCurve","REQ"),("curve_1","_Object._CurveType.NurbsCurve","REQ"),("radius","dbl","OPT"),("point_0","array_of dbl","OPT"),("point_1","array_of dbl","OPT"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}
add_interp_crv_on_srf = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_interp_curve_on_srf",
    "method_parameters": (("surface","_Object._CurveType.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}
add_interp_crv_on_srf_u_v = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_interp_curve_on_srf_uv",
    "method_parameters": (("surface","_Object._CurveType.NurbsCurve","REQ"),("points","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}
add_interp_curve = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_interp_curve",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","array_of dbl","OPT"),("end_tan","array_of dbl","OPT"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}
add_interp_curve_ex = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_interp_curve_ex",
    "method_parameters": (("points","array_of dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","array_of dbl","OPT"),("end_tangent","array_of dbl","OPT"),),
    "method_returns": ("_Object._CurveType.Curve","null")
}    
add_sub_crv = {#ed
    "method_location": "_Object._Curve.NurbsCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_sub_curve",
    "method_parameters": (("curve","_Object._CurveType.NurbsCurve","REQ"),("param_0","dbl","REQ"),("param_1","dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Curve","null")
} 

#methods

#... none, they are all in the _Object class

#===============================================================================
# Arc
#===============================================================================
     
#constructors

add_arc = {#ed
    "method_location": "_Object._Curve.Arc",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_arc",
    "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Arc","null")
}
add_arc_3_pt = {#ed
    "method_location": "_Object._Curve.Arc",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_arc_3pt",
    "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Arc","null")
}

#===============================================================================
# ArcAttributes
#===============================================================================

arc_angle = {#ed
    "method_location": "_Object._Curve.ArcAttributes",
    "method_type": "METHOD",
    "method_name": "angle",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
arc_center_point = {#ed
    "method_location": "_Object._Curve.ArcAttributes",
    "method_type": "METHOD",
    "method_name": "center_point",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
arc_mid_point = {#ed
    "method_location": "_Object._Curve.ArcAttributes",
    "method_type": "METHOD",
    "method_name": "mid_point",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
arc_radius = {#ed
    "method_location": "_Object._Curve.ArcAttributes",
    "method_type": "METHOD",
    "method_name": "radius",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}

#===============================================================================
# Circle
#===============================================================================

#constructors

add_circle = {#ed
    "method_location": "_Object._Curve.Circle",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_circle",
    "method_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Circle","null")
}
add_circle_3_pt = {#ed
    "method_location": "_Object._Curve.Circle",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_circle_3pt",
    "method_parameters": (("first","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Circle","null")
}

#===============================================================================
# CircleAttributes
#===============================================================================

circle_center_point = {#ed
    "method_location": "_Object._Curve.CircleAttributes",
    "method_type": "METHOD",
    "method_name": "center_point",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
circle_circumference = {#ed
    "method_location": "_Object._Curve.CircleAttributes",
    "method_type": "METHOD",
    "method_name": "circumference",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
circle_radius = {#ed
    "method_location": "_Object._Curve.CircleAttributes",
    "method_type": "METHOD",
    "method_name": "radius",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
#===============================================================================
# Ellipse
#===============================================================================

#constructors

add_ellipse = {#ed
    "method_location": "_Object._Curve.Ellipse",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_ellipse",
    "method_parameters": (("plane","array_of dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Ellipse","null")
}
add_ellipse_3_pt = {#ed
    "method_location": "_Object._Curve.Ellipse",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_ellipse_3pt",
    "method_parameters": (("center","array_of dbl","REQ"),("second","array_of dbl","REQ"),("third","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Ellipse","null")
}

#===============================================================================
# EllipseAttributes
#===============================================================================

ellipse_center_point = {#ed
    "method_location": "_Object._Curve.EllipseAttributes",
    "method_type": "METHOD",
    "method_name": "center_point",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
}
ellipse_quad_points = {#ed
    "method_location": "_Object._Curve.EllipseAttributes",
    "method_type": "METHOD",
    "method_name": "quad_points",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
} 
#===============================================================================
# Line
#===============================================================================

#constructors

add_line = {#ed
    "method_location": "_Object._Curve.Line",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_line",
    "method_parameters": (("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType.Line","null")
}

#===============================================================================
# LineAttributes
#===============================================================================

#how about the start and end points - that might be useful

#===============================================================================
# Polyline
#===============================================================================

#constructors

add_polyline = {#ed
    "method_location": "_Object._Curve.Polyline",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_polyline",
    "method_parameters": (("points","array_of dbl","REQ"),),
    "method_returns": ("Polyline","null")
}
convert_curve_to_polyline = {#ed
    "method_location": "_Object._Curve.Polyline",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_polyline_from_curve",
    "method_parameters": (("curve","_Object._Curve","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT"),),
    "method_returns": ("_Object._CurveType","null")
} 
#===============================================================================
# PolylineAttributes
#===============================================================================

polyline_vertices = {#ed
    "method_location": "_Object._Curve.PolylineAttributes",
    "method_type": "METHOD",
    "method_name": "vertices",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl.Polyline","null")
}
#===============================================================================
# PolyCurve
#===============================================================================

#constructors

join_curves = {#ed
    "method_location": "_Object._Curve.PolyCurve",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_polycurve",
    "method_parameters": (("curves","array_of _Object._CurveType.Curve","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._CurveType","null")
}

#methods

poly_curve_count = {#ed
    "method_location": "_Object._Curve.PolyCurve",
    "method_type": "METHOD",
    "method_name": "count",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
#===============================================================================
# CurveType
#===============================================================================

#methods

is_arc = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_arc",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_circle = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_circle",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_ellipse = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_ellipse",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
}
is_line = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_line",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_poly_curve = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_poly_curve",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_polyline = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_polyline",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}


#===============================================================================
# CurveType
#===============================================================================

is_curve_in_plane = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "in_plane",
    "method_parameters": (("","self","REQ"),("plane","array_of dbl","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_closable = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_closable",
    "method_parameters": (("","self","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_closed = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_closed",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_linear = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_linear",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_periodic = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_periodic",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_planar = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_planar",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_curve_rational = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_curve_rational",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
is_point_on_curve = {#ed
    "method_location": "_Object._Curve.CurveType",
    "method_type": "METHOD",
    "method_name": "is_point_on_curve",
    "method_parameters": (("","self","REQ"),("point","array_of int","REQ"),("index","int","OPT"),),
    "method_returns": ("boolean","null")
}
#===============================================================================
# CurveModify
#===============================================================================


curve_seam = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "seam",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("boolean","null")
}
fair_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "fair_curve",
    "method_parameters": (("","self","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("boolean","null")
}
insert_curve_knot = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "insert_curve_knot",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT"),),
    "method_returns": ("boolean","null")
}
project_curve_to_mesh = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "project_curve_to_mesh",
    "method_parameters": (("curves","array_of _Object","REQ"),("meshes","array_of str","REQ"),("direction","array_of dbl","REQ"),),
    "method_returns": ("array_of dbl","null")
}
rebuild_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "rebuild_curve",
    "method_parameters": (("","self","REQ"),("degree","int","OPT"),("point_count","int","OPT"),),
    "method_returns": ("boolean","null")
}
remove_curve_knot = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "remove_curve_knot",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("boolean","null")
}
reverse_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "reverse_curve",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
}
simplify_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "simplify_curve",
    "method_parameters": (("","self","REQ"),("flags","int","OPT"),),
    "method_returns": ("boolean","null")
}

#methods that return curves
#the curves returned will be a modified version of the input curve - the id is the same
#why this inconsistency??

close_curve = {# this only makes sense on open curves - so exclude form circle etc
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "close_curve",
    "method_parameters": (("","self","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("_Object._CurveType","null")
}
extend_curve = {#ed - open curves only
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "extend_curve",
    "method_parameters": (("","self","REQ"),("type","int","REQ"),("side","int","REQ"),("objects","array_of str","REQ"),),
    "method_returns": ("_Object._CurveType","null")
}
extend_curve_length = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "extend_curve_length",
    "method_parameters": (("","self","REQ"),("type","int","REQ"),("side","int","REQ"),("length","dbl","REQ"),),
    "method_returns": ("_Object._CurveType","null")
}
extend_curve_point = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "extend_curve_point",
    "method_parameters": (("","self","REQ"),("side","int","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("_Object._CurveType","null")
}
fit_curve = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "fit_curve",
    "method_parameters": (("","self","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
    "method_returns": ("_Object._CurveType","null")
}
make_curve_non_periodic = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "make_curve_non_periodic",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._CurveType","_Object._CurveType","null")
}
make_curve_periodic = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "make_curve_periodic",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._CurveType","_Object._CurveType","null")
}
trim_curve = {#ed
    "method_location": "_Object._CurveType.CurveModify",
    "method_type": "METHOD",
    "method_name": "trim_curve",
    "method_parameters": (("","self","REQ"),("interval","array_of int","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._CurveType","null")
}


#===============================================================================
# Curve ??????
#===============================================================================
#return arrays of curves

split_curve = {#this has the delete parameter
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "split_curve",
    "method_parameters": (("","self","REQ"),("parameters","array_of dbl","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
explode_curves = {#this has the delete parameter
    0: {                  
    "method_location": "Document",
    "method_type": "FUNCTION",
    "method_name": "curves_explode",
    "method_parameters": (("objects","array_of _Object","REQ"),("delete","bln","OPT"),),###
    "method_returns": ("array_of _Object._CurveType","null")
    },
    1: {
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "explode",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT"),),###
    "method_returns": ("array_of _Object._CurveType","null")
    }
}

offset_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "offset_curve",
    "method_parameters": (("","self","REQ"),("direction","array_of dbl","REQ"),("distance","dbl","REQ"),("normal","array_of dbl","OPT"),("style","int","OPT"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
offset_curve_on_surface = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "offset_curve_on_surface",
    "method_parameters": (("","self","REQ"),("surface","str","REQ"),("distance","dbl","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
curve_fillet_points = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "fillet_points",
    "method_parameters": (("","self","REQ"),("curve_0","str","REQ"),("radius","dbl","OPT"),("base_point_0","array_of dbl","OPT"),("base_point__1","array_of dbl","OPT"),),
    "method_returns": ("array_of (array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl, array_of dbl)","_Object._CurveType","null")
}
project_curve_to_surface = {#split
    0: {
    "method_location": "Document",
    "method_type": "FUNCTION",
    "method_name": "curves_project_to_surface",
    "method_parameters": (("curves","array_of _Object","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ"),),###
    "method_returns": ("array_of _Object._CurveType","null")
    },
    1: {
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "project_to_surface",
    "method_parameters": (("","self","REQ"),("surfaces","array_of str","REQ"),("direction","array_of dbl","REQ"),),###
    "method_returns": ("array_of _Object._CurveType","null")
    }
}

#===============================================================================
# CurveAttributes
#===============================================================================
curve_domain = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "domain",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
curve_degree = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "degree",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_edit_points = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "edit_points",
    "method_parameters": (("","self","REQ"),("return_parameters","bln","OPT"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
}
curve_end_point = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "end_point",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_knot_count = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "knot_count",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_knots = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "knots",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_arrows = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "arrows",
    "method_parameters": (("","self","REQ"),("style","int","OPT"),),
    "method_returns": ("number","number","null")
}
curve_dim = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "dim",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_discontinuity = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "discontinuity",
    "method_parameters": (("","self","REQ"),("style","int","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_length = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "length",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),("sub_domain","array_of int","OPT"),),
    "method_returns": ("number","null")
}
curve_mid_point = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "mid_point",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_normal = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "normal",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_plane = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_plane",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_point_count = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_point_count",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_points = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_points",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_start_point = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "start_point",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_weights = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "weights",
    "method_parameters": (("","self","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
#===============================================================================
# CurveIntersectionFunctions
#===============================================================================
curve_brep_intersect = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "brep_intersection",
    "method_parameters": (("","self","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
curve_curve_intersection = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_intersection",
    "method_parameters": (("","self","REQ"),("object_1","str","OPT"),("tolerance","dbl","OPT"),),
    "method_returns": ("array_of (int, array_of dbl, array_of dbl, array_of dbl, array_of dbl, int, int, int, int","null")
}
curve_surface_intersection = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "surface_intersection",
    "method_parameters": (("","self","REQ"),("surface","str","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT"),),
    "method_returns": ("array_of (int, array_of dbl, array_of dbl, array_of dbl, array_of dbl, int, int, int, int)","null")
}



#===============================================================================
# CurveBooleanFunctions
#===============================================================================

curve_boolean_difference = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "boolean_difference",
    "method_parameters": (("","self","REQ"),("curve","str","REQ"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
curve_boolean_intersection = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "boolean_intersection",
    "method_parameters": (("","self","REQ"),("curve_a","str","REQ"),),
    "method_returns": ("array_of _Object._CurveType","null")
}
curve_boolean_union = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "FUNCTION",
    "method_name": "boolean_union",
    "method_parameters": (("curves","array_of _Object","REQ"),),#there is no self parameter
    "method_returns": ("array_of _Object._CurveType","null")
}


#===============================================================================
# CurveGeneralFunctions
#===============================================================================
divide_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "divide_curve",
    "method_parameters": (("","self","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
}
divide_curve_equidistant = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "divide_curve_equidistant",
    "method_parameters": (("","self","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
}
divide_curve_length = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "divide_curve_length",
    "method_parameters": (("","self","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
}

curve_closest_object = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "closest_object",
    "method_parameters": (("","self","REQ"),("objects","array_of _Object","REQ"),),
    "method_returns": ("array_of (_Object._CurveType, array_of dbl, array_of dbl)","null")
}
curve_closest_point = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "closest_point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_arc_length_point = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_arc_length_point",
    "method_parameters": (("","self","REQ"),("length","dbl","REQ"),("from_start","bln","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_contour_points = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "contour_points",
    "method_parameters": (("","self","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_radius = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "radius",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),("index","int","OPT"),),
    "method_returns": ("number","null")
}
curve_deviation = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "deviation",
    "method_parameters": (("","self","REQ"),("curve_a","str","REQ"),),
    "method_returns": ("array_of (int, int, int, int, int, int)","number","null")
}
line_fit_from_points = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "line_fit_from_points",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_directions_match = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "directions_match",
    "method_parameters": (("","self","REQ"),("curve_1","str","REQ"),),
    "method_returns": ("boolean","null")
}

planar_curve_collision = {#ed - maybe this should go to the intersections
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "planar_curve_collision",
    "method_parameters": (("","self","REQ"),("curve_0","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
    "method_returns": ("bln","null")
}

#closed curves

curve_area = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "area",
    "method_parameters": (("","array_of _Object","REQ"),),
    "method_returns": ("array_of (int, int)","number","number","null")
}
curve_area_centroid = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curve_area_centroid",
    "method_parameters": (("objects","array_of _Object","REQ"),),
    "method_returns": ("array_of (dbl, dbl)","null")
}
point_in_planar_closed_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "point_in_planar_closed_curve",
    "method_parameters": (("point","array_of dbl","REQ"),("curve","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
    "method_returns": ("number","null")
}
planar_closed_curve_containment = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "planar_closed_curve_containment",
    "method_parameters": (("","self","REQ"),("curve__1","str","REQ"),("plane","array_of dbl","OPT"),("tolerance","dbl","OPT"),),
    "method_returns": ("number","null")
}



#===============================================================================
# CurveTFunctions
#===============================================================================
curve_evaluate = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "evaluate_derivatives",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ"),),
    "method_returns": ("array_of (array_of dbl, array_of dbl, array_of dbl, array_of dbl)","null")
}
evaluate_curve = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "evaluate",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}
curve_frame = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "frame",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("array_of (array_of dbl, array_of dbl, array_of dbl, array_of dbl","null")
}
curve_curvature = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "curvature",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("array_of (array_of dbl), (array_of dbl), (array_of dbl), (array_of dbl), (array_of dbl)","number","null")
}
curve_perp_frame = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "perp_frame",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("array_of dbl","null")
}
curve_tangent = {#ed
    "method_location": "_Object._CurveType",
    "method_type": "METHOD",
    "method_name": "tangent",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("index","int","OPT"),),
    "method_returns": ("array_of dbl","null")
}

#===============================================================================
# Mesh
#===============================================================================

mesh_polyline = {#ed
    "method_location": "_Object._MeshType.Mesh",
    "method_type": "CONSTRUCTOR",
    "method_name": "mesh",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("_Object._CurveType.Polyline","null")
}
