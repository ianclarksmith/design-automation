#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# Mesh
#===============================================================================
add_mesh = {#ed
    "method_location": "_Object._MeshType.Mesh",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("vertices","array of dbl","REQ"),("face_vertices","array of int","REQ"),("vertex_normals","array of dbl","OPT"),("texture_coordinates","array of dbl","OPT"),("vertex_colors","array of int","OPT")),
    "method_returns": ("_Object._MeshType.Mesh","null")
    }
#===============================================================================
# PlanarMesh
#===============================================================================

add_planar_mesh = {#ed
    "method_location": "_Object._MeshType.PlanarMesh",
    "method_type": "METHOD",
    "method_name": "add_planar_mesh",
    "method_parameters": (("","self","REQ"),("delete","bln","REQ")),
    "method_returns": ("_Object._MeshType.Mesh","null")
    }
#===============================================================================
# _Object
#===============================================================================
is_mesh = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_mesh",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_mesh_closed = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_mesh_closed",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_mesh_manifold = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_mesh_manifold",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
#===============================================================================
# _MeshType
#===============================================================================
mesh_offset = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "CONSTRUCTOR",
    "method_name": "mesh_offset",
    "method_parameters": (("","self","REQ"),("distance","dbl","REQ")),
    "method_returns": ("_Object._MeshType.Mesh","null")
    }
pull_curve_to_mesh = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "CONSTRUCTOR",
    "method_name": "pull_curve_to_mesh",
    "method_parameters": (("","self","REQ"),("curve","str","REQ")),
    "method_returns": ("_Object._MeshType.Mesh","null")
    }
curve_mesh_intersection = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "curve_mesh_intersection",
    "method_parameters": (("","self","REQ"),("mesh","str","REQ"),("return_faces","bln","OPT")),
    "method_returns": ("array of dbl","array of (array of dbl, int)","null")
    }
disjoint_mesh_count = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "disjoint_mesh_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
duplicate_mesh_border = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "duplicate_mesh_border",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of _Object._MeshType","null")
    }
explode_meshes = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "explode_meshes",
    "method_parameters": (("objects","array of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_area = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_area",
    "method_parameters": (("objects","array of str","REQ")),
    "method_returns": ("array of (int, int, int)","null")
    }
mesh_area_centroid = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_area_centroid",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_boolean_difference = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_difference",
    "method_parameters": (("input_0","array of str","REQ"),("input_1","array of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_boolean_intersection = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_intersection",
    "method_parameters": (("input_0","array of str","REQ"),("input_1","array of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_boolean_split = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_split",
    "method_parameters": (("input_0","array of str","REQ"),("input_1","array of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_boolean_union = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_boolean_union",
    "method_parameters": (("input","array of str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
mesh_closest_point = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_closest_point",
    "method_parameters": (("","self","REQ"),("point","array of dbl","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("array of(array of dbl,int)","null")
    }
mesh_contour_points = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_contour_points",
    "method_parameters": (("","self","REQ"),("start_point","array of dbl","REQ"),("end_point","array of dbl","REQ"),("interval","dbl","OPT"),("remove_coincident_points","bln","OPT")),
    "method_returns": ("array of dbl","null")
    }
mesh_face_centers = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_face_centers",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_face_count = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_face_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
mesh_face_normals = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_face_normals",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_face_vertices = {
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_face_vertices",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_faces = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_faces",
    "method_parameters": (("","self","REQ"),("face_type","bln","OPT")),
    "method_returns": ("array of dbl","null")
    }
mesh_has_face_normals = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_has_face_normals",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
mesh_has_texture_coordinates = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_has_texture_coordinates",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
mesh_has_vertex_colors = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_has_vertex_colors",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
mesh_has_vertex_normals = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_has_vertex_normals",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
mesh_mesh_intersection = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_mesh_intersection",
    "method_parameters": (("","self","REQ"),("mesh_1","str","REQ"),("tolerance","dbl","OPT")),
    "method_returns": ("array of dbl","null")
    }
mesh_naked_edge_points = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_naked_edge_points",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of bln","null")
    }
mesh_quad_count = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_quad_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
mesh_quads_to_triangles = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_quads_to_triangles",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
mesh_texture_coordinates = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_texture_coordinates",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_triangle_count = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_triangle_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
mesh_vertex_colors = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_colors",
    "method_parameters": (("","self","REQ"),("vertex_colors","array of int","OPT")),
    "method_returns": ("array of int","array of int","null")
    }
mesh_vertex_count = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
mesh_vertex_normals = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_vertex_normals",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_vertices = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_vertices",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
mesh_volume = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_volume",
    "method_parameters": (("objects","array of str","REQ")),
    "method_returns": ("array of (int,int,int)","null")
    }
mesh_volume_centroid = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "mesh_volume_centroid",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
split_disjoint_mesh = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "split_disjoint_mesh",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT")),
    "method_returns": ("array of _Object._MeshType","null")
    }
unify_mesh_normals = {#ed
    "method_location": "_Object._MeshType",
    "method_type": "METHOD",
    "method_name": "unify_mesh_normals",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
