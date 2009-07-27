#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

add_mesh = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "add_mesh",
    "method_parameters": (("vertices","arr_of_dbl","REQ"),("face_vertices","arr_of_int","REQ"),("vertex_normals","arr_of_dbl","OPT"),("texture_coordinates","arr_of_dbl","OPT"),("vertex_colors","arr_of_int","OPT")),
    "method_returns": (""string"",""null"")
    }
add_planar_mesh = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "add_planar_mesh",
    "method_parameters": (("object","str","REQ"),("delete","bln","REQ")),
    "method_returns": (""string"",""null"")
    }
curve_mesh_intersection = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "curve_mesh_intersection",
    "method_parameters": (("curve","str","REQ"),("mesh","str","REQ"),("return_faces","bln","OPT")),
    "method_returns": (""array"",""array"",""array"",""number"",""null"")
    }
disjoint_mesh_count = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "disjoint_mesh_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
duplicate_mesh_border = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "duplicate_mesh_border",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
explode_meshes = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "explode_meshes",
    "method_parameters": (("objects","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
is_mesh = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "is_mesh",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
is_mesh_closed = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "is_mesh_closed",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
is_mesh_manifold = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "is_mesh_manifold",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_area = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_area",
    "method_parameters": (("objects","arr_of_str","REQ")),
    "method_returns": (""array"",""number"",""number"",""number"",""null"")
    }
mesh_area_centroid = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_area_centroid",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_boolean_difference = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_difference",
    "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_boolean_intersection = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_intersection",
    "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_boolean_split = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_split",
    "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_boolean_union = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_union",
    "method_parameters": (("input","arr_of_str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_closest_point = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_closest_point",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
    "method_returns": (""array"",""array"",""number"",""null"")
    }
mesh_contour_points = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_contour_points",
    "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("interval","dbl","OPT"),("remove_coincident_points","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_face_centers = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_face_centers",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_face_count = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_face_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
mesh_face_normals = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_face_normals",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_face_vertices = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_face_vertices",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_faces = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_faces",
    "method_parameters": (("object","str","REQ"),("face_type","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_has_face_normals = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_has_face_normals",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_has_texture_coordinates = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_has_texture_coordinates",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_has_vertex_colors = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_has_vertex_colors",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_has_vertex_normals = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_has_vertex_normals",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_mesh_intersection = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_mesh_intersection",
    "method_parameters": (("mesh1","str","REQ"),("mesh2","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": (""array"",""null"")
    }
mesh_naked_edge_points = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_naked_edge_points",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_offset = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_offset",
    "method_parameters": (("mesh","str","REQ"),("distance","dbl","REQ")),
    "method_returns": (""string"",""null"")
    }
mesh_quad_count = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_quad_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
mesh_quads_to_triangles = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_quads_to_triangles",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
mesh_texture_coordinates = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_texture_coordinates",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_triangle_count = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_triangle_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
mesh_vertex_colors = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_colors",
    "method_parameters": (("object","str","REQ"),("vertex_colors","arr_of_int","OPT")),
    "method_returns": (""array"",""array"",""null"")
    }
mesh_vertex_count = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
mesh_vertex_normals = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_normals",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_vertices = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_vertices",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
mesh_volume = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_volume",
    "method_parameters": (("objects","arr_of_str","REQ")),
    "method_returns": (""array"",""number"",""number"",""number"",""null"")
    }
mesh_volume_centroid = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "mesh_volume_centroid",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""array"",""null"")
    }
pull_curve_to_mesh = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "pull_curve_to_mesh",
    "method_parameters": (("mesh","str","REQ"),("curve","str","REQ")),
    "method_returns": (""string"",""null"")
    }
split_disjoint_mesh = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "split_disjoint_mesh",
    "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
unify_mesh_normals = {
    "method_location": "Mesh",
    "method_type": "METHOD",
    "method_name": "unify_mesh_normals",
    "method_parameters": (("object","str","REQ")),
    "method_returns": (""number"",""null"")
    }
