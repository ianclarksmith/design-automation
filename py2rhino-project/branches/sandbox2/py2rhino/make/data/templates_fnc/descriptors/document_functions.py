#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

create_preview_image = {
    "function_location": "document",
    "function_com_id": 388,
    "function_vb_name": "CreatePreviewImage",
    "function_name": "create_preview_image",
    "function_parameters": (("file","str","REQ"),("view","str","OPT"),("size","array_of int","OPT"),("flags","int","OPT"),("wireframe","bln","OPT")),
    "function_returns": ("boolean")
    }
document_modified = {
    "function_location": "document",
    "function_com_id": 323,
    "function_vb_name": "DocumentModified",
    "function_name": "document_modified",
    "function_parameters": (("modified","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
document_name = {
    "function_location": "document",
    "function_com_id": 113,
    "function_vb_name": "DocumentName",
    "function_name": "document_name",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
document_path = {
    "function_location": "document",
    "function_com_id": 301,
    "function_vb_name": "DocumentPath",
    "function_name": "document_path",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
document_u_r_l = {
    "function_location": "document",
    "function_com_id": 275,
    "function_vb_name": "DocumentURL",
    "function_name": "document_u_r_l",
    "function_parameters": (("u_r_l","str","OPT")),
    "function_returns": ("string","string","null")
    }
enable_redraw = {
    "function_location": "document",
    "function_com_id": 317,
    "function_vb_name": "EnableRedraw",
    "function_name": "enable_redraw",
    "function_parameters": (("select","bln","OPT")),
    "function_returns": ("boolean")
    }
extract_preview_image = {
    "function_location": "document",
    "function_com_id": 389,
    "function_vb_name": "ExtractPreviewImage",
    "function_name": "extract_preview_image",
    "function_parameters": (("file_name","str","REQ"),("model_name","str","OPT")),
    "function_returns": ("boolean")
    }
is_document_modified = {
    "function_location": "document",
    "function_com_id": 273,
    "function_vb_name": "IsDocumentModified",
    "function_name": "is_document_modified",
    "function_parameters": (),
    "function_returns": ("boolean")
    }
notes = {
    "function_location": "document",
    "function_com_id": 274,
    "function_vb_name": "Notes",
    "function_name": "notes",
    "function_parameters": (("notes","str","OPT")),
    "function_returns": ("string","string","null")
    }
read_file_version = {
    "function_location": "document",
    "function_com_id": 737,
    "function_vb_name": "ReadFileVersion",
    "function_name": "read_file_version",
    "function_parameters": (),
    "function_returns": ("number","null")
    }
redraw = {
    "function_location": "document",
    "function_com_id": 114,
    "function_vb_name": "Redraw",
    "function_name": "redraw",
    "function_parameters": (),
    "function_returns": ()
    }
render_antialias = {
    "function_location": "document",
    "function_com_id": 333,
    "function_vb_name": "RenderAntialias",
    "function_name": "render_antialias",
    "function_parameters": (("style","int","OPT")),
    "function_returns": ("number","number","number")
    }
render_color = {
    "function_location": "document",
    "function_com_id": 331,
    "function_vb_name": "RenderColor",
    "function_name": "render_color",
    "function_parameters": (("item","int","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_density = {
    "function_location": "document",
    "function_com_id": 844,
    "function_vb_name": "RenderMeshDensity",
    "function_name": "render_mesh_density",
    "function_parameters": (("density","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_max_angle = {
    "function_location": "document",
    "function_com_id": 845,
    "function_vb_name": "RenderMeshMaxAngle",
    "function_name": "render_mesh_max_angle",
    "function_parameters": (("angle","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_max_aspect_ratio = {
    "function_location": "document",
    "function_com_id": 846,
    "function_vb_name": "RenderMeshMaxAspectRatio",
    "function_name": "render_mesh_max_aspect_ratio",
    "function_parameters": (("ratio","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_max_dist_edge_to_srf = {
    "function_location": "document",
    "function_com_id": 849,
    "function_vb_name": "RenderMeshMaxDistEdgeToSrf",
    "function_name": "render_mesh_max_dist_edge_to_srf",
    "function_parameters": (("distance","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_max_edge_length = {
    "function_location": "document",
    "function_com_id": 848,
    "function_vb_name": "RenderMeshMaxEdgeLength",
    "function_name": "render_mesh_max_edge_length",
    "function_parameters": (("length","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_min_edge_length = {
    "function_location": "document",
    "function_com_id": 847,
    "function_vb_name": "RenderMeshMinEdgeLength",
    "function_name": "render_mesh_min_edge_length",
    "function_parameters": (("length","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_min_initial_grid_quads = {
    "function_location": "document",
    "function_com_id": 850,
    "function_vb_name": "RenderMeshMinInitialGridQuads",
    "function_name": "render_mesh_min_initial_grid_quads",
    "function_parameters": (("quads","int","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_quality = {
    "function_location": "document",
    "function_com_id": 843,
    "function_vb_name": "RenderMeshQuality",
    "function_name": "render_mesh_quality",
    "function_parameters": (("quality","int","OPT")),
    "function_returns": ("number","number","null")
    }
render_mesh_settings = {
    "function_location": "document",
    "function_com_id": 851,
    "function_vb_name": "RenderMeshSettings",
    "function_name": "render_mesh_settings",
    "function_parameters": (("settings","int","OPT")),
    "function_returns": ("number","number","null")
    }
render_resolution = {
    "function_location": "document",
    "function_com_id": 332,
    "function_vb_name": "RenderResolution",
    "function_name": "render_resolution",
    "function_parameters": (("resolution","array_of int","REQ")),
    "function_returns": ("array","array","null")
    }
render_settings = {
    "function_location": "document",
    "function_com_id": 334,
    "function_vb_name": "RenderSettings",
    "function_name": "render_settings",
    "function_parameters": (("settings","int","OPT")),
    "function_returns": ("number","number","number")
    }
unit_absolute_tolerance = {
    "function_location": "document",
    "function_com_id": 324,
    "function_vb_name": "UnitAbsoluteTolerance",
    "function_name": "unit_absolute_tolerance",
    "function_parameters": (("abs_tol","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
unit_angle_tolerance = {
    "function_location": "document",
    "function_com_id": 325,
    "function_vb_name": "UnitAngleTolerance",
    "function_name": "unit_angle_tolerance",
    "function_parameters": (("angle_tol","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
unit_custom_unit_system = {
    "function_location": "document",
    "function_com_id": 326,
    "function_vb_name": "UnitCustomUnitSystem",
    "function_name": "unit_custom_unit_system",
    "function_parameters": (("units","dbl","REQ"),("scale","bln","OPT"),("name","str","OPT")),
    "function_returns": ("number","null")
    }
unit_distance_display_mode = {
    "function_location": "document",
    "function_com_id": 327,
    "function_vb_name": "UnitDistanceDisplayMode",
    "function_name": "unit_distance_display_mode",
    "function_parameters": (("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
unit_distance_display_precision = {
    "function_location": "document",
    "function_com_id": 328,
    "function_vb_name": "UnitDistanceDisplayPrecision",
    "function_name": "unit_distance_display_precision",
    "function_parameters": (("precision","int","OPT")),
    "function_returns": ("number","number","null")
    }
unit_relative_tolerance = {
    "function_location": "document",
    "function_com_id": 329,
    "function_vb_name": "UnitRelativeTolerance",
    "function_name": "unit_relative_tolerance",
    "function_parameters": (("rel_tol","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
unit_scale = {
    "function_location": "document",
    "function_com_id": 868,
    "function_vb_name": "UnitScale",
    "function_name": "unit_scale",
    "function_parameters": (("to_system","int","REQ"),("from_system","int","OPT")),
    "function_returns": ("number","null")
    }
unit_system = {
    "function_location": "document",
    "function_com_id": 330,
    "function_vb_name": "UnitSystem",
    "function_name": "unit_system",
    "function_parameters": (("system","int","OPT"),("scale","bln","OPT")),
    "function_returns": ("number","null")
    }
unit_system_name = {
    "function_location": "document",
    "function_com_id": 492,
    "function_vb_name": "UnitSystemName",
    "function_name": "unit_system_name",
    "function_parameters": (("capitalize","bln","OPT"),("singular","bln","OPT"),("abbreviate","bln","OPT")),
    "function_returns": ("string")
    }
