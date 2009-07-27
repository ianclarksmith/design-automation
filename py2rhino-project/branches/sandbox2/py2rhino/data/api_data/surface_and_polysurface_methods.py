#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

add_box = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_box",
    "method_parameters": (("corners","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
add_cone = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_cone",
    "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "method_returns": ("string","null")
    }
add_cut_plane = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_cut_plane",
    "method_parameters": (("objects","arr_of_str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("normal","arr_of_dbl","OPT")),
    "method_returns": ("string","null")
    }
add_cylinder = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_cylinder",
    "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "method_returns": ("string","null")
    }
add_edge_srf = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_edge_srf",
    "method_parameters": (("objects","arr_of_str","REQ")),
    "method_returns": ("string","null")
    }
add_loft_srf = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_loft_srf",
    "method_parameters": (("objects","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT")),
    "method_returns": ("array","null")
    }
add_nurbs_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_nurbs_surface",
    "method_parameters": (("point_count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("knots_u","arr_of_int","REQ"),("knots_v","arr_of_int","REQ"),("degree","arr_of_int","REQ"),("weights","arr_of_int","REQ")),
    "method_returns": ("string","null")
    }
add_planar_srf = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_planar_srf",
    "method_parameters": (("objects","arr_of_str","REQ")),
    "method_returns": ("array","null")
    }
add_plane_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_plane_surface",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ")),
    "method_returns": ("string","null")
    }
add_rail_rev_srf = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_rail_rev_srf",
    "method_parameters": (("profile","str","REQ"),("rail","str","REQ"),("axis","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
add_rev_srf = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_rev_srf",
    "method_parameters": (("profile","str","REQ"),("axis","arr_of_dbl","REQ"),("start_angle","dbl","OPT"),("end_angle","dbl","OPT")),
    "method_returns": ("string","null")
    }
add_sphere = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_sphere",
    "method_parameters": (("center","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("radius","dbl","REQ")),
    "method_returns": ("string","null")
    }
add_srf_contour_crvs = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_srf_contour_crvs",
    "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("interval","dbl","OPT")),
    "method_returns": ("array","null")
    }
add_srf_control_pt_grid = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_srf_control_pt_grid",
    "method_parameters": (("count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("degree","arr_of_dbl","OPT")),
    "method_returns": ("string","null")
    }
add_srf_pt = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_srf_pt",
    "method_parameters": (("points","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
add_srf_pt_grid = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_srf_pt_grid",
    "method_parameters": (("count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("degree","arr_of_int","OPT"),("closed","arr_of_bln","OPT")),
    "method_returns": ("string","null")
    }
add_srf_section_crvs = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_srf_section_crvs",
    "method_parameters": (("object","str","REQ"),("plane","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
add_sweep1 = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_sweep1",
    "method_parameters": (("rail","str","REQ"),("shapes","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
    "method_returns": ("array","null")
    }
add_sweep2 = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_sweep2",
    "method_parameters": (("rails","arr_of_str","REQ"),("shapes","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
    "method_returns": ("array","null")
    }
add_torus = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "add_torus",
    "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","arr_of_dbl","OPT")),
    "method_returns": ("string","null")
    }
boolean_difference = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "boolean_difference",
    "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
boolean_intersection = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "boolean_intersection",
    "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
boolean_union = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "boolean_union",
    "method_parameters": (("input","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
brep_closest_point = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "brep_closest_point",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
cap_planar_holes = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "cap_planar_holes",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
duplicate_edge_curves = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "duplicate_edge_curves",
    "method_parameters": (("object","str","REQ"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
duplicate_surface_border = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "duplicate_surface_border",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
evaluate_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "evaluate_surface",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
explode_polysurfaces = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "explode_polysurfaces",
    "method_parameters": (("objects","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
extract_iso_curve = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extract_iso_curve",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ"),("dir","int","REQ")),
    "method_returns": ("array","null")
    }
extrude_curve = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extrude_curve",
    "method_parameters": (("curve","str","REQ"),("path","str","REQ")),
    "method_returns": ("string","null")
    }
extrude_curve_point = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extrude_curve_point",
    "method_parameters": (("curve","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
extrude_curve_straight = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extrude_curve_straight",
    "method_parameters": (("curve","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
extrude_curve_tapered = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extrude_curve_tapered",
    "method_parameters": (("curve","str","REQ"),("distance","dbl","REQ"),("direction","arr_of_dbl","REQ"),("base_point","arr_of_dbl","REQ"),("angle","dbl","REQ"),("corner_type","int","OPT")),
    "method_returns": ("array","null")
    }
extrude_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "extrude_surface",
    "method_parameters": (("surface","str","REQ"),("curve","str","REQ"),("cap","bln","OPT")),
    "method_returns": ("string","null")
    }
fit_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "fit_surface",
    "method_parameters": (("object","str","REQ"),("degree","arr_of_int","OPT"),("tolerance","dbl","OPT")),
    "method_returns": ("string","null")
    }
flip_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "flip_surface",
    "method_parameters": (("object","str","REQ"),("flip","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
insert_surface_knot = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "insert_surface_knot",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),("symmetrical","bln","OPT")),
    "method_returns": ("boolean","null")
    }
intersect_breps = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "intersect_breps",
    "method_parameters": (("brep1","str","REQ"),("brep2","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("array","null")
    }
is_brep = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_brep",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_brep_manifold = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_brep_manifold",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_cone = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_cone",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_cylinder = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_cylinder",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_parameter_on_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_parameter_on_surface",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_plane_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_plane_surface",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_point_in_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_point_in_surface",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_point_on_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_point_on_surface",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_poly_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_poly_surface",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_poly_surface_closed = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_poly_surface_closed",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_poly_surface_planar = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_poly_surface_planar",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_sphere = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_sphere",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface_closed = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_closed",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface_periodic = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_periodic",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface_planar = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_planar",
    "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("boolean","null")
    }
is_surface_rational = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_rational",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface_singular = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_singular",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "method_returns": ("boolean","null")
    }
is_surface_trimmed = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_surface_trimmed",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_torus = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "is_torus",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
join_surfaces = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "join_surfaces",
    "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","null")
    }
make_surface_non_periodic = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "make_surface_non_periodic",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","string","null")
    }
make_surface_periodic = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "make_surface_periodic",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
    "method_returns": ("string","string","null")
    }
offset_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "offset_surface",
    "method_parameters": (("object","str","REQ"),("distance","dbl","REQ")),
    "method_returns": ("string","null")
    }
pull_curve = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "pull_curve",
    "method_parameters": (("surface","str","REQ"),("curve","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
rebuild_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "rebuild_surface",
    "method_parameters": (("object","str","REQ"),("degree","arr_of_int","OPT"),("point_count","arr_of_int","OPT")),
    "method_returns": ("boolean","null")
    }
remove_surface_knot = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "remove_surface_knot",
    "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ")),
    "method_returns": ("boolean","null")
    }
