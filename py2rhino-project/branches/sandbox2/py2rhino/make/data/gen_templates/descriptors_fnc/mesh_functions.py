#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_mesh = {
    "function_location": "mesh",
    "function_com_id": 494,
    "function_vb_name": "AddMesh",
    "function_name": "add_mesh",
    "function_parameters": (("vertices","array_of dbl","REQ"),("face_vertices","array_of int","REQ"),("vertex_normals","array_of dbl","OPT"),("texture_coordinates","array_of dbl","OPT"),("vertex_colors","array_of int","OPT")),
    "function_returns": ("string","null")
    }
add_planar_mesh = {
    "function_location": "mesh",
    "function_com_id": 915,
    "function_vb_name": "AddPlanarMesh",
    "function_name": "add_planar_mesh",
    "function_parameters": (("object","str","REQ"),("delete","bln","REQ")),
    "function_returns": ("string","null")
    }
curve_mesh_intersection = {
    "function_location": "mesh",
    "function_com_id": 842,
    "function_vb_name": "CurveMeshIntersection",
    "function_name": "curve_mesh_intersection",
    "function_parameters": (("curve","str","REQ"),("mesh","str","REQ"),("return_faces","bln","OPT")),
    "function_returns": ("array","array","array","number","null")
    }
disjoint_mesh_count = {
    "function_location": "mesh",
    "function_com_id": 721,
    "function_vb_name": "DisjointMeshCount",
    "function_name": "disjoint_mesh_count",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
duplicate_mesh_border = {
    "function_location": "mesh",
    "function_com_id": 853,
    "function_vb_name": "DuplicateMeshBorder",
    "function_name": "duplicate_mesh_border",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
explode_meshes = {
    "function_location": "mesh",
    "function_com_id": 903,
    "function_vb_name": "ExplodeMeshes",
    "function_name": "explode_meshes",
    "function_parameters": (("objects","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
is_mesh = {
    "function_location": "mesh",
    "function_com_id": 119,
    "function_vb_name": "IsMesh",
    "function_name": "is_mesh",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_mesh_closed = {
    "function_location": "mesh",
    "function_com_id": 355,
    "function_vb_name": "IsMeshClosed",
    "function_name": "is_mesh_closed",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_mesh_manifold = {
    "function_location": "mesh",
    "function_com_id": 855,
    "function_vb_name": "IsMeshManifold",
    "function_name": "is_mesh_manifold",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_area = {
    "function_location": "mesh",
    "function_com_id": 353,
    "function_vb_name": "MeshArea",
    "function_name": "mesh_area",
    "function_parameters": (("objects","array_of str","REQ")),
    "function_returns": ("array","number","number","number","null")
    }
mesh_area_centroid = {
    "function_location": "mesh",
    "function_com_id": 477,
    "function_vb_name": "MeshAreaCentroid",
    "function_name": "mesh_area_centroid",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_boolean_difference = {
    "function_location": "mesh",
    "function_com_id": 732,
    "function_vb_name": "MeshBooleanDifference",
    "function_name": "mesh_boolean_difference",
    "function_parameters": (("input0","array_of str","REQ"),("input1","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_boolean_intersection = {
    "function_location": "mesh",
    "function_com_id": 733,
    "function_vb_name": "MeshBooleanIntersection",
    "function_name": "mesh_boolean_intersection",
    "function_parameters": (("input0","array_of str","REQ"),("input1","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_boolean_split = {
    "function_location": "mesh",
    "function_com_id": 734,
    "function_vb_name": "MeshBooleanSplit",
    "function_name": "mesh_boolean_split",
    "function_parameters": (("input0","array_of str","REQ"),("input1","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_boolean_union = {
    "function_location": "mesh",
    "function_com_id": 731,
    "function_vb_name": "MeshBooleanUnion",
    "function_name": "mesh_boolean_union",
    "function_parameters": (("input","array_of str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_closest_point = {
    "function_location": "mesh",
    "function_com_id": 750,
    "function_vb_name": "MeshClosestPoint",
    "function_name": "mesh_closest_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","array","number","null")
    }
mesh_contour_points = {
    "function_location": "mesh",
    "function_com_id": 123,
    "function_vb_name": "MeshContourPoints",
    "function_name": "mesh_contour_points",
    "function_parameters": (("object","str","REQ"),("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("interval","dbl","OPT"),("remove_coincident_points","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_face_centers = {
    "function_location": "mesh",
    "function_com_id": 570,
    "function_vb_name": "MeshFaceCenters",
    "function_name": "mesh_face_centers",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_face_count = {
    "function_location": "mesh",
    "function_com_id": 124,
    "function_vb_name": "MeshFaceCount",
    "function_name": "mesh_face_count",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
mesh_face_normals = {
    "function_location": "mesh",
    "function_com_id": 569,
    "function_vb_name": "MeshFaceNormals",
    "function_name": "mesh_face_normals",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_face_vertices = {
    "function_location": "mesh",
    "function_com_id": 495,
    "function_vb_name": "MeshFaceVertices",
    "function_name": "mesh_face_vertices",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_faces = {
    "function_location": "mesh",
    "function_com_id": 125,
    "function_vb_name": "MeshFaces",
    "function_name": "mesh_faces",
    "function_parameters": (("object","str","REQ"),("face_type","bln","OPT")),
    "function_returns": ("array","null")
    }
mesh_has_face_normals = {
    "function_location": "mesh",
    "function_com_id": 696,
    "function_vb_name": "MeshHasFaceNormals",
    "function_name": "mesh_has_face_normals",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_has_texture_coordinates = {
    "function_location": "mesh",
    "function_com_id": 697,
    "function_vb_name": "MeshHasTextureCoordinates",
    "function_name": "mesh_has_texture_coordinates",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_has_vertex_colors = {
    "function_location": "mesh",
    "function_com_id": 698,
    "function_vb_name": "MeshHasVertexColors",
    "function_name": "mesh_has_vertex_colors",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_has_vertex_normals = {
    "function_location": "mesh",
    "function_com_id": 695,
    "function_vb_name": "MeshHasVertexNormals",
    "function_name": "mesh_has_vertex_normals",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_mesh_intersection = {
    "function_location": "mesh",
    "function_com_id": 749,
    "function_vb_name": "MeshMeshIntersection",
    "function_name": "mesh_mesh_intersection",
    "function_parameters": (("mesh1","str","REQ"),("mesh2","str","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","null")
    }
mesh_naked_edge_points = {
    "function_location": "mesh",
    "function_com_id": 580,
    "function_vb_name": "MeshNakedEdgePoints",
    "function_name": "mesh_naked_edge_points",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_offset = {
    "function_location": "mesh",
    "function_com_id": 720,
    "function_vb_name": "MeshOffset",
    "function_name": "mesh_offset",
    "function_parameters": (("mesh","str","REQ"),("distance","dbl","REQ")),
    "function_returns": ("string","null")
    }
mesh_quad_count = {
    "function_location": "mesh",
    "function_com_id": 350,
    "function_vb_name": "MeshQuadCount",
    "function_name": "mesh_quad_count",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
mesh_quads_to_triangles = {
    "function_location": "mesh",
    "function_com_id": 352,
    "function_vb_name": "MeshQuadsToTriangles",
    "function_name": "mesh_quads_to_triangles",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
mesh_texture_coordinates = {
    "function_location": "mesh",
    "function_com_id": 425,
    "function_vb_name": "MeshTextureCoordinates",
    "function_name": "mesh_texture_coordinates",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_triangle_count = {
    "function_location": "mesh",
    "function_com_id": 351,
    "function_vb_name": "MeshTriangleCount",
    "function_name": "mesh_triangle_count",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
mesh_vertex_colors = {
    "function_location": "mesh",
    "function_com_id": 699,
    "function_vb_name": "MeshVertexColors",
    "function_name": "mesh_vertex_colors",
    "function_parameters": (("object","str","REQ"),("vertex_colors","array_of int","OPT")),
    "function_returns": ("array","array","null")
    }
mesh_vertex_count = {
    "function_location": "mesh",
    "function_com_id": 126,
    "function_vb_name": "MeshVertexCount",
    "function_name": "mesh_vertex_count",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
mesh_vertex_normals = {
    "function_location": "mesh",
    "function_com_id": 426,
    "function_vb_name": "MeshVertexNormals",
    "function_name": "mesh_vertex_normals",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_vertices = {
    "function_location": "mesh",
    "function_com_id": 127,
    "function_vb_name": "MeshVertices",
    "function_name": "mesh_vertices",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
mesh_volume = {
    "function_location": "mesh",
    "function_com_id": 354,
    "function_vb_name": "MeshVolume",
    "function_name": "mesh_volume",
    "function_parameters": (("objects","array_of str","REQ")),
    "function_returns": ("array","number","number","number","null")
    }
mesh_volume_centroid = {
    "function_location": "mesh",
    "function_com_id": 478,
    "function_vb_name": "MeshVolumeCentroid",
    "function_name": "mesh_volume_centroid",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
pull_curve_to_mesh = {
    "function_location": "mesh",
    "function_com_id": 719,
    "function_vb_name": "PullCurveToMesh",
    "function_name": "pull_curve_to_mesh",
    "function_parameters": (("mesh","str","REQ"),("curve","str","REQ")),
    "function_returns": ("string","null")
    }
split_disjoint_mesh = {
    "function_location": "mesh",
    "function_com_id": 722,
    "function_vb_name": "SplitDisjointMesh",
    "function_name": "split_disjoint_mesh",
    "function_parameters": (("object","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
unify_mesh_normals = {
    "function_location": "mesh",
    "function_com_id": 723,
    "function_vb_name": "UnifyMeshNormals",
    "function_name": "unify_mesh_normals",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
