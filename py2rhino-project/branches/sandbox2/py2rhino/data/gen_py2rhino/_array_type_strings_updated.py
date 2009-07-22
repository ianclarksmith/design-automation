#Replace in the ??? with either "bln", "int", "dbl", or "str"

application = {
    "status_bar_point": {
        "Point": "arr_of_dbl",
    },
},
block = {
},
curve = {
    "add_arc": {
        "Plane": "arr_of_dbl",
        "Radius": "dbl",
        "Angle": "dbl",
    },
    "add_arc3_pt": {
        "Start": "arr_of_dbl",
        "End": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "add_circle": {
        "Plane": "arr_of_dbl",
        "Radius": "dbl",
    },
    "add_circle3_pt": {
        "Start": "arr_of_dbl",
        "End": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "add_curve": {
        "Points": "arr_of_dbl",
        "Degree": "int",
    },
    "add_ellipse": {
        "Plane": "arr_of_dbl",
        "XRadius": "dbl",
        "YRadius": "dbl",
    },
    "add_ellipse3_pt": {
        "Center": "arr_of_dbl",
        "Second": "arr_of_dbl",
        "Third": "arr_of_dbl",
    },
    "add_fillet_curve": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "Point0": "arr_of_dbl",
        "Point1": "arr_of_dbl",
    },
    "add_interp_crv_on_srf": {
        "Object": "str",
        "Points": "arr_of_dbl",
    },
    "add_interp_crv_on_srf_u_v": {
        "Object": "str",
        "Points": "arr_of_dbl",
    },
    "add_interp_curve": {
        "Points": "arr_of_dbl",
        "Degree": "int",
        "KnotStyle": "int",
        "StartTan": "arr_of_dbl",
        "EndTan": "arr_of_dbl",
    },
    "add_interp_curve_ex": {
        "Points": "arr_of_dbl",
        "Degree": "int",
        "KnotStyle": "int",
        "Sharp": "bln",
        "StartTangent": "arr_of_dbl",
        "EndTangent": "arr_of_dbl",
    },
    "add_line": {
        "Start": "arr_of_dbl",
        "End": "arr_of_dbl",
    },
    "add_nurbs_curve": {
        "Points": "arr_of_dbl",
        "Knots": "arr_of_int",
        "Degree": "int",
        "Weights": "arr_of_int",
    },
    "add_polyline": {
        "Points": "arr_of_dbl",
    },
    "curve_boolean_union": {
        "Curves": "arr_of_str",
    },
    "curve_closest_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
        "Index": "int",
    },
    "curve_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
        "Interval": "dbl",
    },
    "curve_fillet_points": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "BasePoint0": "arr_of_dbl",
        "BasePoint1": "arr_of_dbl",
    },
    "curve_length": {
        "Object": "str",
        "Index": "int",
        "SubDomain": "arr_of_int",
    },
    "curve_radius": {
        "Object": "str",
        "Point": "arr_of_dbl",
        "Index": "int",
    },
    "extend_curve": {
        "Object": "str",
        "Type": "int",
        "Side": "int",
        "Objects": "arr_of_str",
    },
    "extend_curve_point": {
        "Object": "str",
        "Side": "int",
        "Point": "arr_of_dbl",
    },
    "is_curve_in_plane": {
        "Object": "str",
        "Plane": "arr_of_dbl",
    },
    "is_point_on_curve": {
        "Object": "str",
        "Point": "arr_of_int",
        "Index": "int",
    },
    "planar_closed_curve_containment": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "planar_curve_collision": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "point_in_planar_closed_curve": {
        "Point": "arr_of_dbl",
        "Curve": "str",
        "Plane": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "trim_curve": {
        "Object": "str",
        "Interval": "arr_of_int",
        "Delete": "bln",
    },
},
dimension = {
    "add_leader": {
        "Points": "arr_of_dbl",
        "View": "str",
        "Text": "str",
    },
},
document = {
    "create_preview_image": {
        "File": "str",
        "View": "str",
        "Size": "arr_of_int",
        "Flags": "int",
        "Wireframe": "bln",
    },
    "render_resolution": {
        "Resolution": "arr_of_int", 
    },
},
geometry = {
    "add_point": {
        "Point": "arr_of_dbl",
    },
    "add_point_cloud": {
        "Points": "arr_of_dbl",
    },
    "add_points": {
        "Points": "arr_of_dbl",
    },
    "add_text_dot": {
        "Test": "str",
        "Point": "arr_of_dbl",
    },
    "point_coordinates": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "text_dot_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "text_object_plane": {
        "Object": "str",
        "Plane": "arr_of_dbl",
    },
    "text_object_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
},
group = {
    "add_objects_to_group": {
        "Objects": "arr_of_str",
        "Group": "str",
    },
    "remove_objects_from_group": {
        "Objects": "arr_of_str",
        "Group": "str",
    },
},
hatch = {
    "add_hatches": {
        "Curves": "arr_of_str",
        "Hatch": "str",
        "Scale": "dbl",
        "Rotation": "dbl",
    },
},
layer = {
},
light = {
    "add_directional_light": {
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
    },
    "add_linear_light": {
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
        "Width": "dbl",
    },
    "add_point_light": {
        "Point": "arr_of_dbl",
    },
    "add_rectangular_light": {
        "Origin": "arr_of_dbl",
        "Width": "arr_of_dbl",
        "Height": "arr_of_dbl",
    },
    "add_spot_light": {
        "Origin": "arr_of_dbl",
        "Radius": "dbl",
        "Apex": "arr_of_dbl",
    },
    "light_direction": {
        "Object": "str",
        "Direction": "arr_of_dbl",
    },
    "light_location": {
        "Object": "str",
        "location": "arr_of_dbl",
    },
},
line_and_plane = {
    "distance_to_plane": {
        "Plane": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "evaluate_plane": {
        "Plane": "arr_of_dbl",
        "Parameter": "arr_of_dbl",
    },
    "intersect_planes": {
        "Plane1": "arr_of_dbl",
        "Plane2": "arr_of_dbl",
        "Plane3": "arr_of_dbl",
    },
    "line_closest_point": {
        "Line": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "line_line_intersection": {
        "LineA": "arr_of_dbl",
        "LineB": "arr_of_dbl",
        "Planar": "bln",
    },
    "line_plane": {
        "Line": "arr_of_dbl",
    },
    "line_plane_intersection": {
        "Line": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "line_transform": {
        "Line": "arr_of_dbl",
        "Xform": "arr_of_dbl", 
    },
    "move_plane": {
        "Plane": "arr_of_dbl",
        "Origin": "arr_of_dbl",
    },
    "plane_closest_point": {
        "Plane": "arr_of_dbl",
        "Point": "arr_of_dbl",
        "ReturnPoint": "bln",
    },
    "plane_equation": {
        "Plane": "arr_of_dbl",
    },
    "plane_fit_from_points": {
        "Points": "arr_of_dbl",
    },
    "plane_from_frame": {
        "Origin": "arr_of_dbl",
        "Xaxis": "arr_of_dbl",
        "Yaxis": "arr_of_dbl",
    },
    "plane_from_normal": {
        "Origin": "arr_of_dbl",
        "Normal": "arr_of_dbl",
    },
    "plane_from_points": {
        "Origin": "arr_of_dbl",
        "PointX": "arr_of_dbl",
        "PointY": "arr_of_dbl",
    },
    "plane_plane_intersection": {
        "Plane1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
    },
    "plane_transform": {
        "Plane": "arr_of_dbl",
        "Xform": "arr_of_dbl",
    },
    "rotate_plane": {
        "Plane": "arr_of_dbl",
        "Angle": "dbl",
        "Axis": "arr_of_dbl",
    },
},
linetype = {
},
material = {
},
math = {
    "angle": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
        "World": "bln",
    },
    "angle2": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
    },
    "deviation": {
        "Numbers": "arr_of_int",
    },
    "max": {
        "Numbers": "arr_of_int",
    },
    "mean": {
        "Numbers": "arr_of_int",
    },
    "median": {
        "Numbers": "arr_of_int",
    },
    "min": {
        "Numbers": "arr_of_int",
    },
    "polar": {
        "Point": "arr_of_dbl",
        "Angle": "dbl",
        "Distance": "dbl",
        "Plane": "arr_of_dbl",
    },
    "sum": {
        "Numbers": "arr_of_int",
    },
},
mesh = {
    "add_mesh": {
        "Vertices": "arr_of_dbl",
        "FaceVertices": "arr_of_int",
        "VertexNormals": "arr_of_dbl",
        "TextureCoordinates": "arr_of_dbl", 
        "VertexColors": "arr_of_int",
    },
    "mesh_boolean_difference": {
        "Input0": "arr_of_str", 
        "Input1": "arr_of_str",
        "Delete": "bln",
    },
    "mesh_boolean_intersection": {
        "Input0": "arr_of_str",
        "Input1": "arr_of_str",
        "Delete": "bln",
    },
    "mesh_boolean_split": {
        "Input0": "arr_of_str",
        "Input1": "arr_of_str",
        "Delete": "bln",
    },
    "mesh_boolean_union": {
        "Input": "arr_of_str",
        "Delete": "bln",
    },
    "mesh_closest_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "mesh_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
        "Interval": "dbl",
        "RemoveCoincidentPoints": "bln",
    },
},
object = {
    "delete_objects": {
        "Objects": "arr_of_str",
    },
    "enable_object_mesh": {
        "Objects": "arr_of_str", 
        "Enable": "bln",
    },
    "hide_objects": {
        "Objects": "arr_of_str",
    },
    "is_object_in_box": {
        "Object": "str",
        "Box": "arr_of_dbl",
        "Mode": "bln",
    },
    "lock_objects": {
        "Objects": "arr_of_str",
    },
    "mirror_object": {
        "Object": "str",
        "StartPt": "arr_of_dbl",
        "EndPt": "arr_of_dbl",
        "Copy": "bln",
    },
    "mirror_objects": {
        "Objects": "arr_of_str",
        "StartPt": "arr_of_dbl",
        "EndPt": "arr_of_dbl",
        "Copy": "bln",
    },
    "object_names": {
        "Objects": "arr_of_str",
        "Names": "arr_of_str",
    },
    "orient_object": {
        "Object": "str",
        "Reference": "arr_of_dbl",
        "Target": "arr_of_dbl",
        "Flags": "int",
    },
    "orient_objects": {
        "Objects": "arr_of_str",
        "Reference": "arr_of_dbl",
        "Target": "arr_of_dbl",
        "Flags": "int",
    },
    "remap_object": {
        "Object": "str",
        "SrcPlane": "arr_of_dbl",
        "DstPlane": "arr_of_dbl",
        "Copy": "bln",
    },
    "remap_objects": {
        "Object": "arr_of_str",
        "SrcPlane": "arr_of_dbl",
        "DstPlane": "arr_of_dbl",
        "Copy": "bln",
    },
    "rotate_object": {
        "Object": "str",
        "Point": "arr_of_dbl",
        "Angle": "dbl",
        "Axis": "arr_of_dbl",
        "Copy": "bln",
    },
    "rotate_objects": {
        "Objects": "arr_of_str",
        "Point": "arr_of_dbl",
        "Angle": "dbl",
        "Axis": "arr_of_dbl",
        "Copy": "bln",
    },
    "scale_object": {
        "Object": "str",
        "Origin": "arr_of_dbl",
        "Scale": "arr_of_int",
        "Copy": "bln",
    },
    "scale_objects": {
        "Objects": "arr_of_str",
        "Origin": "arr_of_dbl",
        "Scale": "arr_of_dbl",
        "Copy": "bln",
    },
    "select_objects": {
        "Objects": "arr_of_str",
    },
    "shear_object": {
        "Object": "str",
        "Origin": "arr_of_dbl",
        "RefPt": "arr_of_dbl",
        "Scale": "arr_of_int",
        "Copy": "bln",
    },
    "shear_objects": {
        "Objects": "arr_of_str",
        "Origin": "arr_of_dbl",
        "RefPt": "arr_of_dbl",
        "Scale": "arr_of_int",
        "Copy": "bln",
    },
    "show_objects": {
        "Objects": "arr_of_str",
    },
    "unlock_objects": {
        "Objects": "arr_of_str",
    },
    "unselect_objects": {
        "Objects": "arr_of_str",
    },
},
object_grip = {
    "object_grip_location": {
        "Object": "str",
        "Index": "int",
        "Point": "arr_of_dbl",
    },
    "object_grip_locations": {
        "Object": "str",
        "Points": "arr_of_dbl",
    },
},
point_and_vector = {
    "is_vector_parallel_to": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "is_vector_perpendicular_to": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "is_vector_tiny": {
        "Vector": "arr_of_dbl",
    },
    "is_vector_zero": {
        "Vector": "arr_of_dbl",
    },
    "point_add": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
    },
    "point_array_bounding_box": {
        "Points": "arr_of_dbl",
        "View": "str",
        "WorldCoords": "bln",
    },
    "point_array_closest_point": {
        "Points": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "point_array_transform": {
        "Points": "arr_of_dbl",
        "Xform": "arr_of_dbl",
    },
    "point_compare": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "point_divide": {
        "Point": "arr_of_dbl",
        "Scale": "dbl",
    },
    "point_scale": {
        "Point": "arr_of_dbl",
        "Scale": "dbl",
    },
    "point_subtract": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
    },
    "point_transform": {
        "Point": "arr_of_dbl",
        "Xform": "arr_of_dbl",
    },
    "points_are_coplanar": {
        "Points": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "pull_points": {
        "Object": "str",
        "Points": "arr_of_dbl",
    },
    "vector_add": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_compare": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_create": {
        "Point1": "arr_of_dbl",
        "Point2": "arr_of_dbl",
    },
    "vector_cross_product": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_divide": {
        "Vector": "arr_of_dbl",
        "Divide": "dbl",
    },
    "vector_dot_product": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_length": {
        "Vector": "arr_of_dbl",
    },
    "vector_multiply": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_reverse": {
        "Vector": "arr_of_dbl",
    },
    "vector_rotate": {
        "Vector": "arr_of_dbl",
        "Angle": "dbl",
        "Axis": "arr_of_dbl",
    },
    "vector_scale": {
        "Vector": "arr_of_dbl",
        "Scale": "dbl",
    },
    "vector_subtract": {
        "Vector1": "arr_of_dbl",
        "Vector2": "arr_of_dbl",
    },
    "vector_transform": {
        "Vector": "arr_of_dbl",
        "Xform": "arr_of_dbl",
    },
    "vector_unitize": {
        "Vector": "arr_of_dbl",
    },
},
selection = {
    "get_object": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_str",
    },
    "get_object_ex": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_str",
    },
    "get_objects": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_str",
    },
    "get_objects_ex": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_str",
    },
},
surface_and_polysurface = {
    "add_box": {
        "Corners": "arr_of_dbl",
    },
    "add_cut_plane": {
        "Objects": "arr_of_str",
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
        "Normal": "arr_of_dbl",
    },
    "add_edge_srf": {
        "Objects": "arr_of_str",
    },
    "add_loft_srf": {
        "Objects": "arr_of_str",
        "StartPt": "arr_of_dbl",
        "EndPt": "arr_of_dbl",
        "Type": "int",
        "Style": "int",
        "Value": "n",
        "Closed": "bln",
    },
    "add_nurbs_surface": {
        "PointCount": "arr_of_int",
        "Points": "arr_of_dbl",
        "KnotsU": "arr_of_int",
        "KnotsU": "arr_of_int",
        "Degree": "arr_of_int",
        "Weights": "arr_of_int",
    }, 
    "add_planar_srf": {
        "Objects": "arr_of_str",
    },
    "add_plane_surface": {
        "Plane": "arr_of_dbl",
        "DU": "dbl",
        "DV": "dbl",
    },
    "add_rail_rev_srf": {
        "Profile": "str",
        "Rail": "str",
        "Axis": "arr_of_dbl",
    },
    "add_rev_srf": {
        "Profile": "str",
        "Axis": "arr_of_dbl",
        "StartAngle": "dbl",
        "EndAngle": "dbl",
    },
    "add_srf_control_pt_grid": {
        "Count": "arr_of_int",
        "Points": "arr_of_dbl",
        "Degree": "arr_of_dbl",
    },
    "add_srf_pt": {
        "Points": "arr_of_dbl",
    },
    "add_srf_pt_grid": {
        "Count": "arr_of_int",
        "Points": "arr_of_dbl",
        "Degree": "arr_of_int",
        "Closed": "arr_of_bln",
    },
    "add_srf_section_crvs": {
        "Object": "str",
        "Plane": "arr_of_dbl",
    },
    "add_sweep1": {
        "Rail": "str",
        "Shapes": "arr_of_str",
        "StartPt": "arr_of_dbl",
        "EndPt": "arr_of_dbl",
        "Closed": "bln",
        "Style": "int",
        "StyleArg": "va",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "add_sweep2": {
        "Rails": "arr_of_str",
        "Shapes": "arr_of_str",
        "StartPt": "arr_of_dbl",
        "EndPt": "arr_of_dbl",
        "Closed": "bln",
        "SimpleSweep": "bln",
        "MaintainHeight": "bln",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "boolean_difference": {
        "Input0": "arr_of_str",
        "Input1": "arr_of_str",
        "Delete": "bln",
    },
    "boolean_intersection": {
        "Input0": "arr_of_str",
        "Input1": "arr_of_str",
        "Delete": "bln",
    },
    "boolean_union": {
        "Input": "arr_of_str",
        "Delete": "bln",
    },
    "brep_closest_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "evaluate_surface": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
    },
    "extract_iso_curve": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
        "Dir": "int",
    },
    "extrude_curve_point": {
        "Curve": "str",
        "Point": "arr_of_dbl",
    },
    "extrude_curve_straight": {
        "Curve": "str",
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
    },
    "extrude_curve_tapered": {
        "Curve": "str",
        "Distance": "dbl",
        "Direction": "arr_of_dbl",
        "BasePoint": "arr_of_dbl",
        "Angle": "dbl",
        "CornerType": "int",
    },
    "fit_surface": {
        "Object": "str",
        "Degree": "arr_of_int",
        "Tolerance": "dbl",
    },
    "is_parameter_on_surface": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
    },
    "is_point_in_surface": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "is_point_on_surface": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "rebuild_surface": {
        "Object": "str",
        "Degree": "arr_of_int",
        "PointCount": "arr_of_int",
    },
    "short_path": {
        "Surface": "str",
        "Start": "arr_of_dbl",
        "End": "arr_of_dbl",
    },
    "surface_closest_point": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
    "surface_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_dbl",
        "EndPoint": "arr_of_dbl",
        "Interval": "dbl",
        "Angle": "dbl",
    },
    "surface_curvature": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
    },
    "surface_evaluate": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
        "Derivative": "int",
    },
    "surface_frame": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
    },
    "surface_normal": {
        "Object": "str",
        "Parameter": "arr_of_dbl",
    },
    "surface_principal_curvature": {
        "Object": "str",
        "Point": "arr_of_dbl",
    },
},
transformation = {
    "is_xform_identity": {
        "Xform": "arr_of_dbl",
    },
    "is_xform_similarity": {
        "Xform": "arr_of_dbl",
    },
    "is_xform_zero": {
        "Xform": "arr_of_dbl",
    },
    "xform_c_plane_to_world": {
        "Point": "arr_of_dbl",
        "Plane": "arr_of_dbl",
    },
    "xform_compare": {
        "Xform1": "arr_of_dbl",
        "Xform2": "arr_of_dbl",
    },
    "xform_determinant": {
        "Xform": "arr_of_dbl",
    },
    "xform_inverse": {
        "Xform": "arr_of_dbl",
    },
    "xform_mirror": {
        "Point": "arr_of_dbl",
        "Normal": "arr_of_dbl",
    },
    "xform_multiply": {
        "Xform1": "arr_of_dbl",
        "Xform2": "arr_of_dbl",
    },
    "xform_planar_projection": {
        "Plane": "arr_of_dbl",
    },
    "xform_screen_to_world": {
        "Point": "arr_of_dbl",
        "View": "str",
        "Convert": "bln",
    },
    "xform_shear": {
        "Plane": "arr_of_dbl",
        "X1": "arr_of_dbl",
        "Y1": "arr_of_dbl",
        "Z1": "arr_of_dbl",
    },
    "xform_translation": {
        "Vector": "arr_of_dbl",
    },
    "xform_world_to_c_plane": {
        "Point": "arr_of_dbl",
        "Plane": "arr_of_dbl",
    },
    "xform_world_to_screen": {
        "Point": "arr_of_dbl",
        "View": "str",
        "Convert": "bln",
    },
},
user_data = {
},
user_interface = {
    "check_list_box": {
        "Items": "arr_of_str",
        "Values": "arr_of_bln",
        "Message": "str",
        "Title": "str",
    },
    "combo_list_box": {
        "Items": "arr_of_str",
        "Message": "str",
        "Title": "str",
    },
    "get_angle": {
        "Point": "arr_of_dbl",
        "Reference": "arr_of_dbl", 
        "Angle": "dbl",
        "Message": "str",
    },
    "get_boolean": {
        "Message": "str",
        "Items": "arr_of_str",
        "Defaults": "arr_of_bln",
    },
    "get_box": {
        "Mode": "int",
        "Point": "arr_of_dbl",
        "Prompt1": "str",
        "Prompt2": "str",
        "Prompt3": "str",
    },
    "get_distance": {
        "Point": "arr_of_dbl",
        "Distance": "dbl",
        "Message1": "str",
        "Message2": "str",
    },
    "get_point": {
        "Message": "str",
        "Point": "arr_of_dbl",
        "Distance": "dbl",
        "Plane": "bln",
    },
    "get_point_on_line": {
        "Message": "str",
        "Start": "arr_of_dbl",
        "End": "arr_of_dbl",
        "Track": "bln",
    },
    "get_point_on_plane": {
        "Message": "str",
        "Plane": "arr_of_dbl",
        "Point": "arr_of_dbl",
    },
    "get_points": {
        "Draw": "bln",
        "Plane": "bln",
        "Message1": "str",
        "Message2": "str",
        "MaxPoints": "int",
        "BasePoint": "arr_of_dbl",
    },
    "get_string": {
        "Message": "str",
        "String": "str",
        "Strings": "arr_of_str",
    },
    "list_box": {
        "Items": "arr_of_str",
        "Message": "str",
        "Title": "str",
    },
    "multi_list_box": {
        "Items": "arr_of_str",
        "Message": "str",
        "Title": "str",
    },
    "popup_menu": {
        "Items": "arr_of_str",
        "Modes": "arr_of_int",
        "Point": "arr_of_dbl",
        "View": "str",
    },
    "property_list_box": {
        "Items": "arr_of_str",
        "Values": "arr_of_str",
        "Message": "str",
        "Title": "str",
    },
},
utility = {
    "cull_duplicate_numbers": {
        "Numbers": "arr_of_int",
        "Tolerance": "dbl",
    },
    "cull_duplicate_points": {
        "Points": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "cull_duplicate_strings": {
        "Strings": "arr_of_int",
        "CaseSensitive": "bln",
    },
    "join_arrays": {
        "1": "arr_of_any",
        "2": "arr_of_any",
    },
    "pt2_str": {
        "Point": "arr_of_dbl",
        "Precision": "n",
        "Space": "bln",
    },
    "simplify_array": {
        "Points": "arr_of_dbl",
    },
    "sort_numbers": {
        "Numbers": "arr_of_int",
        "Ascending": "bln",
    },
    "sort_point_list": {
        "Points": "arr_of_dbl",
        "Tolerance": "dbl",
    },
    "sort_points": {
        "Points": "arr_of_dbl",
        "Ascending": "bln",
        "Order": "bln",
    },
    "sort_strings": {
        "Strings": "arr_of_str",
        "Ascending": "bln",
        "NoCase": "bln",
    },
},
view = {
    "view_c_plane": {
        "View": "str",
        "Plane": "arr_of_dbl",
    },
    "view_camera": {
        "View": "str",
        "Camera": "arr_of_dbl",
    },
    "view_camera_target": {
        "View": "str",
        "Camera": "arr_of_dbl",
        "Target": "arr_of_dbl",
    },
    "view_camera_up": {
        "View": "str",
        "UpVector": "arr_of_dbl",
    },
    "view_target": {
        "View": "str",
        "Target": "arr_of_dbl",
    },
    "zoom_bounding_box": {
        "Corners": "arr_of_dbl",
        "View": "str",
        "All": "bln",
    },
},
