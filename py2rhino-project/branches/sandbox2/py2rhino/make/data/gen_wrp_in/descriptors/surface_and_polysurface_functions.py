#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_box = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 72,
    "function_vb_name": "AddBox",
    "function_name": "add_box",
    "function_parameters": (("corners","array_of dbl","REQ"),),
    "function_returns": ("string","null")
    }
add_cone = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 75,
    "function_vb_name": "AddCone",
    "function_name": "add_cone",
    "function_parameters": (("base","array_of dbl","REQ"),("height_pnt","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "function_returns": ("string","null")
    }
add_cone_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 75,
    "function_vb_name": "AddCone",
    "function_name": "add_cone_2",
    "function_parameters": (("plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "function_returns": ("string","null")
    }
add_cut_plane = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 822,
    "function_vb_name": "AddCutPlane",
    "function_name": "add_cut_plane",
    "function_parameters": (("objects","array_of str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("normal","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_cylinder = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 73,
    "function_vb_name": "AddCylinder",
    "function_name": "add_cylinder",
    "function_parameters": (("base","array_of dbl","REQ"),("height_pnt","array_of dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "function_returns": ("string","null")
    }
add_cylinder_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 73,
    "function_vb_name": "AddCylinder",
    "function_name": "add_cylinder_2",
    "function_parameters": (("plane","array_of dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
    "function_returns": ("string","null")
    }
add_edge_srf = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 203,
    "function_vb_name": "AddEdgeSrf",
    "function_name": "add_edge_srf",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("string","null")
    }
add_loft_srf = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 567,
    "function_vb_name": "AddLoftSrf",
    "function_name": "add_loft_srf",
    "function_parameters": (("objects","array_of str","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT")),
    "function_returns": ("array","null")
    }
add_nurbs_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 435,
    "function_vb_name": "AddNurbsSurface",
    "function_name": "add_nurbs_surface",
    "function_parameters": (("point_count","array_of int","REQ"),("points","array_of dbl","REQ"),("knots_u","array_of int","REQ"),("knots_v","array_of int","REQ"),("degree","array_of int","REQ"),("weights","array_of int","REQ")),
    "function_returns": ("string","null")
    }
add_planar_srf = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 371,
    "function_vb_name": "AddPlanarSrf",
    "function_name": "add_planar_srf",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("array","null")
    }
add_plane_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 648,
    "function_vb_name": "AddPlaneSurface",
    "function_name": "add_plane_surface",
    "function_parameters": (("plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_rail_rev_srf = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 536,
    "function_vb_name": "AddRailRevSrf",
    "function_name": "add_rail_rev_srf",
    "function_parameters": (("profile","str","REQ"),("rail","str","REQ"),("axis","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_rev_srf = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 535,
    "function_vb_name": "AddRevSrf",
    "function_name": "add_rev_srf",
    "function_parameters": (("profile","str","REQ"),("axis","array_of dbl","REQ"),("start_angle","dbl","OPT"),("end_angle","dbl","OPT")),
    "function_returns": ("string","null")
    }
add_sphere = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 71,
    "function_vb_name": "AddSphere",
    "function_name": "add_sphere",
    "function_parameters": (("center","array_of dbl","REQ"),("radius","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_sphere_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 71,
    "function_vb_name": "AddSphere",
    "function_name": "add_sphere_2",
    "function_parameters": (("plane","array_of dbl","REQ"),("radius","dbl","REQ")),
    "function_returns": ("string","null")
    }
add_srf_contour_crvs = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 747,
    "function_vb_name": "AddSrfContourCrvs",
    "function_name": "add_srf_contour_crvs",
    "function_parameters": (("object","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT")),
    "function_returns": ("array","null")
    }
add_srf_contour_crvs_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 747,
    "function_vb_name": "AddSrfContourCrvs",
    "function_name": "add_srf_contour_crvs_2",
    "function_parameters": (("object","str","REQ"),("plane","array_of dbl","REQ"),("interval","dbl","OPT")),
    "function_returns": ("array","null")
    }
add_srf_control_pt_grid = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 294,
    "function_vb_name": "AddSrfControlPtGrid",
    "function_name": "add_srf_control_pt_grid",
    "function_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_srf_pt = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 204,
    "function_vb_name": "AddSrfPt",
    "function_name": "add_srf_pt",
    "function_parameters": (("points","array_of dbl","REQ"),),
    "function_returns": ("string","null")
    }
add_srf_pt_grid = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 293,
    "function_vb_name": "AddSrfPtGrid",
    "function_name": "add_srf_pt_grid",
    "function_parameters": (("count","array_of int","REQ"),("points","array_of dbl","REQ"),("degree","array_of int","OPT"),("closed","array_of bln","OPT")),
    "function_returns": ("string","null")
    }
add_srf_section_crvs = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 803,
    "function_vb_name": "AddSrfSectionCrvs",
    "function_name": "add_srf_section_crvs",
    "function_parameters": (("object","str","REQ"),("plane","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
add_sweep_1 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 893,
    "function_vb_name": "AddSweep1",
    "function_name": "add_sweep_1",
    "function_parameters": (("rail","str","REQ"),("shapes","array_of str","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
    "function_returns": ("array","null")
    }
add_sweep_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 894,
    "function_vb_name": "AddSweep2",
    "function_name": "add_sweep_2",
    "function_parameters": (("rails","array_of str","REQ"),("shapes","array_of str","REQ"),("start_pt","array_of dbl","OPT"),("end_pt","array_of dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
    "function_returns": ("array","null")
    }
add_torus = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 74,
    "function_vb_name": "AddTorus",
    "function_name": "add_torus",
    "function_parameters": (("base","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
add_torus_2 = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 74,
    "function_vb_name": "AddTorus",
    "function_name": "add_torus_2",
    "function_parameters": (("plane","array_of dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ")),
    "function_returns": ("string","null")
    }
boolean_difference = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 508,
    "function_vb_name": "BooleanDifference",
    "function_name": "boolean_difference",
    "function_parameters": (("input_0","array_of str","REQ"),("input_1","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
boolean_intersection = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 507,
    "function_vb_name": "BooleanIntersection",
    "function_name": "boolean_intersection",
    "function_parameters": (("input_0","array_of str","REQ"),("input_1","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
boolean_union = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 506,
    "function_vb_name": "BooleanUnion",
    "function_name": "boolean_union",
    "function_parameters": (("input","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
brep_closest_point = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 514,
    "function_vb_name": "BrepClosestPoint",
    "function_name": "brep_closest_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
cap_planar_holes = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 701,
    "function_vb_name": "CapPlanarHoles",
    "function_name": "cap_planar_holes",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
duplicate_edge_curves = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 657,
    "function_vb_name": "DuplicateEdgeCurves",
    "function_name": "duplicate_edge_curves",
    "function_parameters": (("object","str","REQ"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
duplicate_surface_border = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 852,
    "function_vb_name": "DuplicateSurfaceBorder",
    "function_name": "duplicate_surface_border",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
evaluate_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 205,
    "function_vb_name": "EvaluateSurface",
    "function_name": "evaluate_surface",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
explode_polysurfaces = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 447,
    "function_vb_name": "ExplodePolysurfaces",
    "function_name": "explode_polysurfaces",
    "function_parameters": (("objects","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
extract_iso_curve = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 488,
    "function_vb_name": "ExtractIsoCurve",
    "function_name": "extract_iso_curve",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ"),("dir","int","REQ")),
    "function_returns": ("array","null")
    }
extrude_curve = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 538,
    "function_vb_name": "ExtrudeCurve",
    "function_name": "extrude_curve",
    "function_parameters": (("curve","str","REQ"),("path","str","REQ")),
    "function_returns": ("string","null")
    }
extrude_curve_point = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 540,
    "function_vb_name": "ExtrudeCurvePoint",
    "function_name": "extrude_curve_point",
    "function_parameters": (("curve","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
extrude_curve_straight = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 539,
    "function_vb_name": "ExtrudeCurveStraight",
    "function_name": "extrude_curve_straight",
    "function_parameters": (("curve","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
extrude_curve_tapered = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 914,
    "function_vb_name": "ExtrudeCurveTapered",
    "function_name": "extrude_curve_tapered",
    "function_parameters": (("curve","str","REQ"),("distance","dbl","REQ"),("direction","array_of dbl","REQ"),("base_point","array_of dbl","REQ"),("angle","dbl","REQ"),("corner_type","int","OPT")),
    "function_returns": ("array","null")
    }
extrude_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 541,
    "function_vb_name": "ExtrudeSurface",
    "function_name": "extrude_surface",
    "function_parameters": (("surface","str","REQ"),("curve","str","REQ"),("cap","bln","OPT")),
    "function_returns": ("string","null")
    }
fit_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 815,
    "function_vb_name": "FitSurface",
    "function_name": "fit_surface",
    "function_parameters": (("object","str","REQ"),("degree","array_of int","OPT"),("tolerance","dbl","OPT")),
    "function_returns": ("string","null")
    }
flip_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 718,
    "function_vb_name": "FlipSurface",
    "function_name": "flip_surface",
    "function_parameters": (("object","str","REQ"),("flip","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
insert_surface_knot = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 516,
    "function_vb_name": "InsertSurfaceKnot",
    "function_name": "insert_surface_knot",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),("symmetrical","bln","OPT")),
    "function_returns": ("boolean","null")
    }
intersect_breps = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 544,
    "function_vb_name": "IntersectBreps",
    "function_name": "intersect_breps",
    "function_parameters": (("brep_1","str","REQ"),("brep_2","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","null")
    }
is_brep = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 206,
    "function_vb_name": "IsBrep",
    "function_name": "is_brep",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_brep_manifold = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 854,
    "function_vb_name": "IsBrepManifold",
    "function_name": "is_brep_manifold",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_cone = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 885,
    "function_vb_name": "IsCone",
    "function_name": "is_cone",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_cylinder = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 884,
    "function_vb_name": "IsCylinder",
    "function_name": "is_cylinder",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_parameter_on_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 879,
    "function_vb_name": "IsParameterOnSurface",
    "function_name": "is_parameter_on_surface",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
is_plane_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 638,
    "function_vb_name": "IsPlaneSurface",
    "function_name": "is_plane_surface",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_point_in_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 443,
    "function_vb_name": "IsPointInSurface",
    "function_name": "is_point_in_surface",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
is_point_on_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 319,
    "function_vb_name": "IsPointOnSurface",
    "function_name": "is_point_on_surface",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
is_poly_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 207,
    "function_vb_name": "IsPolySurface",
    "function_name": "is_poly_surface",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_poly_surface_closed = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 208,
    "function_vb_name": "IsPolySurfaceClosed",
    "function_name": "is_poly_surface_closed",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_poly_surface_planar = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 209,
    "function_vb_name": "IsPolySurfacePlanar",
    "function_name": "is_poly_surface_planar",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_sphere = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 883,
    "function_vb_name": "IsSphere",
    "function_name": "is_sphere",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 210,
    "function_vb_name": "IsSurface",
    "function_name": "is_surface",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_surface_closed = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 211,
    "function_vb_name": "IsSurfaceClosed",
    "function_name": "is_surface_closed",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "function_returns": ("boolean","null")
    }
is_surface_periodic = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 212,
    "function_vb_name": "IsSurfacePeriodic",
    "function_name": "is_surface_periodic",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "function_returns": ("boolean","null")
    }
is_surface_planar = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 213,
    "function_vb_name": "IsSurfacePlanar",
    "function_name": "is_surface_planar",
    "function_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("boolean","null")
    }
is_surface_rational = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 434,
    "function_vb_name": "IsSurfaceRational",
    "function_name": "is_surface_rational",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_surface_singular = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 214,
    "function_vb_name": "IsSurfaceSingular",
    "function_name": "is_surface_singular",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "function_returns": ("boolean","null")
    }
is_surface_trimmed = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 269,
    "function_vb_name": "IsSurfaceTrimmed",
    "function_name": "is_surface_trimmed",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_torus = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 886,
    "function_vb_name": "IsTorus",
    "function_name": "is_torus",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
join_surfaces = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 487,
    "function_vb_name": "JoinSurfaces",
    "function_name": "join_surfaces",
    "function_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","null")
    }
make_surface_non_periodic = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 926,
    "function_vb_name": "MakeSurfaceNonPeriodic",
    "function_name": "make_surface_non_periodic",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","string","null")
    }
make_surface_periodic = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 445,
    "function_vb_name": "MakeSurfacePeriodic",
    "function_name": "make_surface_periodic",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
    "function_returns": ("string","string","null")
    }
offset_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 635,
    "function_vb_name": "OffsetSurface",
    "function_name": "offset_surface",
    "function_parameters": (("object","str","REQ"),("distance","dbl","REQ")),
    "function_returns": ("string","null")
    }
pull_curve = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 493,
    "function_vb_name": "PullCurve",
    "function_name": "pull_curve",
    "function_parameters": (("surface","str","REQ"),("curve","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
rebuild_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 816,
    "function_vb_name": "RebuildSurface",
    "function_name": "rebuild_surface",
    "function_parameters": (("object","str","REQ"),("degree","array_of int","OPT"),("point_count","array_of int","OPT")),
    "function_returns": ("boolean","null")
    }
remove_surface_knot = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 917,
    "function_vb_name": "RemoveSurfaceKnot",
    "function_name": "remove_surface_knot",
    "function_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ")),
    "function_returns": ("boolean","null")
    }
reverse_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 927,
    "function_vb_name": "ReverseSurface",
    "function_name": "reverse_surface",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "function_returns": ("boolean","null")
    }
short_path = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 702,
    "function_vb_name": "ShortPath",
    "function_name": "short_path",
    "function_parameters": (("surface","str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
shrink_trimmed_surface = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 700,
    "function_vb_name": "ShrinkTrimmedSurface",
    "function_name": "shrink_trimmed_surface",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("boolean","null")
    }
split_brep = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 637,
    "function_vb_name": "SplitBrep",
    "function_name": "split_brep",
    "function_parameters": (("brep","str","REQ"),("cutter","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
surface_area = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 382,
    "function_vb_name": "SurfaceArea",
    "function_name": "surface_area",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","number","number","null")
    }
surface_area_centroid = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 384,
    "function_vb_name": "SurfaceAreaCentroid",
    "function_name": "surface_area_centroid",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_area_moments = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 386,
    "function_vb_name": "SurfaceAreaMoments",
    "function_name": "surface_area_moments",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_closest_point = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 215,
    "function_vb_name": "SurfaceClosestPoint",
    "function_name": "surface_closest_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
surface_cone = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 889,
    "function_vb_name": "SurfaceCone",
    "function_name": "surface_cone",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("array","array","number","number","null")
    }
surface_contour_points = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 79,
    "function_vb_name": "SurfaceContourPoints",
    "function_name": "surface_contour_points",
    "function_parameters": (("object","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),("angle","dbl","OPT")),
    "function_returns": ("array","null")
    }
surface_curvature = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 378,
    "function_vb_name": "SurfaceCurvature",
    "function_name": "surface_curvature",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","number","number","number","number","null")
    }
surface_curvature_analysis = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 632,
    "function_vb_name": "SurfaceCurvatureAnalysis",
    "function_name": "surface_curvature_analysis",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","array","array","array","array","null")
    }
surface_cylinder = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 888,
    "function_vb_name": "SurfaceCylinder",
    "function_name": "surface_cylinder",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("array","array","number","number","null")
    }
surface_degree = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 216,
    "function_vb_name": "SurfaceDegree",
    "function_name": "surface_degree",
    "function_parameters": (("object","str","REQ"),("direction","int","OPT")),
    "function_returns": ("array","number","null")
    }
surface_domain = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 217,
    "function_vb_name": "SurfaceDomain",
    "function_name": "surface_domain",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ")),
    "function_returns": ("array","null")
    }
