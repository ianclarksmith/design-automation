#Replace in the ??? with either "bln", "int", "dbl", or "str"

application = {
    "status_bar_point": {
        "point": "arr_of_dbl",
    },
},
block = {
    "insert_block": {
        "name": "str",
        "point": "arr_of_dbl",
        "scale": "arr_of_int",
        "angle": "dbl",
        "normal": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
},
curve = {
    "add_arc": {
        "plane": "arr_of_dbl",
        "radius": "dbl",
        "angle": "dbl",
    },
    "add_arc3_pt": {
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "add_circle": {
        "plane": "arr_of_dbl",
        "radius": "dbl",
    },
    "add_circle3_pt": {
        "first": "arr_of_dbl",
        "second": "arr_of_dbl",
        "third": "arr_of_dbl",
    },
    "add_curve": {
        "points": "arr_of_dbl",
        "degree": "int",
    },
    "add_ellipse": {
        "plane": "arr_of_dbl",
        "x_radius": "dbl",
        "y_radius": "dbl",
    },
    "add_ellipse3_pt": {
        "center": "arr_of_dbl",
        "second": "arr_of_dbl",
        "third": "arr_of_dbl",
    },
    "add_fillet_curve": {
        "curve0": "str",
        "curve1": "str",
        "radius": "dbl",
        "point0": "arr_of_dbl",
        "point1": "arr_of_dbl",
    },
    "add_interp_crv_on_srf": {
        "object": "str",
        "points": "arr_of_dbl",
    },
    "add_interp_crv_on_srf_u_v": {
        "object": "str",
        "points": "arr_of_dbl",
    },
    "add_interp_curve": {
        "points": "arr_of_dbl",
        "degree": "int",
        "knot_style": "int",
        "start_tan": "arr_of_dbl",
        "end_tan": "arr_of_dbl",
    },
    "add_interp_curve_ex": {
        "points": "arr_of_dbl",
        "degree": "int",
        "knot_style": "int",
        "sharp": "bln",
        "start_tangent": "arr_of_dbl",
        "end_tangent": "arr_of_dbl",
    },
    "add_line": {
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
    },
    "add_nurbs_curve": {
        "points": "arr_of_dbl",
        "knots": "arr_of_int",
        "degree": "int",
        "weights": "arr_of_int",
    },
    "add_polyline": {
        "points": "arr_of_dbl",
    },
    "curve_area": {
        "objects": "arr_of_str",
    },
    "curve_area_centroid": {
        "objects": "arr_of_str",
    },
    "curve_boolean_union": {
        "curves": "arr_of_str",
    },
    "curve_closest_object": {
        "curve": "str",
        "objects": "arr_of_str",
    },
    "curve_closest_point": {
        "object": "str",
        "point": "arr_of_dbl",
        "index": "int",
    },
    "curve_contour_points": {
        "object": "str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "interval": "dbl",
    },
    "curve_fillet_points": {
        "curve0": "str",
        "curve1": "str",
        "radius": "dbl",
        "base_point0": "arr_of_dbl",
        "base_point1": "arr_of_dbl",
    },
    "curve_length": {
        "object": "str",
        "index": "int",
        "sub_domain": "arr_of_int",
    },
    "curve_radius": {
        "object": "str",
        "point": "arr_of_dbl",
        "index": "int",
    },
    "explode_curves": {
        "objects": "arr_of_str",
        "delete": "bln",
    },
    "extend_curve": {
        "object": "str",
        "type": "int",
        "side": "int",
        "objects": "arr_of_str",
    },
    "extend_curve_point": {
        "object": "str",
        "side": "int",
        "point": "arr_of_dbl",
    },
    "is_curve_in_plane": {
        "object": "str",
        "plane": "arr_of_dbl",
    },
    "is_point_on_curve": {
        "object": "str",
        "point": "arr_of_int",
        "index": "int",
    },
    "offset_curve": {
        "object": "str",
        "direction": "arr_of_dbl",
        "distance": "dbl",
        "normal": "arr_of_dbl",
        "style": "int",
    },
    "offset_curve_on_surface": {
        "curve": "str",
        "surface": "str",
        "distance": "dbl",
        "parameter": "arr_of_dbl",
    },
    "planar_closed_curve_containment": {
        "curve1": "str",
        "curve2": "str",
        "plane": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "planar_curve_collision": {
        "curve1": "str",
        "curve2": "str",
        "plane": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "point_in_planar_closed_curve": {
        "point": "arr_of_dbl",
        "curve": "str",
        "plane": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "project_curve_to_mesh": {
        "curves": "arr_of_str",
        "meshes": "arr_of_str",
        "direction": "arr_of_dbl",
    },
    "project_curve_to_surface": {
        "curves": "arr_of_str",
        "surfaces": "arr_of_str",
        "direction": "arr_of_dbl",
    },
    "split_curve": {
        "object": "str",
        "parameters": "arr_of_dbl",
        "delete": "bln",
    },
    "trim_curve": {
        "object": "str",
        "interval": "arr_of_int",
        "delete": "bln",
    },
},
dimension = {
    "add_leader": {
        "points": "arr_of_dbl",
        "view": "str",
        "text": "str",
    },
},
document = {
    "create_preview_image": {
        "file": "str",
        "view": "str",
        "size": "arr_of_int",
        "flags": "int",
        "wireframe": "bln",
    },
    "render_resolution": {
        "resolution": "arr_of_int",
    },
},
geometry = {
    "add_clipping_plane": {
        "plane": "arr_of_dbl",
        "d_u": "dbl",
        "d_v": "dbl",
        "views": "arr_of_str",
    },
    "add_point_cloud": {
        "points": "arr_of_dbl",
    },
    "add_points": {
        "points": "arr_of_dbl",
    },
    "add_text": {
        "text": "str",
        "point": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "height": "dbl",
        "font": "str",
        "style": "int",
    },
    "add_text_dot": {
        "test": "str",
        "point": "arr_of_dbl",
    },
    "bounding_box": {
        "objects": "arr_of_str",
        "view": "str",
        "world_coords": "bln",
    },
    "point_coordinates": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "text_dot_point": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "text_object_plane": {
        "object": "str",
        "plane": "arr_of_dbl",
    },
    "text_object_point": {
        "object": "str",
        "point": "arr_of_dbl",
    },
},
group = {
    "add_objects_to_group": {
        "objects": "arr_of_str",
        "group": "str",
    },
    "remove_objects_from_group": {
        "objects": "arr_of_str",
        "group": "str",
    },
},
hatch = {
    "add_hatches": {
        "curves": "arr_of_str",
        "hatch": "str",
        "scale": "dbl",
        "rotation": "dbl",
    },
},
layer = {
},
light = {
    "add_directional_light": {
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
    },
    "add_linear_light": {
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "width": "dbl",
    },
    "add_point_light": {
        "point": "arr_of_dbl",
    },
    "add_rectangular_light": {
        "origin": "arr_of_dbl",
        "width": "arr_of_dbl",
        "height": "arr_of_dbl",
    },
    "add_spot_light": {
        "origin": "arr_of_dbl",
        "radius": "dbl",
        "apex": "arr_of_dbl",
    },
    "light_direction": {
        "object": "str",
        "direction": "arr_of_dbl",
    },
    "light_location": {
        "object": "str",
        "location": "arr_of_dbl",
    },
},
line_and_plane = {
    "distance_to_plane": {
        "plane": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "evaluate_plane": {
        "plane": "arr_of_dbl",
        "parameter": "arr_of_dbl",
    },
    "intersect_planes": {
        "plane1": "arr_of_dbl",
        "plane2": "arr_of_dbl",
        "plane3": "arr_of_dbl",
    },
    "line_closest_point": {
        "line": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "line_is_farther_than": {
        "line": "arr_of_dbl",
        "distance": "dbl",
        "point": "arr_of_dbl",
        "line2": "arr_of_dbl",
    },
    "line_line_intersection": {
        "line_a": "arr_of_dbl",
        "line_b": "arr_of_dbl",
        "planar": "bln",
    },
    "line_max_distance_to": {
        "line": "arr_of_dbl",
        "point": "arr_of_dbl",
        "line2": "arr_of_dbl",
    },
    "line_min_distance_to": {
        "line": "arr_of_dbl",
        "point": "arr_of_dbl",
        "line2": "arr_of_dbl",
    },
    "line_plane": {
        "line": "arr_of_dbl",
    },
    "line_plane_intersection": {
        "line": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "line_transform": {
        "line": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
    "move_plane": {
        "plane": "arr_of_dbl",
        "origin": "arr_of_dbl",
    },
    "plane_closest_point": {
        "plane": "arr_of_dbl",
        "point": "arr_of_dbl",
        "return_point": "bln",
    },
    "plane_equation": {
        "plane": "arr_of_dbl",
    },
    "plane_fit_from_points": {
        "points": "arr_of_dbl",
    },
    "plane_from_frame": {
        "origin": "arr_of_dbl",
        "xaxis": "arr_of_dbl",
        "yaxis": "arr_of_dbl",
    },
    "plane_from_normal": {
        "origin": "arr_of_dbl",
        "normal": "arr_of_dbl",
    },
    "plane_from_points": {
        "origin": "arr_of_dbl",
        "point_x": "arr_of_dbl",
        "point_y": "arr_of_dbl",
    },
    "plane_plane_intersection": {
        "plane1": "arr_of_dbl",
        "point2": "arr_of_dbl",
    },
    "plane_transform": {
        "plane": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
    "rotate_plane": {
        "plane": "arr_of_dbl",
        "angle": "dbl",
        "axis": "arr_of_dbl",
    },
},
linetype = {
},
material = {
    "match_material": {
        "src_material_index": "int",
        "src_object": "str",
        "dest_objects": "arr_of_str",
    },
},
math = {
    "angle": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
        "world": "bln",
    },
    "angle2": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
    },
    "deviation": {
        "numbers": "arr_of_int",
    },
    "distance": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
        "point_array": "arr_of_dbl",
    },
    "max": {
        "numbers": "arr_of_int",
    },
    "mean": {
        "numbers": "arr_of_int",
    },
    "median": {
        "numbers": "arr_of_int",
    },
    "min": {
        "numbers": "arr_of_int",
    },
    "polar": {
        "point": "arr_of_dbl",
        "angle": "dbl",
        "distance": "dbl",
        "plane": "arr_of_dbl",
    },
},
mesh = {
    "add_mesh": {
        "vertices": "arr_of_dbl",
        "face_vertices": "arr_of_int",
        "vertex_normals": "arr_of_dbl",
        "texture_coordinates": "arr_of_dbl",
        "vertex_colors": "arr_of_int",
    },
    "explode_meshes": {
        "objects": "arr_of_str",
        "delete": "bln",
    },
    "mesh_area": {
        "objects": "arr_of_str",
    },
    "mesh_boolean_difference": {
        "input0": "arr_of_str",
        "input1": "arr_of_str",
        "delete": "bln",
    },
    "mesh_boolean_intersection": {
        "input0": "arr_of_str",
        "input1": "arr_of_str",
        "delete": "bln",
    },
    "mesh_boolean_split": {
        "input0": "arr_of_str",
        "input1": "arr_of_str",
        "delete": "bln",
    },
    "mesh_boolean_union": {
        "input": "arr_of_str",
        "delete": "bln",
    },
    "mesh_closest_point": {
        "object": "str",
        "point": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "mesh_contour_points": {
        "object": "str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "interval": "dbl",
        "remove_coincident_points": "bln",
    },
    "mesh_vertex_colors": {
        "object": "str",
        "vertex_colors": "arr_of_int",
    },
    "mesh_volume": {
        "objects": "arr_of_str",
    },
},
object = {
    "box_morph_object": {
        "objects": "arr_of_str",
        "box_points": "arr_of_dbl",
        "copy": "bln",
    },
    "copy_objects": {
        "objects": "arr_of_str",
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
        "translation": "arr_of_dbl",
    },
    "delete_objects": {
        "objects": "arr_of_str",
    },
    "enable_object_mesh": {
        "objects": "arr_of_str",
        "enable": "bln",
    },
    "flash_object": {
        "objects": "arr_of_str",
        "style": "bln",
    },
    "hide_objects": {
        "objects": "arr_of_str",
    },
    "is_object_in_box": {
        "object": "str",
        "box": "arr_of_dbl",
        "mode": "bln",
    },
    "lock_objects": {
        "objects": "arr_of_str",
    },
    "match_object_attributes": {
        "targets": "arr_of_str",
        "source": "str",
    },
    "mirror_objects": {
        "objects": "arr_of_str",
        "start_pt": "arr_of_dbl",
        "end_pt": "arr_of_dbl",
        "copy": "bln",
    },
    "move_objects": {
        "objects": "arr_of_str",
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
        "translation": "arr_of_dbl",
    },
    "object_color": {
        "objects": "arr_of_str",
        "color": "lng",
    },
    "object_color_source": {
        "objects": "arr_of_str",
        "source": "int",
    },
    "object_layer": {
        "objects": "arr_of_str",
        "layer": "str",
    },
    "object_linetype": {
        "objects": "arr_of_str",
        "layer": "str",
    },
    "object_linetype_source": {
        "objects": "arr_of_str",
        "source": "int",
    },
    "object_material_source": {
        "objects": "arr_of_str",
        "source": "int",
    },
    "object_names": {
        "objects": "arr_of_str",
        "names": "arr_of_str",
    },
    "object_print_color": {
        "objects": "arr_of_str",
        "color": "lng",
    },
    "object_print_color_source": {
        "objects": "arr_of_str",
        "source": "int",
    },
    "object_print_width": {
        "objects": "arr_of_str",
        "width": "dbl",
    },
    "object_print_width_source": {
        "objects": "arr_of_str",
        "source": "int",
    },
    "object_u_r_l": {
        "objects": "arr_of_str",
        "u_r_l": "str",
    },
    "orient_objects": {
        "objects": "arr_of_str",
        "reference": "arr_of_dbl",
        "target": "arr_of_dbl",
        "flags": "int",
    },
    "remap_objects": {
        "object": "arr_of_str",
        "src_plane": "arr_of_dbl",
        "dst_plane": "arr_of_dbl",
        "copy": "bln",
    },
    "rotate_objects": {
        "objects": "arr_of_str",
        "point": "arr_of_dbl",
        "angle": "dbl",
        "axis": "arr_of_dbl",
        "copy": "bln",
    },
    "scale_objects": {
        "objects": "arr_of_str",
        "origin": "arr_of_dbl",
        "scale": "arr_of_dbl",
        "copy": "bln",
    },
    "select_objects": {
        "objects": "arr_of_str",
    },
    "shear_objects": {
        "objects": "arr_of_str",
        "origin": "arr_of_dbl",
        "ref_pt": "arr_of_dbl",
        "scale": "arr_of_int",
        "copy": "bln",
    },
    "show_objects": {
        "objects": "arr_of_str",
    },
    "transform_objects": {
        "objects": "arr_of_str",
        "matrix": "arr_of_str",
        "copy": "bln",
    },
    "unlock_objects": {
        "objects": "arr_of_str",
    },
    "unselect_objects": {
        "objects": "arr_of_str",
    },
},
object_grip = {
    "object_grip_locations": {
        "object": "str",
        "points": "arr_of_dbl",
    },
},
point_and_vector = {
    "is_vector_parallel_to": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "is_vector_perpendicular_to": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "is_vector_tiny": {
        "vector": "arr_of_dbl",
    },
    "is_vector_zero": {
        "vector": "arr_of_dbl",
    },
    "point_add": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
    },
    "point_array_bounding_box": {
        "points": "arr_of_dbl",
        "view": "str",
        "world_coords": "bln",
    },
    "point_array_closest_point": {
        "points": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "point_array_transform": {
        "points": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
    "point_compare": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "point_divide": {
        "point": "arr_of_dbl",
        "scale": "dbl",
    },
    "point_scale": {
        "point": "arr_of_dbl",
        "scale": "dbl",
    },
    "point_subtract": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
    },
    "point_transform": {
        "point": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
    "points_are_coplanar": {
        "points": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "project_point_to_mesh": {
        "points": "arr_of_dbl",
        "meshes": "arr_of_str",
        "direction": "arr_of_dbl",
    },
    "project_point_to_surface": {
        "points": "arr_of_dbl",
        "surfaces": "arr_of_str",
        "direction": "arr_of_dbl",
    },
    "pull_points": {
        "object": "str",
        "points": "arr_of_dbl",
    },
    "vector_add": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_compare": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_create": {
        "point1": "arr_of_dbl",
        "point2": "arr_of_dbl",
    },
    "vector_cross_product": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_divide": {
        "vector": "arr_of_dbl",
        "divide": "dbl",
    },
    "vector_dot_product": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_length": {
        "vector": "arr_of_dbl",
    },
    "vector_multiply": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_reverse": {
        "vector": "arr_of_dbl",
    },
    "vector_rotate": {
        "vector": "arr_of_dbl",
        "angle": "dbl",
        "axis": "arr_of_dbl",
    },
    "vector_scale": {
        "vector": "arr_of_dbl",
        "scale": "dbl",
    },
    "vector_subtract": {
        "vector1": "arr_of_dbl",
        "vector2": "arr_of_dbl",
    },
    "vector_transform": {
        "vector": "arr_of_dbl",
        "xform": "arr_of_dbl",
    },
    "vector_unitize": {
        "vector": "arr_of_dbl",
    },
},
selection = {
    "get_object_ex": {
        "message": "str",
        "type": "int",
        "pre_select": "bln",
        "select": "bln",
        "objects": "arr_of_str",
    },
    "get_objects": {
        "message": "str",
        "type": "int",
        "group": "bln",
        "pre_select": "bln",
        "select": "bln",
        "objects": "arr_of_str",
    },
    "get_objects_ex": {
        "message": "str",
        "type": "int",
        "group": "bln",
        "pre_select": "bln",
        "select": "bln",
        "objects": "arr_of_str",
    },
},
surface_and_polysurface = {
    "add_box": {
        "corners": "arr_of_dbl",
    },
    "add_cone": {
        "base": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "height": "arr_of_dbl",
        "height": "dbl",
        "radius": "dbl",
        "cap": "bln",
    },
    "add_cut_plane": {
        "objects": "arr_of_str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "normal": "arr_of_dbl",
    },
    "add_cylinder": {
        "base": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "height": "arr_of_dbl",
        "height": "dbl",
        "radius": "dbl",
        "cap": "bln",
    },
    "add_edge_srf": {
        "objects": "arr_of_str",
    },
    "add_loft_srf": {
        "objects": "arr_of_str",
        "start_pt": "arr_of_dbl",
        "end_pt": "arr_of_dbl",
        "type": "int",
        "style": "int",
        "value": "n",
        "closed": "bln",
    },
    "add_nurbs_surface": {
        "point_count": "arr_of_int",
        "points": "arr_of_dbl",
        "knots_u": "arr_of_int",
        "knots_v": "arr_of_int",
        "degree": "arr_of_int",
        "weights": "arr_of_int",
    },
    "add_planar_srf": {
        "objects": "arr_of_str",
    },
    "add_plane_surface": {
        "plane": "arr_of_dbl",
        "d_u": "dbl",
        "d_v": "dbl",
    },
    "add_rail_rev_srf": {
        "profile": "str",
        "rail": "str",
        "axis": "arr_of_dbl",
    },
    "add_rev_srf": {
        "profile": "str",
        "axis": "arr_of_dbl",
        "start_angle": "dbl",
        "end_angle": "dbl",
    },
    "add_sphere": {
        "center": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "radius": "dbl",
    },
    "add_srf_contour_crvs": {
        "object": "str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "interval": "dbl",
    },
    "add_srf_control_pt_grid": {
        "count": "arr_of_int",
        "points": "arr_of_dbl",
        "degree": "arr_of_dbl",
    },
    "add_srf_pt": {
        "points": "arr_of_dbl",
    },
    "add_srf_pt_grid": {
        "count": "arr_of_int",
        "points": "arr_of_dbl",
        "degree": "arr_of_int",
        "closed": "arr_of_bln",
    },
    "add_srf_section_crvs": {
        "object": "str",
        "plane": "arr_of_dbl",
    },
    "add_sweep1": {
        "rail": "str",
        "shapes": "arr_of_str",
        "start_pt": "arr_of_dbl",
        "end_pt": "arr_of_dbl",
        "closed": "bln",
        "style": "int",
        "style_arg": "va",
        "simplify": "int",
        "simplify_arg": "va",
    },
    "add_sweep2": {
        "rails": "arr_of_str",
        "shapes": "arr_of_str",
        "start_pt": "arr_of_dbl",
        "end_pt": "arr_of_dbl",
        "closed": "bln",
        "simple_sweep": "bln",
        "maintain_height": "bln",
        "simplify": "int",
        "simplify_arg": "va",
    },
    "add_torus": {
        "base": "arr_of_dbl",
        "plane": "arr_of_dbl",
        "major_radius": "dbl",
        "minor_radius": "dbl",
        "direction": "arr_of_dbl",
    },
    "boolean_difference": {
        "input0": "arr_of_str",
        "input1": "arr_of_str",
        "delete": "bln",
    },
    "boolean_intersection": {
        "input0": "arr_of_str",
        "input1": "arr_of_str",
        "delete": "bln",
    },
    "boolean_union": {
        "input": "arr_of_str",
        "delete": "bln",
    },
    "brep_closest_point": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "evaluate_surface": {
        "object": "str",
        "parameter": "arr_of_dbl",
    },
    "explode_polysurfaces": {
        "objects": "arr_of_str",
        "delete": "bln",
    },
    "extract_iso_curve": {
        "object": "str",
        "parameter": "arr_of_dbl",
        "dir": "int",
    },
    "extrude_curve_point": {
        "curve": "str",
        "point": "arr_of_dbl",
    },
    "extrude_curve_straight": {
        "curve": "str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
    },
    "extrude_curve_tapered": {
        "curve": "str",
        "distance": "dbl",
        "direction": "arr_of_dbl",
        "base_point": "arr_of_dbl",
        "angle": "dbl",
        "corner_type": "int",
    },
    "fit_surface": {
        "object": "str",
        "degree": "arr_of_int",
        "tolerance": "dbl",
    },
    "is_parameter_on_surface": {
        "object": "str",
        "parameter": "arr_of_dbl",
    },
    "is_point_in_surface": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "is_point_on_surface": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "rebuild_surface": {
        "object": "str",
        "degree": "arr_of_int",
        "point_count": "arr_of_int",
    },
    "short_path": {
        "surface": "str",
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
    },
    "surface_closest_point": {
        "object": "str",
        "point": "arr_of_dbl",
    },
    "surface_contour_points": {
        "object": "str",
        "start_point": "arr_of_dbl",
        "end_point": "arr_of_dbl",
        "interval": "dbl",
        "angle": "dbl",
    },
    "surface_curvature": {
        "object": "str",
        "parameter": "arr_of_dbl",
    },
    "surface_evaluate": {
        "object": "str",
        "parameter": "arr_of_dbl",
        "derivative": "int",
    },
    "surface_frame": {
        "object": "str",
        "parameter": "arr_of_dbl",
    },
    "surface_normal": {
        "object": "str",
        "parameter": "arr_of_dbl",
    },
    "surface_principal_curvature": {
        "object": "str",
        "point": "arr_of_dbl",
    },
},
transformation = {
    "is_xform_identity": {
        "xform": "arr_of_dbl",
    },
    "is_xform_similarity": {
        "xform": "arr_of_dbl",
    },
    "is_xform_zero": {
        "xform": "arr_of_dbl",
    },
    "xform_c_plane_to_world": {
        "point": "arr_of_dbl",
        "plane": "arr_of_dbl",
    },
    "xform_change_basis": {
        "plane1": "arr_of_dbl",
        "plane2": "arr_of_dbl",
        "x0": "arr_of_dbl",
        "y0": "arr_of_dbl",
        "z0": "arr_of_dbl",
        "x1": "arr_of_dbl",
        "y1": "arr_of_dbl",
        "z1": "arr_of_dbl",
    },
    "xform_compare": {
        "xform1": "arr_of_dbl",
        "xform2": "arr_of_dbl",
    },
    "xform_determinant": {
        "xform": "arr_of_dbl",
    },
    "xform_inverse": {
        "xform": "arr_of_dbl",
    },
    "xform_mirror": {
        "point": "arr_of_dbl",
        "normal": "arr_of_dbl",
    },
    "xform_multiply": {
        "xform1": "arr_of_dbl",
        "xform2": "arr_of_dbl",
    },
    "xform_planar_projection": {
        "plane": "arr_of_dbl",
    },
    "xform_rotation": {
        "plane1": "arr_of_dbl",
        "plane2": "arr_of_dbl",
        "angle": "dbl",
        "axis": "arr_of_dbl",
        "start_dir": "arr_of_dbl",
        "end_dir": "arr_of_dbl",
        "point": "arr_of_dbl",
        "x0": "arr_of_dbl",
        "y0": "arr_of_dbl",
        "z0": "arr_of_dbl",
        "x1": "arr_of_dbl",
        "y1": "arr_of_dbl",
        "z1": "arr_of_dbl",
    },
    "xform_scale": {
        "plane": "arr_of_dbl",
        "x_scale": "dbl",
        "y_scale": "dbl",
        "z_scale": "dbl",
        "vector": "arr_of_dbl",
        "point": "arr_of_dbl",
        "scale": "dbl",
    },
    "xform_screen_to_world": {
        "point": "arr_of_dbl",
        "view": "str",
        "convert": "bln",
    },
    "xform_shear": {
        "plane": "arr_of_dbl",
        "x1": "arr_of_dbl",
        "y1": "arr_of_dbl",
        "z1": "arr_of_dbl",
    },
    "xform_translation": {
        "vector": "arr_of_dbl",
    },
    "xform_world_to_c_plane": {
        "point": "arr_of_dbl",
        "plane": "arr_of_dbl",
    },
    "xform_world_to_screen": {
        "point": "arr_of_dbl",
        "view": "str",
        "convert": "bln",
    },
},
user_data = {
},
user_interface = {
    "check_list_box": {
        "items": "arr_of_str",
        "values": "arr_of_bln",
        "message": "str",
        "title": "str",
    },
    "combo_list_box": {
        "items": "arr_of_str",
        "message": "str",
        "title": "str",
    },
    "get_angle": {
        "point": "arr_of_dbl",
        "reference": "arr_of_dbl",
        "angle": "dbl",
        "message": "str",
    },
    "get_boolean": {
        "message": "str",
        "items": "arr_of_str",
        "defaults": "arr_of_bln",
    },
    "get_box": {
        "mode": "int",
        "point": "arr_of_dbl",
        "prompt1": "str",
        "prompt2": "str",
        "prompt3": "str",
    },
    "get_distance": {
        "point": "arr_of_dbl",
        "distance": "dbl",
        "message1": "str",
        "message2": "str",
    },
    "get_point_on_line": {
        "message": "str",
        "start": "arr_of_dbl",
        "end": "arr_of_dbl",
        "track": "bln",
    },
    "get_point_on_plane": {
        "message": "str",
        "plane": "arr_of_dbl",
        "point": "arr_of_dbl",
    },
    "get_points": {
        "draw": "bln",
        "plane": "bln",
        "message1": "str",
        "message2": "str",
        "max_points": "int",
        "base_point": "arr_of_dbl",
    },
    "get_rectangle": {
        "mode": "int",
        "point": "arr_of_dbl",
        "prompt1": "str",
        "prompt2": "str",
        "prompt3": "str",
    },
    "get_string": {
        "message": "str",
        "string": "str",
        "strings": "arr_of_str",
    },
    "list_box": {
        "items": "arr_of_str",
        "message": "str",
        "title": "str",
    },
    "multi_list_box": {
        "items": "arr_of_str",
        "message": "str",
        "title": "str",
    },
    "popup_menu": {
        "items": "arr_of_str",
        "modes": "arr_of_int",
        "point": "arr_of_dbl",
        "view": "str",
    },
    "property_list_box": {
        "items": "arr_of_str",
        "values": "arr_of_str",
        "message": "str",
        "title": "str",
    },
},
utility = {
    "cull_duplicate_numbers": {
        "numbers": "arr_of_int",
        "tolerance": "dbl",
    },
    "cull_duplicate_points": {
        "points": "arr_of_dbl",
        "tolerance": "dbl",
    },
    "cull_duplicate_strings": {
        "strings": "arr_of_int",
        "case_sensitive": "bln",
    },
    "pt2_str": {
        "point": "arr_of_dbl",
        "precision": "n",
        "space": "bln",
    },
    "simplify_array": {
        "points": "arr_of_dbl",
    },
},
view = {
    "background_bitmap": {
        "view": "str",
        "file_name": "str",
        "point": "arr_of_dbl",
        "width": "dbl",
    },
    "view_c_plane": {
        "view": "str",
        "plane": "arr_of_dbl",
    },
    "view_camera": {
        "view": "str",
        "camera": "arr_of_dbl",
    },
    "view_camera_target": {
        "view": "str",
        "camera": "arr_of_dbl",
        "target": "arr_of_dbl",
    },
    "view_camera_up": {
        "view": "str",
        "up_vector": "arr_of_dbl",
    },
    "view_target": {
        "view": "str",
        "target": "arr_of_dbl",
    },
    "zoom_bounding_box": {
        "corners": "arr_of_dbl",
        "view": "str",
        "all": "bln",
    },
},
