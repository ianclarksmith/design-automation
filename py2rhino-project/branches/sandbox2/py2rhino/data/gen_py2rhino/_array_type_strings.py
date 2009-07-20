"application": {
    "status_bar_point": {
        "Point": "arr",
    },
},
"block": {
    "insert_block": {
        "Name": "str",
        "Point": "arr",
        "Scale": "arr",
        "Angle": "dbl",
        "Normal": "arr",
        "Xform": "arr",
    },
},
"curve": {
    "add_arc": {
        "Plane": "arr",
        "Radius": "dbl",
        "Angle": "dbl",
    },
    "add_arc3_pt": {
        "Start": "arr",
        "End": "arr",
        "Point": "arr",
    },
    "add_circle": {
        "Plane": "arr",
        "Radius": "dbl",
    },
    "add_circle3_pt": {
        "Start": "arr",
        "End": "arr",
        "Point": "arr",
    },
    "add_curve": {
        "Points": "arr",
        "Degree": "int",
    },
    "add_ellipse": {
        "Plane": "arr",
        "XRadius": "dbl",
        "YRadius": "dbl",
    },
    "add_ellipse3_pt": {
        "Center": "arr",
        "Second": "arr",
        "Third": "arr",
    },
    "add_fillet_curve": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "Point0": "arr",
        "Point1": "arr",
    },
    "add_interp_crv_on_srf": {
        "Object": "str",
        "Points": "arr",
    },
    "add_interp_crv_on_srf_u_v": {
        "Object": "str",
        "Points": "arr",
    },
    "add_interp_curve": {
        "Points": "arr",
        "Degree": "int",
        "KnotStyle": "int",
        "StartTan": "arr",
        "EndTan": "arr",
    },
    "add_interp_curve_ex": {
        "Points": "arr",
        "Degree": "int",
        "KnotStyle": "int",
        "Sharp": "bln",
        "StartTangent": "arr",
        "EndTangent": "arr",
    },
    "add_line": {
        "Start": "arr",
        "End": "arr",
    },
    "add_nurbs_curve": {
        "Points": "arr",
        "Knots": "arr",
        "Degree": "int",
        "Weights": "arr",
    },
    "add_polyline": {
        "Points": "arr",
    },
    "curve_area": {
        "Object": "str",
        "Objects": "arr",
    },
    "curve_area_centroid": {
        "Object": "str",
        "Objects": "arr",
    },
    "curve_boolean_union": {
        "Curves": "arr",
    },
    "curve_closest_object": {
        "Curve": "str",
        "Object": "str",
        "Objects": "arr",
    },
    "curve_closest_point": {
        "Object": "str",
        "Point": "arr",
        "Index": "int",
    },
    "curve_contour_points": {
        "Object": "str",
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Interval": "dbl",
    },
    "curve_fillet_points": {
        "Curve0": "str",
        "Curve1": "str",
        "Radius": "dbl",
        "BasePoint0": "arr",
        "BasePoint1": "arr",
    },
    "curve_length": {
        "Object": "str",
        "Index": "int",
        "SubDomain": "arr",
    },
    "curve_radius": {
        "Object": "str",
        "Point": "arr",
        "Index": "int",
    },
    "explode_curves": {
        "Object": "str",
        "Objects": "arr",
        "Delete": "bln",
    },
    "extend_curve": {
        "Object": "str",
        "Type": "int",
        "Side": "int",
        "Objects": "arr",
    },
    "extend_curve_point": {
        "Object": "str",
        "Side": "int",
        "Point": "arr",
    },
    "is_curve_in_plane": {
        "Object": "str",
        "Plane": "arr",
    },
    "is_point_on_curve": {
        "Object": "str",
        "Point": "arr",
        "Index": "int",
    },
    "offset_curve": {
        "Object": "str",
        "Direction": "arr",
        "Normal": "arr",
        "Style": "int",
    },
    "planar_closed_curve_containment": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr",
        "Tolerance": "dbl",
    },
    "planar_curve_collision": {
        "Curve1": "str",
        "Curve2": "str",
        "Plane": "arr",
        "Tolerance": "dbl",
    },
    "point_in_planar_closed_curve": {
        "Point": "arr",
        "Curve": "str",
        "Plane": "arr",
        "Tolerance": "dbl",
    },
    "project_curve_to_mesh": {
        "Curve": "str",
        "Curves": "arr",
        "Mesh": "str",
        "Meshes": "arr",
        "Direction": "arr",
    },
    "project_curve_to_surface": {
        "Curve": "str",
        "Curves": "arr",
        "Surface": "str",
        "Surfaces": "arr",
        "Direction": "arr",
    },
    "split_curve": {
        "Object": "str",
        "Parameter": "dbl",
        "Parameters": "arr",
        "Delete": "bln",
    },
    "trim_curve": {
        "Object": "str",
        "Interval": "arr",
        "Delete": "bln",
    },
},
"dimension": {
    "add_leader": {
        "Points": "arr",
        "View": "str",
        "Text": "str",
    },
},
"document": {
    "create_preview_image": {
        "File": "str",
        "View": "str",
        "Size": "arr",
        "Flags": "int",
        "Wireframe": "bln",
    },
    "render_resolution": {
        "Resolution": "arr",
    },
},
"geometry": {
    "add_clipping_plane": {
        "Plane": "arr",
        "DU": "dbl",
        "DV": "dbl",
        "View": "str",
        "Views": "arr",
    },
    "add_point": {
        "Point": "arr",
    },
    "add_point_cloud": {
        "Points": "arr",
    },
    "add_points": {
        "Points": "arr",
    },
    "add_text": {
        "Text": "str",
        "Point": "arr",
        "Plane": "arr",
        "Height": "dbl",
        "Font": "str",
        "Style": "int",
    },
    "add_text_dot": {
        "Test": "str",
        "Point": "arr",
    },
    "bounding_box": {
        "Object": "str",
        "Objects": "arr",
        "View": "str",
        "WorldCoords": "bln",
    },
    "point_coordinates": {
        "Object": "str",
        "Point": "arr",
    },
    "text_dot_point": {
        "Object": "str",
        "Point": "arr",
    },
    "text_object_plane": {
        "Object": "str",
        "Plane": "arr",
    },
    "text_object_point": {
        "Object": "str",
        "Point": "arr",
    },
},
"group": {
    "add_objects_to_group": {
        "Objects": "arr",
        "Group": "str",
    },
    "remove_objects_from_group": {
        "Objects": "arr",
        "Group": "str",
    },
},
"hatch": {
    "add_hatches": {
        "Curves": "arr",
        "Hatch": "str",
        "Scale": "dbl",
        "Rotation": "dbl",
    },
},
"layer": {
},
"light": {
    "add_directional_light": {
        "StartPoint": "arr",
        "EndPoint": "arr",
    },
    "add_linear_light": {
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Width": "dbl",
    },
    "add_point_light": {
        "Point": "arr",
    },
    "add_rectangular_light": {
        "Origin": "arr",
        "Width": "arr",
        "Height": "arr",
    },
    "add_spot_light": {
        "Origin": "arr",
        "Radius": "dbl",
        "Apex": "arr",
    },
    "light_direction": {
        "Object": "str",
        "Direction": "arr",
    },
    "light_location": {
        "Object": "str",
        "location": "arr",
    },
},
"line_and_plane": {
    "distance_to_plane": {
        "Plane": "arr",
        "Point": "arr",
    },
    "evaluate_plane": {
        "Plane": "arr",
        "Parameter": "arr",
    },
    "intersect_planes": {
        "Plane1": "arr",
        "Plane2": "arr",
        "Plane3": "arr",
    },
    "line_closest_point": {
        "Line": "arr",
        "Point": "arr",
    },
    "line_is_farther_than": {
        "Line": "arr",
        "Distance": "dbl",
        "Point": "arr",
        "Line2": "arr",
    },
    "line_line_intersection": {
        "LineA": "arr",
        "LineB": "arr",
        "Planar": "bln",
    },
    "line_max_distance_to": {
        "Line": "arr",
        "Point": "arr",
        "Line2": "arr",
    },
    "line_min_distance_to": {
        "Line": "arr",
        "Point": "arr",
        "Line2": "arr",
    },
    "line_plane": {
        "Line": "arr",
    },
    "line_plane_intersection": {
        "Line": "arr",
        "Point": "arr",
    },
    "line_transform": {
        "Line": "arr",
        "Xform": "arr",
    },
    "move_plane": {
        "Plane": "arr",
        "Origin": "arr",
    },
    "plane_closest_point": {
        "Plane": "arr",
        "Point": "arr",
        "ReturnPoint": "bln",
    },
    "plane_equation": {
        "Plane": "arr",
    },
    "plane_fit_from_points": {
        "Points": "arr",
    },
    "plane_from_frame": {
        "Origin": "arr",
        "Xaxis": "arr",
        "Yaxis": "arr",
    },
    "plane_from_normal": {
        "Origin": "arr",
        "Normal": "arr",
    },
    "plane_from_points": {
        "Origin": "arr",
        "PointX": "arr",
        "PointY": "arr",
    },
    "plane_plane_intersection": {
        "Plane1": "arr",
        "Point2": "arr",
    },
    "plane_transform": {
        "Plane": "arr",
        "Xform": "arr",
    },
    "rotate_plane": {
        "Plane": "arr",
        "Angle": "dbl",
        "Axis": "arr",
    },
},
"linetype": {
},
"material": {
    "match_material": {
        "SrcMaterialIndex": "int",
        "SrcObject": "str",
        "DestObject": "str",
        "DestObjects": "arr",
    },
},
"math": {
    "angle": {
        "Point1": "arr",
        "Point2": "arr",
        "World": "bln",
    },
    "angle2": {
        "Point1": "arr",
        "Point2": "arr",
    },
    "deviation": {
        "Numbers": "arr",
    },
    "distance": {
        "Point1": "arr",
        "Point2": "arr",
        "PointArray": "arr",
    },
    "max": {
        "Numbers": "arr",
    },
    "mean": {
        "Numbers": "arr",
    },
    "median": {
        "Numbers": "arr",
    },
    "min": {
        "Numbers": "arr",
    },
    "polar": {
        "Point": "arr",
        "Angle": "dbl",
        "Distance": "dbl",
        "Plane": "arr",
    },
    "sum": {
        "Numbers": "arr",
    },
},
"mesh": {
    "add_mesh": {
        "Vertices": "arr",
        "FaceVertices": "arr",
        "VertexNormals": "arr",
        "TextureCoordinates": "arr",
        "VertexColors": "arr",
    },
    "explode_meshes": {
        "Object": "str",
        "Objects": "arr",
        "Delete": "bln",
    },
    "mesh_area": {
        "Object": "str",
        "Objects": "arr",
    },
    "mesh_boolean_difference": {
        "Input0": "arr",
        "Input1": "arr",
        "Delete": "bln",
    },
    "mesh_boolean_intersection": {
        "Input0": "arr",
        "Input1": "arr",
        "Delete": "bln",
    },
    "mesh_boolean_split": {
        "Input0": "arr",
        "Input1": "arr",
        "Delete": "bln",
    },
    "mesh_boolean_union": {
        "Input": "arr",
        "Delete": "bln",
    },
    "mesh_closest_point": {
        "Object": "str",
        "Point": "arr",
        "Tolerance": "dbl",
    },
    "mesh_contour_points": {
        "Object": "str",
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Interval": "dbl",
        "RemoveCoincidentPoints": "bln",
    },
    "mesh_vertex_colors": {
        "Object": "str",
        "VertexColors": "arr",
        "Null": "arr",
    },
    "mesh_volume": {
        "Object": "str",
        "Objects": "arr",
    },
},
"object": {
    "box_morph_object": {
        "Object": "str",
        "Objects": "arr",
        "BoxPoints": "arr",
        "Copy": "bln",
    },
    "copy_object": {
        "Object": "str",
        "Start": "arr",
        "End": "arr",
        "Translation": "arr",
    },
    "copy_objects": {
        "Objects": "arr",
        "Start": "arr",
        "End": "arr",
        "Translation": "arr",
    },
    "delete_objects": {
        "Objects": "arr",
    },
    "enable_object_mesh": {
        "Objects": "arr",
        "Enable": "bln",
    },
    "flash_object": {
        "Object": "str",
        "Objects": "arr",
        "Style": "bln",
    },
    "hide_objects": {
        "Objects": "arr",
    },
    "is_object_in_box": {
        "Object": "str",
        "Box": "arr",
        "Mode": "bln",
    },
    "lock_objects": {
        "Objects": "arr",
    },
    "match_object_attributes": {
        "Target": "str",
        "Targets": "arr",
        "Source": "str",
    },
    "mirror_object": {
        "Object": "str",
        "StartPt": "arr",
        "EndPt": "arr",
        "Copy": "bln",
    },
    "mirror_objects": {
        "Objects": "arr",
        "StartPt": "arr",
        "EndPt": "arr",
        "Copy": "bln",
    },
    "move_object": {
        "Object": "str",
        "Start": "arr",
        "End": "arr",
        "Translation": "arr",
    },
    "move_objects": {
        "Objects": "arr",
        "Start": "arr",
        "End": "arr",
        "Translation": "arr",
    },
    "object_color": {
        "Object": "str",
        "Objects": "arr",
        "Color": "lng",
    },
    "object_color_source": {
        "Object": "str",
        "Objects": "arr",
        "Source": "int",
    },
    "object_layer": {
        "Object": "str",
        "Objects": "arr",
        "Layer": "str",
    },
    "object_linetype": {
        "Object": "str",
        "Objects": "arr",
        "Layer": "str",
    },
    "object_linetype_source": {
        "Object": "str",
        "Objects": "arr",
        "Source": "int",
    },
    "object_material_source": {
        "Object": "str",
        "Objects": "arr",
        "Source": "int",
    },
    "object_name": {
        "Object": "str",
        "Objects": "arr",
        "Name": "str",
    },
    "object_names": {
        "Objects": "arr",
        "Names": "arr",
    },
    "object_print_color": {
        "Object": "str",
        "Objects": "arr",
        "Color": "lng",
    },
    "object_print_color_source": {
        "Object": "str",
        "Objects": "arr",
        "Source": "int",
    },
    "object_print_width": {
        "Object": "str",
        "Objects": "arr",
        "Width": "dbl",
    },
    "object_print_width_source": {
        "Object": "str",
        "Objects": "arr",
        "Source": "int",
    },
    "object_u_r_l": {
        "Object": "str",
        "Objects": "arr",
        "URL": "str",
    },
    "orient_object": {
        "Object": "str",
        "Reference": "arr",
        "Target": "arr",
        "Flags": "int",
    },
    "orient_objects": {
        "Objects": "arr",
        "Reference": "arr",
        "Target": "arr",
        "Flags": "int",
    },
    "remap_object": {
        "Object": "str",
        "SrcPlane": "arr",
        "DstPlane": "arr",
        "Copy": "bln",
    },
    "remap_objects": {
        "Object": "arr",
        "SrcPlane": "arr",
        "DstPlane": "arr",
        "Copy": "bln",
    },
    "rotate_object": {
        "Object": "str",
        "Point": "arr",
        "Angle": "dbl",
        "Axis": "arr",
        "Copy": "bln",
    },
    "rotate_objects": {
        "Objects": "arr",
        "Point": "arr",
        "Angle": "dbl",
        "Axis": "arr",
        "Copy": "bln",
    },
    "scale_object": {
        "Object": "str",
        "Origin": "arr",
        "Scale": "arr",
        "Copy": "bln",
    },
    "scale_objects": {
        "Objects": "arr",
        "Origin": "arr",
        "Scale": "arr",
        "Copy": "bln",
    },
    "select_objects": {
        "Objects": "arr",
    },
    "shear_object": {
        "Object": "str",
        "Origin": "arr",
        "RefPt": "arr",
        "Scale": "arr",
        "Copy": "bln",
    },
    "shear_objects": {
        "Objects": "arr",
        "Origin": "arr",
        "RefPt": "arr",
        "Scale": "arr",
        "Copy": "bln",
    },
    "show_objects": {
        "Objects": "arr",
    },
    "transform_object": {
        "Object": "str",
        "Matrix": "arr",
        "Copy": "bln",
    },
    "transform_objects": {
        "Objects": "arr",
        "Matrix": "arr",
        "Copy": "bln",
    },
    "unlock_objects": {
        "Objects": "arr",
    },
    "unselect_objects": {
        "Objects": "arr",
    },
},
"object_grip": {
    "object_grip_location": {
        "Object": "str",
        "Index": "int",
        "Point": "arr",
    },
    "object_grip_locations": {
        "Object": "str",
        "Points": "arr",
    },
},
"point_and_vector": {
    "is_vector_parallel_to": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "is_vector_perpendicular_to": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "is_vector_tiny": {
        "Vector": "arr",
    },
    "is_vector_zero": {
        "Vector": "arr",
    },
    "point_add": {
        "Point1": "arr",
        "Point2": "arr",
    },
    "point_array_bounding_box": {
        "Points": "arr",
        "View": "str",
        "WorldCoords": "bln",
    },
    "point_array_closest_point": {
        "Points": "arr",
        "Point": "arr",
    },
    "point_array_transform": {
        "Points": "arr",
        "Xform": "arr",
    },
    "point_compare": {
        "Point1": "arr",
        "Point2": "arr",
        "Tolerance": "dbl",
    },
    "point_divide": {
        "Point": "arr",
        "Scale": "dbl",
    },
    "point_scale": {
        "Point": "arr",
        "Scale": "dbl",
    },
    "point_subtract": {
        "Point1": "arr",
        "Point2": "arr",
    },
    "point_transform": {
        "Point": "arr",
        "Xform": "arr",
    },
    "points_are_coplanar": {
        "Points": "arr",
        "Tolerance": "dbl",
    },
    "project_point_to_mesh": {
        "Points": "arr",
        "Points": "arr",
        "Mesh": "str",
        "Meshes": "arr",
        "Direction": "arr",
    },
    "project_point_to_surface": {
        "Points": "arr",
        "Points": "arr",
        "Surface": "str",
        "Surfaces": "arr",
        "Direction": "arr",
    },
    "pull_points": {
        "Object": "str",
        "Points": "arr",
    },
    "vector_add": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_compare": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_create": {
        "Point1": "arr",
        "Point2": "arr",
    },
    "vector_cross_product": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_divide": {
        "Vector": "arr",
        "Divide": "dbl",
    },
    "vector_dot_product": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_length": {
        "Vector": "arr",
    },
    "vector_multiply": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_reverse": {
        "Vector": "arr",
    },
    "vector_rotate": {
        "Vector": "arr",
        "Angle": "dbl",
        "Axis": "arr",
    },
    "vector_scale": {
        "Vector": "arr",
        "Scale": "dbl",
    },
    "vector_subtract": {
        "Vector1": "arr",
        "Vector2": "arr",
    },
    "vector_transform": {
        "Vector": "arr",
        "Xform": "arr",
    },
    "vector_unitize": {
        "Vector": "arr",
    },
},
"selection": {
    "get_object": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr",
    },
    "get_object_ex": {
        "Message": "str",
        "Type": "int",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr",
    },
    "get_objects": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr",
    },
    "get_objects_ex": {
        "Message": "str",
        "Type": "int",
        "Group": "bln",
        "PreSelect": "bln",
        "Select": "bln",
        "Objects": "arr",
    },
},
"surface_and_polysurface": {
    "add_box": {
        "Corners": "arr",
    },
    "add_cone": {
        "Base": "arr",
        "Plane": "arr",
        "Height": "arr",
        "Height": "dbl",
        "Radius": "dbl",
        "Cap": "bln",
    },
    "add_cut_plane": {
        "Objects": "arr",
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Normal": "arr",
    },
    "add_cylinder": {
        "Base": "arr",
        "Plane": "arr",
        "Height": "arr",
        "Height": "dbl",
        "Radius": "dbl",
        "Cap": "bln",
    },
    "add_edge_srf": {
        "Objects": "arr",
    },
    "add_loft_srf": {
        "Objects": "arr",
        "StartPt": "arr",
        "EndPt": "arr",
        "Type": "int",
        "Style": "int",
        "Value": "n",
        "Closed": "bln",
    },
    "add_nurbs_surface": {
        "PointCount": "arr",
        "Points": "arr",
        "KnotsU": "arr",
        "KnotsU": "arr",
        "Degree": "arr",
        "Weights": "arr",
    },
    "add_planar_srf": {
        "Objects": "arr",
    },
    "add_plane_surface": {
        "Plane": "arr",
        "DU": "dbl",
        "DV": "dbl",
    },
    "add_rail_rev_srf": {
        "Profile": "str",
        "Rail": "str",
        "Axis": "arr",
    },
    "add_rev_srf": {
        "Profile": "str",
        "Axis": "arr",
        "StartAngle": "dbl",
        "EndAngle": "dbl",
    },
    "add_sphere": {
        "Center": "arr",
        "Plane": "arr",
        "Radius": "dbl",
    },
    "add_srf_contour_crvs": {
        "Object": "str",
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Plane": "arr",
        "Interval": "dbl",
    },
    "add_srf_control_pt_grid": {
        "Count": "arr",
        "Points": "arr",
        "Degree": "arr",
    },
    "add_srf_pt": {
        "Points": "arr",
    },
    "add_srf_pt_grid": {
        "Count": "arr",
        "Points": "arr",
        "Degree": "arr",
        "Closed": "arr",
    },
    "add_srf_section_crvs": {
        "Object": "str",
        "Plane": "arr",
    },
    "add_sweep1": {
        "Rail": "str",
        "Shapes": "arr",
        "StartPt": "arr",
        "EndPt": "arr",
        "Closed": "bln",
        "Style": "int",
        "StyleArg": "va",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "add_sweep2": {
        "Rails": "arr",
        "Shapes": "arr",
        "StartPt": "arr",
        "EndPt": "arr",
        "Closed": "bln",
        "SimpleSweep": "bln",
        "MaintainHeight": "bln",
        "Simplify": "int",
        "SimplifyArg": "va",
    },
    "add_torus": {
        "Base": "arr",
        "Plane": "arr",
        "MajorRadius": "dbl",
        "MinorRadius": "dbl",
        "Direction": "arr",
    },
    "boolean_difference": {
        "Input0": "arr",
        "Input1": "arr",
        "Delete": "bln",
    },
    "boolean_intersection": {
        "Input0": "arr",
        "Input1": "arr",
        "Delete": "bln",
    },
    "boolean_union": {
        "Input": "arr",
        "Delete": "bln",
    },
    "brep_closest_point": {
        "Object": "str",
        "Point": "arr",
    },
    "evaluate_surface": {
        "Object": "str",
        "Parameter": "arr",
    },
    "explode_polysurfaces": {
        "Object": "str",
        "Objects": "arr",
        "Delete": "bln",
    },
    "extract_iso_curve": {
        "Object": "str",
        "Parameter": "arr",
        "Dir": "int",
    },
    "extrude_curve_point": {
        "Curve": "str",
        "Point": "arr",
    },
    "extrude_curve_straight": {
        "Curve": "str",
        "StartPoint": "arr",
        "EndPoint": "arr",
    },
    "extrude_curve_tapered": {
        "Curve": "str",
        "Distance": "dbl",
        "Direction": "arr",
        "BasePoint": "arr",
        "Angle": "dbl",
        "CornerType": "int",
    },
    "fit_surface": {
        "Object": "str",
        "Degree": "arr",
        "Tolerance": "dbl",
    },
    "is_parameter_on_surface": {
        "Object": "str",
        "Parameter": "arr",
    },
    "is_point_in_surface": {
        "Object": "str",
        "Point": "arr",
    },
    "is_point_on_surface": {
        "Object": "str",
        "Point": "arr",
    },
    "rebuild_surface": {
        "Object": "str",
        "Degree": "arr",
        "PointCount": "arr",
    },
    "short_path": {
        "Surface": "str",
        "Start": "arr",
        "End": "arr",
    },
    "surface_closest_point": {
        "Object": "str",
        "Point": "arr",
    },
    "surface_contour_points": {
        "Object": "str",
        "StartPoint": "arr",
        "EndPoint": "arr",
        "Interval": "dbl",
        "Angle": "dbl",
    },
    "surface_curvature": {
        "Object": "str",
        "Parameter": "arr",
    },
    "surface_evaluate": {
        "Object": "str",
        "Parameter": "arr",
        "Derivative": "int",
    },
    "surface_frame": {
        "Object": "str",
        "Parameter": "arr",
    },
    "surface_normal": {
        "Object": "str",
        "Parameter": "arr",
    },
    "surface_principal_curvature": {
        "Object": "str",
        "Point": "arr",
    },
},
"transformation": {
    "is_xform_identity": {
        "Xform": "arr",
    },
    "is_xform_similarity": {
        "Xform": "arr",
    },
    "is_xform_zero": {
        "Xform": "arr",
    },
    "xform_c_plane_to_world": {
        "Point": "arr",
        "Plane": "arr",
    },
    "xform_change_basis": {
        "Plane1": "arr",
        "Plane2": "arr",
        "X0": "arr",
        "Y0": "arr",
        "Z0": "arr",
        "X1": "arr",
        "Y1": "arr",
        "Z1": "arr",
    },
    "xform_compare": {
        "Xform1": "arr",
        "Xform2": "arr",
    },
    "xform_determinant": {
        "Xform": "arr",
    },
    "xform_inverse": {
        "Xform": "arr",
    },
    "xform_mirror": {
        "Point": "arr",
        "Normal": "arr",
    },
    "xform_multiply": {
        "Xform1": "arr",
        "Xform2": "arr",
    },
    "xform_planar_projection": {
        "Plane": "arr",
    },
    "xform_rotation": {
        "Plane1": "arr",
        "Plane2": "arr",
        "Angle": "dbl",
        "Axis": "arr",
        "StartDir": "arr",
        "EndDir": "arr",
        "Point": "arr",
        "X0": "arr",
        "Y0": "arr",
        "Z0": "arr",
        "X1": "arr",
        "Y1": "arr",
        "Z1": "arr",
    },
    "xform_scale": {
        "Plane": "arr",
        "XScale": "dbl",
        "YScale": "dbl",
        "ZScale": "dbl",
        "Vector": "arr",
        "Point": "arr",
        "Scale": "dbl",
    },
    "xform_screen_to_world": {
        "Point": "arr",
        "View": "str",
        "Convert": "bln",
    },
    "xform_shear": {
        "Plane": "arr",
        "X1": "arr",
        "Y1": "arr",
        "Z1": "arr",
    },
    "xform_translation": {
        "Vector": "arr",
    },
    "xform_world_to_c_plane": {
        "Point": "arr",
        "Plane": "arr",
    },
    "xform_world_to_screen": {
        "Point": "arr",
        "View": "str",
        "Convert": "bln",
    },
},
"user_data": {
},
"user_interface": {
    "check_list_box": {
        "Items": "arr",
        "Values": "arr",
        "Message": "str",
        "Title": "str",
    },
    "combo_list_box": {
        "Items": "arr",
        "Message": "str",
        "Title": "str",
    },
    "get_angle": {
        "Point": "arr",
        "Reference": "arr",
        "Angle": "dbl",
        "Message": "str",
    },
    "get_boolean": {
        "Message": "str",
        "Items": "arr",
        "Defaults": "arr",
    },
    "get_box": {
        "Mode": "int",
        "Point": "arr",
        "Prompt1": "str",
        "Prompt2": "str",
        "Prompt3": "str",
    },
    "get_distance": {
        "Point": "arr",
        "Distance": "dbl",
        "Message1": "str",
        "Message2": "str",
    },
    "get_point": {
        "Message": "str",
        "Point": "arr",
        "Distance": "dbl",
        "Plane": "bln",
    },
    "get_point_on_line": {
        "Message": "str",
        "Start": "arr",
        "End": "arr",
        "Track": "bln",
    },
    "get_point_on_plane": {
        "Message": "str",
        "Plane": "arr",
        "Point": "arr",
    },
    "get_points": {
        "Draw": "bln",
        "Plane": "bln",
        "Message1": "str",
        "Message2": "str",
        "MaxPoints": "int",
        "BasePoint": "arr",
    },
    "get_rectangle": {
        "Mode": "int",
        "Point": "arr",
        "Prompt1": "str",
        "Prompt2": "str",
        "Prompt3": "str",
    },
    "get_string": {
        "Message": "str",
        "String": "str",
        "Strings": "arr",
    },
    "list_box": {
        "Items": "arr",
        "Message": "str",
        "Title": "str",
    },
    "multi_list_box": {
        "Items": "arr",
        "Message": "str",
        "Title": "str",
    },
    "popup_menu": {
        "Items": "arr",
        "Modes": "arr",
        "Point": "arr",
        "View": "str",
    },
    "property_list_box": {
        "Items": "arr",
        "Values": "arr",
        "Message": "str",
        "Title": "str",
    },
},
"utility": {
    "cull_duplicate_numbers": {
        "Numbers": "arr",
        "Tolerance": "dbl",
    },
    "cull_duplicate_points": {
        "Points": "arr",
        "Tolerance": "dbl",
    },
    "cull_duplicate_strings": {
        "Strings": "arr",
        "CaseSensitive": "bln",
    },
    "join_arrays": {
        "1": "arr",
        "2": "arr",
    },
    "pt2_str": {
        "Point": "arr",
        "Precision": "n",
        "Space": "bln",
    },
    "simplify_array": {
        "Points": "arr",
    },
    "sort_numbers": {
        "Numbers": "arr",
        "Ascending": "bln",
    },
    "sort_point_list": {
        "Points": "arr",
        "Tolerance": "dbl",
    },
    "sort_points": {
        "Points": "arr",
        "Ascending": "bln",
        "Order": "bln",
    },
    "sort_strings": {
        "Strings": "arr",
        "Ascending": "bln",
        "NoCase": "bln",
    },
},
"view": {
    "background_bitmap": {
        "View": "str",
        "Point": "arr",
        "Width": "dbl",
    },
    "view_c_plane": {
        "View": "str",
        "Plane": "arr",
    },
    "view_camera": {
        "View": "str",
        "Camera": "arr",
    },
    "view_camera_target": {
        "View": "str",
        "Camera": "arr",
        "Target": "arr",
    },
    "view_camera_up": {
        "View": "str",
        "UpVector": "arr",
    },
    "view_target": {
        "View": "str",
        "Target": "arr",
    },
    "zoom_bounding_box": {
        "Corners": "arr",
        "View": "str",
        "All": "bln",
    },
},