surface_edit_points = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 427,
    "function_vb_name": "SurfaceEditPoints",
    "function_name": "surface_edit_points",
    "function_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("return_all","bln","OPT")),
    "function_returns": ("array","array","null")
    }
surface_evaluate = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 583,
    "function_vb_name": "SurfaceEvaluate",
    "function_name": "surface_evaluate",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ"),("derivative","int","REQ")),
    "function_returns": ("array","array","array","array","array","array","array","array","null")
    }
surface_frame = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 623,
    "function_vb_name": "SurfaceFrame",
    "function_name": "surface_frame",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
surface_isocurve_density = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 361,
    "function_vb_name": "SurfaceIsocurveDensity",
    "function_name": "surface_isocurve_density",
    "function_parameters": (("object","str","REQ"),("density","int","OPT")),
    "function_returns": ("number","number","null")
    }
surface_knot_count = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 431,
    "function_vb_name": "SurfaceKnotCount",
    "function_name": "surface_knot_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_knots = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 432,
    "function_vb_name": "SurfaceKnots",
    "function_name": "surface_knots",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_normal = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 362,
    "function_vb_name": "SurfaceNormal",
    "function_name": "surface_normal",
    "function_parameters": (("object","str","REQ"),("parameter","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
surface_point_count = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 218,
    "function_vb_name": "SurfacePointCount",
    "function_name": "surface_point_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_points = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 372,
    "function_vb_name": "SurfacePoints",
    "function_name": "surface_points",
    "function_parameters": (("object","str","REQ"),("return_all","bln","OPT")),
    "function_returns": ("array","null")
    }
surface_principal_curvature = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 717,
    "function_vb_name": "SurfacePrincipalCurvature",
    "function_name": "surface_principal_curvature",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
surface_seam = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 804,
    "function_vb_name": "SurfaceSeam",
    "function_name": "surface_seam",
    "function_parameters": (("object","str","REQ"),("direction","int","REQ"),("parameter","dbl","REQ")),
    "function_returns": ("boolean","null")
    }
surface_sphere = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 887,
    "function_vb_name": "SurfaceSphere",
    "function_name": "surface_sphere",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("array","array","number","null")
    }
surface_surface_intersection = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 484,
    "function_vb_name": "SurfaceSurfaceIntersection",
    "function_name": "surface_surface_intersection",
    "function_parameters": (("surface_a","str","REQ"),("surface_b","str","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT")),
    "function_returns": ("array","array","number","string","null")
    }
surface_torus = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 890,
    "function_vb_name": "SurfaceTorus",
    "function_name": "surface_torus",
    "function_parameters": (("surface","str","REQ"),),
    "function_returns": ("array","array","number","number","null")
    }
surface_volume = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 383,
    "function_vb_name": "SurfaceVolume",
    "function_name": "surface_volume",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","number","number","null")
    }
surface_volume_centroid = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 385,
    "function_vb_name": "SurfaceVolumeCentroid",
    "function_name": "surface_volume_centroid",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_volume_moments = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 387,
    "function_vb_name": "SurfaceVolumeMoments",
    "function_name": "surface_volume_moments",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
surface_weights = {
    "function_location": "surface_and_polysurface",
    "function_com_id": 433,
    "function_vb_name": "SurfaceWeights",
    "function_name": "surface_weights",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
