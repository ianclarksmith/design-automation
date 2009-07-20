#Replace in the ??? with either "bln", "int", "dbl", or "str"

application = {
    "status_bar_point": {
        "Point": "arr_of_???",
    },
},
block = {
},
curve = {
    "add_arc": {
        "Plane": "arr_of_???",
        "Radius": "dbl",
        "Angle": "dbl",
    },
    "add_arc3_pt": {
        "Start": "arr_of_???",
        "End": "arr_of_???",
        "Point": "arr_of_???",
    },
    "add_circle": {
        "Plane": "arr_of_???",
        "Radius": "dbl",
    },
    "add_circle3_pt": {
        "Start": "arr_of_???",
        "End": "arr_of_???",
        "Point": "arr_of_???",
    },
    "add_curve": {
        "Points": "arr_of_???",
        "Degree": "int",
    },
    "add_ellipse": {
        "Plane": "arr_of_???",
        "XRadius": "dbl",
        "YRadius": "dbl",
    },
    "add_ellipse3_pt": {
        "Center": "arr_of_???",
        "Second": "arr_of_???",
        "Third": "arr_of_???",
    },
    "add_fillet_curve": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "Point0": "arr_of_???",
        "Point1": "arr_of_???",
    },
    "add_interp_crv_on_srf": {
        "Object": "str",
        "Points": "arr_of_???",
    },
    "add_interp_crv_on_srf_u_v": {
        "Object": "str",
        "Points": "arr_of_???",
    },
    "add_interp_curve": {
        "Points": "arr_of_???",
        "Degree": "int",
        "KnotStyle": "int",
        "StartTan": "arr_of_???",
        "EndTan": "arr_of_???",
    },
    "add_interp_curve_ex": {
        "Points": "arr_of_???",
        "Degree": "int",
        "KnotStyle": "int",
        "Sharp": "bln",
        "StartTangent": "arr_of_???",
        "EndTangent": "arr_of_???",
    },
    "add_line": {
        "Start": "arr_of_???",
        "End": "arr_of_???",
    },
    "add_nurbs_curve": {
        "Points": "arr_of_???",
        "Knots": "arr_of_???",
        "Degree": "int",
        "Weights": "arr_of_???",
    },
    "add_polyline": {
        "Points": "arr_of_???",
    },
    "curve_boolean_union": {
        "Curves": "arr_of_???",
    },
    "curve_closest_point": {
        "Object": "str",
        "Point": "arr_of_???",
        "Index": "int",
    },
    "curve_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
        "Interval": "dbl",
    },
    "curve_fillet_points": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "BasePoint0": "arr_of_???",
        "BasePoint1": "arr_of_???",
    },
    "curve_length": {
        "Object": "str",
        "Index": "int",
        "SubDomain": "arr_of_???",
    },
    "curve_radius": {
        "Object": "str",
        "Point": "arr_of_???",
        "Index": "int",
    },
    "extend_curve": {
        "Object": "str",
        "Type": "int",
        "Side": "int",
        "Objects": "arr_of_???",
    },
    "extend_curve_point": {
        "Object": "str",
        "Side": "int",
        "Point": "arr_of_???",
    },
    "is_curve_in_plane": {
        "Object": "str",
        "Plane": "arr_of_???",
    },
    "is_point_on_curve": {
        "Object": "str",
        "Point": "arr_of_???",
        "Index": "int",
    },
    "planar_closed_curve_containment": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr_of_???",
        "Tolerance": "dbl",
    },
    "planar_curve_collision": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr_of_???",
        "Tolerance": "dbl",
    },
    "point_in_planar_closed_curve": {
        "Point": "arr_of_???",
        "Curve": "str",
        "Plane": "arr_of_???",
        "Tolerance": "dbl",
    },
    "trim_curve": {
        "Object": "str",
        "Interval": "arr_of_???",
        "Delete": "bln",
    },
},
dimension = {
    "add_leader": {
        "Points": "arr_of_???",
        "View": "str",
        "Text": "str",
    },
},
document = {
    "create_preview_image": {
        "File": "str",
        "View": "str",
        "Size": "arr_of_???",
        "Flags": "int",
        "Wireframe": "bln",
    },
    "render_resolution": {
        "Resolution": "arr_of_???",
    },
},
geometry = {
    "add_point": {
        "Point": "arr_of_???",
    },
    "add_point_cloud": {
        "Points": "arr_of_???",
    },
    "add_points": {
        "Points": "arr_of_???",
    },
    "add_text_dot": {
        "Test": "str",
        "Point": "arr_of_???",
    },
    "point_coordinates": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "text_dot_point": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "text_object_plane": {
        "Object": "str",
        "Plane": "arr_of_???",
    },
    "text_object_point": {
        "Object": "str",
        "Point": "arr_of_???",
    },
},
group = {
    "add_objects_to_group": {
        "Objects": "arr_of_???",
        "Group": "str",
    },
    "remove_objects_from_group": {
        "Objects": "arr_of_???",
        "Group": "str",
    },
},
hatch = {
    "add_hatches": {
        "Curves": "arr_of_???",
        "Hatch": "str",
        "Scale": "dbl",
        "Rotation": "dbl",
    },
},
layer = {
},
light = {
    "add_directional_light": {
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
    },
    "add_linear_light": {
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
        "Width": "dbl",
    },
    "add_point_light": {
        "Point": "arr_of_???",
    },
    "add_rectangular_light": {
        "Origin": "arr_of_???",
        "Width": "arr_of_???",
        "Height": "arr_of_???",
    },
    "add_spot_light": {
        "Origin": "arr_of_???",
        "Radius": "dbl",
        "Apex": "arr_of_???",
    },
    "light_direction": {
        "Object": "str",
        "Direction": "arr_of_???",
    },
    "light_location": {
        "Object": "str",
        "location": "arr_of_???",
    },
},
line_and_plane = {
    "distance_to_plane": {
        "Plane": "arr_of_???",
        "Point": "arr_of_???",
    },
    "evaluate_plane": {
        "Plane": "arr_of_???",
        "Parameter": "arr_of_???",
    },
    "intersect_planes": {
        "Plane1": "arr_of_???",
        "Plane2": "arr_of_???",
        "Plane3": "arr_of_???",
    },
    "line_closest_point": {
        "Line": "arr_of_???",
        "Point": "arr_of_???",
    },
    "line_line_intersection": {
        "LineA": "arr_of_???",
        "LineB": "arr_of_???",
        "Planar": "bln",
    },
    "line_plane": {
        "Line": "arr_of_???",
    },
    "line_plane_intersection": {
        "Line": "arr_of_???",
        "Point": "arr_of_???",
    },
    "line_transform": {
        "Line": "arr_of_???",
        "Xform": "arr_of_???",
    },
    "move_plane": {
        "Plane": "arr_of_???",
        "Origin": "arr_of_???",
    },
    "plane_closest_point": {
        "Plane": "arr_of_???",
        "Point": "arr_of_???",
        "ReturnPoint": "bln",
    },
    "plane_equation": {
        "Plane": "arr_of_???",
    },
    "plane_fit_from_points": {
        "Points": "arr_of_???",
    },
    "plane_from_frame": {
        "Origin": "arr_of_???",
        "Xaxis": "arr_of_???",
        "Yaxis": "arr_of_???",
    },
    "plane_from_normal": {
        "Origin": "arr_of_???",
        "Normal": "arr_of_???",
    },
    "plane_from_points": {
        "Origin": "arr_of_???",
        "PointX": "arr_of_???",
        "PointY": "arr_of_???",
    },
    "plane_plane_intersection": {
        "Plane1": "arr_of_???",
        "Point2": "arr_of_???",
    },
    "plane_transform": {
        "Plane": "arr_of_???",
        "Xform": "arr_of_???",
    },
    "rotate_plane": {
        "Plane": "arr_of_???",
        "Angle": "dbl",
        "Axis": "arr_of_???",
    },
},
linetype = {
},
material = {
},
math = {
    "angle": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
        "World": "bln",
    },
    "angle2": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
    },
    "deviation": {
        "Numbers": "arr_of_???",
    },
    "max": {
        "Numbers": "arr_of_???",
    },
    "mean": {
        "Numbers": "arr_of_???",
    },
    "median": {
        "Numbers": "arr_of_???",
    },
    "min": {
        "Numbers": "arr_of_???",
    },
    "polar": {
        "Point": "arr_of_???",
        "Angle": "dbl",
        "Distance": "dbl",
        "Plane": "arr_of_???",
    },
    "sum": {
        "Numbers": "arr_of_???",
    },
},
mesh = {
    "add_mesh": {
        "Vertices": "arr_of_???",
        "FaceVertices": "arr_of_???",
        "VertexNormals": "arr_of_???",
        "TextureCoordinates": "arr_of_???",
        "VertexColors": "arr_of_???",
    },
    "mesh_boolean_difference": {
        "Input0": "arr_of_???",
        "Input1": "arr_of_???",
        "Delete": "bln",
    },
    "mesh_boolean_intersection": {
        "Input0": "arr_of_???",
        "Input1": "arr_of_???",
        "Delete": "bln",
    },
    "mesh_boolean_split": {
        "Input0": "arr_of_???",
        "Input1": "arr_of_???",
        "Delete": "bln",
    },
    "mesh_boolean_union": {
        "Input": "arr_of_???",
        "Delete": "bln",
    },
    "mesh_closest_point": {
        "Object": "str",
        "Point": "arr_of_???",
        "Tolerance": "dbl",
    },
    "mesh_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
        "Interval": "dbl",
        "RemoveCoincidentPoints": "bln",
    },
},
object = {
    "delete_objects": {
        "Objects": "arr_of_???",
    },
    "enable_object_mesh": {
        "Objects": "arr_of_???",
        "Enable": "bln",
    },
    "hide_objects": {
        "Objects": "arr_of_???",
    },
    "is_object_in_box": {
        "Object": "str",
        "Box": "arr_of_???",
        "Mode": "bln",
    },
    "lock_objects": {
        "Objects": "arr_of_???",
    },
    "mirror_object": {
        "Object": "str",
        "StartPt": "arr_of_???",
        "EndPt": "arr_of_???",
        "Copy": "bln",
    },
    "mirror_objects": {
        "Objects": "arr_of_???",
        "StartPt": "arr_of_???",
        "EndPt": "arr_of_???",
        "Copy": "bln",
    },
    "object_names": {
        "Objects": "arr_of_???",
        "Names": "arr_of_???",
    },
    "orient_object": {
        "Object": "str",
        "Reference": "arr_of_???",
        "Target": "arr_of_???",
        "Flags": "int",
    },
    "orient_objects": {
        "Objects": "arr_of_???",
        "Reference": "arr_of_???",
        "Target": "arr_of_???",
        "Flags": "int",
    },
    "remap_object": {
        "Object": "str",
        "SrcPlane": "arr_of_???",
        "DstPlane": "arr_of_???",
        "Copy": "bln",
    },
    "remap_objects": {
        "Object": "arr_of_???",
        "SrcPlane": "arr_of_???",
        "DstPlane": "arr_of_???",
        "Copy": "bln",
    },
    "rotate_object": {
        "Object": "str",
        "Point": "arr_of_???",
        "Angle": "dbl",
        "Axis": "arr_of_???",
        "Copy": "bln",
    },
    "rotate_objects": {
        "Objects": "arr_of_???",
        "Point": "arr_of_???",
        "Angle": "dbl",
        "Axis": "arr_of_???",
        "Copy": "bln",
    },
    "scale_object": {
        "Object": "str",
        "Origin": "arr_of_???",
        "Scale": "arr_of_???",
        "Copy": "bln",
    },
    "scale_objects": {
        "Objects": "arr_of_???",
        "Origin": "arr_of_???",
        "Scale": "arr_of_???",
        "Copy": "bln",
    },
    "select_objects": {
        "Objects": "arr_of_???",
    },
    "shear_object": {
        "Object": "str",
        "Origin": "arr_of_???",
        "RefPt": "arr_of_???",
        "Scale": "arr_of_???",
        "Copy": "bln",
    },
    "shear_objects": {
        "Objects": "arr_of_???",
        "Origin": "arr_of_???",
        "RefPt": "arr_of_???",
        "Scale": "arr_of_???",
        "Copy": "bln",
    },
    "show_objects": {
        "Objects": "arr_of_???",
    },
    "unlock_objects": {
        "Objects": "arr_of_???",
    },
    "unselect_objects": {
        "Objects": "arr_of_???",
    },
},
object_grip = {
    "object_grip_location": {
        "Object": "str",
        "Index": "int",
        "Point": "arr_of_???",
    },
    "object_grip_locations": {
        "Object": "str",
        "Points": "arr_of_???",
    },
},
point_and_vector = {
    "is_vector_parallel_to": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "is_vector_perpendicular_to": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "is_vector_tiny": {
        "Vector": "arr_of_???",
    },
    "is_vector_zero": {
        "Vector": "arr_of_???",
    },
    "point_add": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
    },
    "point_array_bounding_box": {
        "Points": "arr_of_???",
        "View": "str",
        "WorldCoords": "bln",
    },
    "point_array_closest_point": {
        "Points": "arr_of_???",
        "Point": "arr_of_???",
    },
    "point_array_transform": {
        "Points": "arr_of_???",
        "Xform": "arr_of_???",
    },
    "point_compare": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
        "Tolerance": "dbl",
    },
    "point_divide": {
        "Point": "arr_of_???",
        "Scale": "dbl",
    },
    "point_scale": {
        "Point": "arr_of_???",
        "Scale": "dbl",
    },
    "point_subtract": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
    },
    "point_transform": {
        "Point": "arr_of_???",
        "Xform": "arr_of_???",
    },
    "points_are_coplanar": {
        "Points": "arr_of_???",
        "Tolerance": "dbl",
    },
    "pull_points": {
        "Object": "str",
        "Points": "arr_of_???",
    },
    "vector_add": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_compare": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_create": {
        "Point1": "arr_of_???",
        "Point2": "arr_of_???",
    },
    "vector_cross_product": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_divide": {
        "Vector": "arr_of_???",
        "Divide": "dbl",
    },
    "vector_dot_product": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_length": {
        "Vector": "arr_of_???",
    },
    "vector_multiply": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_reverse": {
        "Vector": "arr_of_???",
    },
    "vector_rotate": {
        "Vector": "arr_of_???",
        "Angle": "dbl",
        "Axis": "arr_of_???",
    },
    "vector_scale": {
        "Vector": "arr_of_???",
        "Scale": "dbl",
    },
    "vector_subtract": {
        "Vector1": "arr_of_???",
        "Vector2": "arr_of_???",
    },
    "vector_transform": {
        "Vector": "arr_of_???",
        "Xform": "arr_of_???",
    },
    "vector_unitize": {
        "Vector": "arr_of_???",
    },
},
selection = {
    "get_object": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_???",
    },
    "get_object_ex": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_???",
    },
    "get_objects": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_???",
    },
    "get_objects_ex": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr_of_???",
    },
},
surface_and_polysurface = {
    "add_box": {
        "Corners": "arr_of_???",
    },
    "add_cut_plane": {
        "Objects": "arr_of_???",
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
        "Normal": "arr_of_???",
    },
    "add_edge_srf": {
        "Objects": "arr_of_???",
    },
    "add_loft_srf": {
        "Objects": "arr_of_???",
        "StartPt": "arr_of_???",
        "EndPt": "arr_of_???",
        "Type": "int",
        "Style": "int",
        "Value": "n",
        "Closed": "bln",
    },
    "add_nurbs_surface": {
        "PointCount": "arr_of_???",
        "Points": "arr_of_???",
        "KnotsU": "arr_of_???",
        "KnotsU": "arr_of_???",
        "Degree": "arr_of_???",
        "Weights": "arr_of_???",
    },
    "add_planar_srf": {
        "Objects": "arr_of_???",
    },
    "add_plane_surface": {
        "Plane": "arr_of_???",
        "DU": "dbl",
        "DV": "dbl",
    },
    "add_rail_rev_srf": {
        "Profile": "str",
        "Rail": "str",
        "Axis": "arr_of_???",
    },
    "add_rev_srf": {
        "Profile": "str",
        "Axis": "arr_of_???",
        "StartAngle": "dbl",
        "EndAngle": "dbl",
    },
    "add_srf_control_pt_grid": {
        "Count": "arr_of_???",
        "Points": "arr_of_???",
        "Degree": "arr_of_???",
    },
    "add_srf_pt": {
        "Points": "arr_of_???",
    },
    "add_srf_pt_grid": {
        "Count": "arr_of_???",
        "Points": "arr_of_???",
        "Degree": "arr_of_???",
        "Closed": "arr_of_???",
    },
    "add_srf_section_crvs": {
        "Object": "str",
        "Plane": "arr_of_???",
    },
    "add_sweep1": {
        "Rail": "str",
        "Shapes": "arr_of_???",
        "StartPt": "arr_of_???",
        "EndPt": "arr_of_???",
        "Closed": "bln",
        "Style": "int",
        "StyleArg": "va",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "add_sweep2": {
        "Rails": "arr_of_???",
        "Shapes": "arr_of_???",
        "StartPt": "arr_of_???",
        "EndPt": "arr_of_???",
        "Closed": "bln",
        "SimpleSweep": "bln",
        "MaintainHeight": "bln",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "boolean_difference": {
        "Input0": "arr_of_???",
        "Input1": "arr_of_???",
        "Delete": "bln",
    },
    "boolean_intersection": {
        "Input0": "arr_of_???",
        "Input1": "arr_of_???",
        "Delete": "bln",
    },
    "boolean_union": {
        "Input": "arr_of_???",
        "Delete": "bln",
    },
    "brep_closest_point": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "evaluate_surface": {
        "Object": "str",
        "Parameter": "arr_of_???",
    },
    "extract_iso_curve": {
        "Object": "str",
        "Parameter": "arr_of_???",
        "Dir": "int",
    },
    "extrude_curve_point": {
        "Curve": "str",
        "Point": "arr_of_???",
    },
    "extrude_curve_straight": {
        "Curve": "str",
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
    },
    "extrude_curve_tapered": {
        "Curve": "str",
        "Distance": "dbl",
        "Direction": "arr_of_???",
        "BasePoint": "arr_of_???",
        "Angle": "dbl",
        "CornerType": "int",
    },
    "fit_surface": {
        "Object": "str",
        "Degree": "arr_of_???",
        "Tolerance": "dbl",
    },
    "is_parameter_on_surface": {
        "Object": "str",
        "Parameter": "arr_of_???",
    },
    "is_point_in_surface": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "is_point_on_surface": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "rebuild_surface": {
        "Object": "str",
        "Degree": "arr_of_???",
        "PointCount": "arr_of_???",
    },
    "short_path": {
        "Surface": "str",
        "Start": "arr_of_???",
        "End": "arr_of_???",
    },
    "surface_closest_point": {
        "Object": "str",
        "Point": "arr_of_???",
    },
    "surface_contour_points": {
        "Object": "str",
        "StartPoint": "arr_of_???",
        "EndPoint": "arr_of_???",
        "Interval": "dbl",
        "Angle": "dbl",
    },
    "surface_curvature": {
        "Object": "str",
        "Parameter": "arr_of_???",
    },
    "surface_evaluate": {
        "Object": "str",
        "Parameter": "arr_of_???",
        "Derivative": "int",
    },
    "surface_frame": {
        "Object": "str",
        "Parameter": "arr_of_???",
    },
    "surface_normal": {
        "Object": "str",
        "Parameter": "arr_of_???",
    },
    "surface_principal_curvature": {
        "Object": "str",
        "Point": "arr_of_???",
    },
},
transformation = {
    "is_xform_identity": {
        "Xform": "arr_of_???",
    },
    "is_xform_similarity": {
        "Xform": "arr_of_???",
    },
    "is_xform_zero": {
        "Xform": "arr_of_???",
    },
    "xform_c_plane_to_world": {
        "Point": "arr_of_???",
        "Plane": "arr_of_???",
    },
    "xform_compare": {
        "Xform1": "arr_of_???",
        "Xform2": "arr_of_???",
    },
    "xform_determinant": {
        "Xform": "arr_of_???",
    },
    "xform_inverse": {
        "Xform": "arr_of_???",
    },
    "xform_mirror": {
        "Point": "arr_of_???",
        "Normal": "arr_of_???",
    },
    "xform_multiply": {
        "Xform1": "arr_of_???",
        "Xform2": "arr_of_???",
    },
    "xform_planar_projection": {
        "Plane": "arr_of_???",
    },
    "xform_screen_to_world": {
        "Point": "arr_of_???",
        "View": "str",
        "Convert": "bln",
    },
    "xform_shear": {
        "Plane": "arr_of_???",
        "X1": "arr_of_???",
        "Y1": "arr_of_???",
        "Z1": "arr_of_???",
    },
    "xform_translation": {
        "Vector": "arr_of_???",
    },
    "xform_world_to_c_plane": {
        "Point": "arr_of_???",
        "Plane": "arr_of_???",
    },
    "xform_world_to_screen": {
        "Point": "arr_of_???",
        "View": "str",
        "Convert": "bln",
    },
},
user_data = {
},
user_interface = {
    "check_list_box": {
        "Items": "arr_of_???",
        "Values": "arr_of_???",
        "Message": "str",
        "Title": "str",
    },
    "combo_list_box": {
        "Items": "arr_of_???",
        "Message": "str",
        "Title": "str",
    },
    "get_angle": {
        "Point": "arr_of_???",
        "Reference": "arr_of_???",
        "Angle": "dbl",
        "Message": "str",
    },
    "get_boolean": {
        "Message": "str",
        "Items": "arr_of_???",
        "Defaults": "arr_of_???",
    },
    "get_box": {
        "Mode": "int",
        "Point": "arr_of_???",
        "Prompt1": "str",
        "Prompt2": "str",
        "Prompt3": "str",
    },
    "get_distance": {
        "Point": "arr_of_???",
        "Distance": "dbl",
        "Message1": "str",
        "Message2": "str",
    },
    "get_point": {
        "Message": "str",
        "Point": "arr_of_???",
        "Distance": "dbl",
        "Plane": "bln",
    },
    "get_point_on_line": {
        "Message": "str",
        "Start": "arr_of_???",
        "End": "arr_of_???",
        "Track": "bln",
    },
    "get_point_on_plane": {
        "Message": "str",
        "Plane": "arr_of_???",
        "Point": "arr_of_???",
    },
    "get_points": {
        "Draw": "bln",
        "Plane": "bln",
        "Message1": "str",
        "Message2": "str",
        "MaxPoints": "int",
        "BasePoint": "arr_of_???",
    },
    "get_string": {
        "Message": "str",
        "String": "str",
        "Strings": "arr_of_???",
    },
    "list_box": {
        "Items": "arr_of_???",
        "Message": "str",
        "Title": "str",
    },
    "multi_list_box": {
        "Items": "arr_of_???",
        "Message": "str",
        "Title": "str",
    },
    "popup_menu": {
        "Items": "arr_of_???",
        "Modes": "arr_of_???",
        "Point": "arr_of_???",
        "View": "str",
    },
    "property_list_box": {
        "Items": "arr_of_???",
        "Values": "arr_of_???",
        "Message": "str",
        "Title": "str",
    },
},
utility = {
    "cull_duplicate_numbers": {
        "Numbers": "arr_of_???",
        "Tolerance": "dbl",
    },
    "cull_duplicate_points": {
        "Points": "arr_of_???",
        "Tolerance": "dbl",
    },
    "cull_duplicate_strings": {
        "Strings": "arr_of_???",
        "CaseSensitive": "bln",
    },
    "join_arrays": {
        "1": "arr_of_???",
        "2": "arr_of_???",
    },
    "pt2_str": {
        "Point": "arr_of_???",
        "Precision": "n",
        "Space": "bln",
    },
    "simplify_array": {
        "Points": "arr_of_???",
    },
    "sort_numbers": {
        "Numbers": "arr_of_???",
        "Ascending": "bln",
    },
    "sort_point_list": {
        "Points": "arr_of_???",
        "Tolerance": "dbl",
    },
    "sort_points": {
        "Points": "arr_of_???",
        "Ascending": "bln",
        "Order": "bln",
    },
    "sort_strings": {
        "Strings": "arr_of_???",
        "Ascending": "bln",
        "NoCase": "bln",
    },
},
view = {
    "view_c_plane": {
        "View": "str",
        "Plane": "arr_of_???",
    },
    "view_camera": {
        "View": "str",
        "Camera": "arr_of_???",
    },
    "view_camera_target": {
        "View": "str",
        "Camera": "arr_of_???",
        "Target": "arr_of_???",
    },
    "view_camera_up": {
        "View": "str",
        "UpVector": "arr_of_???",
    },
    "view_target": {
        "View": "str",
        "Target": "arr_of_???",
    },
    "zoom_bounding_box": {
        "Corners": "arr_of_???",
        "View": "str",
        "All": "bln",
    },
},
