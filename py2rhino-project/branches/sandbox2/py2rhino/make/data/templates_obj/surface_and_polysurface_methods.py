#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

#===============================================================================
# PolySurface
#===============================================================================
add_box = {#ed
    "method_location": "_Object._SurfaceType.Polysurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("corners","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType.Polysurface","null")
    }
explode_polysurfaces = {#ed
    "method_location": "_Object._SurfaceType.Polysurface",
    "method_type": "METHOD",
    "method_name": "explode_polysurfaces",
    "method_parameters": (("objects","array_of _Object","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType.Polysurface","null")
    }
#===============================================================================
# Cone
#===============================================================================
add_cone = {#ed
    "method_location": "_Object._SurfaceType.Cone",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_cone",
    "method_parameters": (("base","array_of dbl","REQ"),("plane","array_of dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType.Cone","null")
    }
surface_cone = {#ed
    "method_location": "_Object._SurfaceType.Cone",
    "method_type": "METHOD",
    "method_name": "definition",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl, int,int)","null")
    }
#===============================================================================
# NurbsSurface
#===============================================================================
add_cut_plane = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "cut_plane",
    "method_parameters": (("objects","array_of__Object","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("normal","array_of dbl","OPT"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_edge_srf = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "edge_srf",
    "method_parameters": (("objects","array_of__Object","REQ"),),
    "method_returns": ("_Object._SurfaceType.Surface","null")
    }
add_loft_srf = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "loft_srf",
    "method_parameters": (("objects","array_of _Object","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType.Surface","null")
    }
add_nurbs_surface = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("point_count","array_of int","REQ"),("points","array_of dbl","REQ"),("knots_u","array_of int","REQ"),("knots_v","array_of int","REQ"),("degree","array_of int","REQ"),("weights","array_of int","REQ"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_planar_srf = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "planar_srf",
    "method_parameters": (("objects","array_of__Object","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType.NurbsSurface","null")
    }
add_rail_rev_srf = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "rail_rev_srf",
    "method_parameters": (("","self","REQ"),("rail","str","REQ"),("axis","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_rev_srf = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "rev_srf",
    "method_parameters": (("","self","REQ"),("axis","array_of dbl","REQ"),("start_angle","dbl","OPT"),("end_angle","dbl","OPT"),),
    "method_returns": ("_Object._SurfaceType.Surface","null")
    }
add_srf_contour_crvs = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "srf_contour_crvs",
    "method_parameters": (("","self","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("plane","array_of dbl","REQ"),("interval","dbl","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType.NurbsSurface","null")
    }
add_srf_control_pt_grid = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "srf_control_pt_grid",
    "method_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of dbl","OPT"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_srf_pt = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "srf_pt",
    "method_parameters": (("points","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_srf_pt_grid = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "srf_pt_grid",
    "method_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of int","OPT"),("closed","array_of bln","OPT"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
add_srf_section_crvs = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "srf_section_crvs",
    "method_parameters": (("","self","REQ"),("plane","array_of dbl","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType.NurbsSurface","null")
    }
add_sweep_1 = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "sweep_1",
    "method_parameters": (("","self","REQ"),("shapes","array_of str","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType.NurbsSurface","null")
    }
add_sweep_2 = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "sweep_2",
    "method_parameters": (("rails","array_of _Object","REQ"),("shapes","array_of _Object","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType.NurbsSurface","null")
    }
#===============================================================================
# Cylinder
#===============================================================================
add_cylinder = {#ed
    "method_location": "_Object._SurfaceType.Cylinder",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("base","array_of dbl","REQ"),("plane","array_of dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType.Cylinder","null")
    }
surface_cylinder = {#ed
    "method_location": "_Object._SurfaceType.Cylinder",
    "method_type": "METHOD",
    "method_name": "surface_cylinder",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType.Cylinder","null")
    }
#===============================================================================
# PlaneSurface
#===============================================================================
add_plane_surface = {#ed
    "method_location": "_Object._SurfaceType.NurbsSurface",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType.NurbsSurface","null")
    }
#===============================================================================
# Sphere
#===============================================================================
add_sphere = {#ed
    "method_location": "_Object._SurfaceType.Sphere",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("center","array_of dbl","REQ"),("plane","array_of dbl","REQ"),("radius","dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType.Sphere","null")
    }

surface_sphere = {#ed
    "method_location": "_Object._SurfaceType.Sphere",
    "method_type": "METHOD",
    "method_name": "surface_sphere",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl, int)","null")
    }
#===============================================================================
# Torus
#===============================================================================
add_torus = {#ed
    "method_location": "_Object._SurfaceType.Torus",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("base","array_of _Object","REQ"),("plane","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","array_of dbl","OPT"),),
    "method_returns": ("_Object._SurfaceType.Torus","null")
    }
surface_torus = {#ed
    "method_location": "_Object._SurfaceType.Torus",
    "method_type": "METHOD",
    "method_name": "surface_torus",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType.Torus","null")
    }
#===============================================================================
# _Object
#===============================================================================
is_brep = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_brep",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_brep_manifold = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_brep_manifold",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_cone = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_cone",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_cylinder = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_cylinder",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_parameter_on_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_parameter_on_surface",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
is_plane_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_plane_surface",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_point_in_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point_in_surface",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
is_point_on_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point_on_surface",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
is_poly_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_poly_surface",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_poly_surface_closed = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_poly_surface_closed",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_poly_surface_planar = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_poly_surface_planar",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_sphere = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_sphere",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface_closed = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_closed",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface_periodic = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_periodic",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface_planar = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_planar",
    "method_parameters": (("","self","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("boolean","null")
    }
is_surface_rational = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_rational",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface_singular = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_singular",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),),
    "method_returns": ("boolean","null")
    }
is_surface_trimmed = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_surface_trimmed",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_torus = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_torus",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
#===============================================================================
# _SurfaceType
#===============================================================================
extrude_curve = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "extrude_curve",
    "method_parameters": (("","self","REQ"),("path","str","REQ"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
extrude_curve_point = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "extrude_curve_point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
extrude_curve_straight = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "extrude_curve_straight",
    "method_parameters": (("","self","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
extrude_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "extrude_surface",
    "method_parameters": (("","self","REQ"),("curve","str","REQ"),("cap","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
fit_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "fit_surface",
    "method_parameters": (("","self","REQ"),("degree","array_of int","OPT"),("tolerance","dbl","OPT"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
join_surfaces = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "join_surfaces",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
make_surface_non_periodic = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "make_surface_non_periodic",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType","_Object._SurfaceType","null")
    }
make_surface_periodic = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "make_surface_periodic",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),("delete","bln","OPT"),),
    "method_returns": ("_Object._SurfaceType","_Object._SurfaceType","null")
    }
offset_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "offset_surface",
    "method_parameters": (("","self","REQ"),("distance","dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
short_path = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "CONSTRUCTOR",
    "method_name": "short_path",
    "method_parameters": (("","self","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),),
    "method_returns": ("_Object._SurfaceType","null")
    }
boolean_difference = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "boolean_difference",
    "method_parameters": (("input_0","array_of _Object","REQ"),("input_1","array_of str","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
boolean_intersection = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "boolean_intersection",
    "method_parameters": (("input_0","array_of _Object","REQ"),("input_1","array_of str","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
boolean_union = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "boolean_union",
    "method_parameters": (("input","array_of _Object","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
brep_closest_point = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "brep_closest_point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("array_of (array_of dbl, array_of dbl, array_of int, array_of dbl","null")
    }
cap_planar_holes = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "cap_planar_holes",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
duplicate_edge_curves = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "duplicate_edge_curves",
    "method_parameters": (("","self","REQ"),("select","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
duplicate_surface_border = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "duplicate_surface_border",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
evaluate_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "evaluate_surface",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
extract_iso_curve = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "extract_iso_curve",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),("dir","int","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
extrude_curve_tapered = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "extrude_curve_tapered",
    "method_parameters": (("","self","REQ"),("distance","dbl","REQ"),("direction","array_of dbl","REQ"),("base_point","array_of dbl","REQ"),("angle","dbl","REQ"),("corner_type","int","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
flip_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "flip_surface",
    "method_parameters": (("","self","REQ"),("flip","bln","OPT"),),
    "method_returns": ("boolean","boolean","null")
    }
insert_surface_knot = {#ed
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "insert_surface_knot",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),("symmetrical","bln","OPT"),),
    "method_returns": ("boolean","null")
    }
intersect_breps = {#ed
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "intersect_breps",
    "method_parameters": (("","self","REQ"),("brep_1","str","REQ"),("tolerance","dbl","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
pull_curve = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "pull_curve",
    "method_parameters": (("","self","REQ"),("curve","str","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
rebuild_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "rebuild_surface",
    "method_parameters": (("","self","REQ"),("degree","array_of int","OPT"),("point_count","array_of int","OPT"),),
    "method_returns": ("boolean","null")
    }
remove_surface_knot = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "remove_surface_knot",
    "method_parameters": (("","self","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),),
    "method_returns": ("boolean","null")
    }
reverse_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "reverse_surface",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),),
    "method_returns": ("boolean","null")
    }
shrink_trimmed_surface = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "shrink_trimmed_surface",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
split_brep = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "split_brep",
    "method_parameters": (("","self","REQ"),("cutter","str","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
surface_area = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_area",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of int,array_of int)","null")
    }
surface_area_centroid = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_area_centroid",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl)","null")
    }
surface_area_moments = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_area_moments",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl),(array_of dbl), (array_of dbl), (array_of dbl),(array_of dbl), (array_of dbl), (array_of dbl),(array_of dbl), (array_of dbl), (array_of dbl),(array_of dbl), (array_of dbl)","null")
    }
surface_closest_point = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_closest_point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
surface_contour_points = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_contour_points",
    "method_parameters": (("","self","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),("angle","dbl","OPT"),),
    "method_returns": ("array_of dbl","null")
    }
surface_curvature = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_curvature",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl, int,array_of dbl), int,array_of dbl, int), (int)","null")
    }
surface_curvature_analysis = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_curvature_analysis",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl)","null")
    }
surface_degree = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_degree",
    "method_parameters": (("","self","REQ"),("direction","int","OPT"),),
    "method_returns": ("array_of dbl","number","null")
    }
surface_domain = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_domain",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
surface_edit_points = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_edit_points",
    "method_parameters": (("","self","REQ"),("return_parameters","bln","OPT"),("return_all","bln","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
surface_evaluate = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_evaluate",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),("derivative","int","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl)","null")
    }
surface_frame = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_frame",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
surface_isocurve_density = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_isocurve_density",
    "method_parameters": (("","self","REQ"),("density","int","OPT"),),
    "method_returns": ("number","number","null")
    }
surface_knot_count = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_knot_count",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of int","null")
    }
surface_knots = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_knots",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
surface_normal = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_normal",
    "method_parameters": (("","self","REQ"),("parameter","array_of dbl","REQ"),),
    "method_returns": ("array_of dbl","null")
    }
surface_point_count = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_point_count",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of int","null")
    }
surface_points = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_points",
    "method_parameters": (("","self","REQ"),("return_all","bln","OPT"),),
    "method_returns": ("array_of int","null")
    }
surface_principal_curvature = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_principal_curvature",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
surface_seam = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_seam",
    "method_parameters": (("","self","REQ"),("direction","int","REQ"),("parameter","dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
surface_surface_intersection = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_surface_intersection",
    "method_parameters": (("","self","REQ"),("surface_a","str","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl)","array_of (int, array_of _Object._SurfaceType)","null")
    }
surface_volume = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_volume",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of _Object._SurfaceType","null")
    }
surface_volume_centroid = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_volume_centroid",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl)","null")
    }
surface_volume_moments = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_volume_moments",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of (array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl,array_of dbl)","null")
    }
surface_weights = {#ed
    "method_location": "_Object._SurfaceType",
    "method_type": "METHOD",
    "method_name": "surface_weights",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
    }