reverse_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "reverse_surface",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "method_returns": ("boolean","null")
    }
short_path = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "short_path",
    "method_parameters": (("surface","str","REQ"),("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
shrink_trimmed_surface = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "shrink_trimmed_surface",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("boolean","null")
    }
split_brep = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "split_brep",
    "method_parameters": (("brep","str","REQ"),("cutter","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
surface_area = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_area",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","number","number","null")
    }
surface_area_centroid = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_area_centroid",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_area_moments = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_area_moments",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_closest_point = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_closest_point",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
surface_cone = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_cone",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("array","array","number","number","null")
    }
surface_contour_points = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_contour_points",
    "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("interval","dbl","OPT"),("angle","dbl","OPT")),
    "method_returns": ("array","null")
    }
surface_curvature = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_curvature",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("array","number","number","number","number","null")
    }
surface_curvature_analysis = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_curvature_analysis",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","array","array","array","array","null")
    }
surface_cylinder = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_cylinder",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("array","array","number","number","null")
    }
surface_degree = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_degree",
    "method_parameters": (("object","str","REQ"),("direction","int","OPT")),
    "method_returns": ("array","number","null")
    }
surface_domain = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_domain",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "method_returns": ("array","null")
    }
surface_edit_points = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_edit_points",
    "method_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("return_all","bln","OPT")),
    "method_returns": ("array","array","null")
    }
surface_evaluate = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_evaluate",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ"),("derivative","int","REQ")),
    "method_returns": ("array","array","array","array","array","array","array","array","null")
    }
surface_frame = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_frame",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
surface_isocurve_density = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_isocurve_density",
    "method_parameters": (("object","str","REQ"),("density","int","OPT")),
    "method_returns": ("number","number","null")
    }
surface_knot_count = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_knot_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_knots = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_knots",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_normal = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_normal",
    "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
surface_point_count = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_point_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_points = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_points",
    "method_parameters": (("object","str","REQ"),("return_all","bln","OPT")),
    "method_returns": ("array","null")
    }
surface_principal_curvature = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_principal_curvature",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
surface_seam = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_seam",
    "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("parameter","dbl","REQ")),
    "method_returns": ("boolean","null")
    }
surface_sphere = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_sphere",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("array","array","number","null")
    }
surface_surface_intersection = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_surface_intersection",
    "method_parameters": (("surface_a","str","REQ"),("surface_b","str","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT")),
    "method_returns": ("array","array","number","string","null")
    }
surface_torus = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_torus",
    "method_parameters": (("surface","str","REQ")),
    "method_returns": ("array","array","number","number","null")
    }
surface_volume = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_volume",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","number","number","null")
    }
surface_volume_centroid = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_volume_centroid",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_volume_moments = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_volume_moments",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
surface_weights = {
    "method_location": "Surface_and_Polysurface",
    "method_type": "METHOD",
    "method_name": "surface_weights",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
