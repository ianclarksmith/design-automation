#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

create_preview_image = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "create_preview_image",
    "method_parameters": (("file","str","REQ"),("view","str","OPT"),("size","array_of int","OPT"),("flags","int","OPT"),("wireframe","bln","OPT")),
    "method_returns": ("boolean")
    }
document_modified = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "document_modified",
    "method_parameters": (("modified","bln","OPT")),
    "method_returns": ("boolean","boolean")
    }
document_name = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "document_name",
    "method_parameters": (),
    "method_returns": ("string","null")
    }
document_path = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "document_path",
    "method_parameters": (),
    "method_returns": ("string","null")
    }
document_u_r_l = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "document_u_r_l",
    "method_parameters": (("u_r_l","str","OPT")),
    "method_returns": ("string","string","null")
    }
enable_redraw = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "enable_redraw",
    "method_parameters": (("select","bln","OPT")),
    "method_returns": ("boolean")
    }
extract_preview_image = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "extract_preview_image",
    "method_parameters": (("file_name","str","REQ"),("model_name","str","OPT")),
    "method_returns": ("boolean")
    }
is_document_modified = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "is_document_modified",
    "method_parameters": (),
    "method_returns": ("boolean")
    }
notes = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "notes",
    "method_parameters": (("notes","str","OPT")),
    "method_returns": ("string","string","null")
    }
read_file_version = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "read_file_version",
    "method_parameters": (),
    "method_returns": ("number","null")
    }
redraw = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "redraw",
    "method_parameters": (),
    "method_returns": ()
    }
render_antialias = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_antialias",
    "method_parameters": (("style","int","OPT")),
    "method_returns": ("number","number","number")
    }
render_color = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_color",
    "method_parameters": (("item","int","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_density = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_density",
    "method_parameters": (("density","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_max_angle = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_max_angle",
    "method_parameters": (("angle","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_max_aspect_ratio = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_max_aspect_ratio",
    "method_parameters": (("ratio","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_max_dist_edge_to_srf = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_max_dist_edge_to_srf",
    "method_parameters": (("distance","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_max_edge_length = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_max_edge_length",
    "method_parameters": (("length","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_min_edge_length = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_min_edge_length",
    "method_parameters": (("length","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_min_initial_grid_quads = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_min_initial_grid_quads",
    "method_parameters": (("quads","int","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_quality = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_quality",
    "method_parameters": (("quality","int","OPT")),
    "method_returns": ("number","number","null")
    }
render_mesh_settings = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_mesh_settings",
    "method_parameters": (("settings","int","OPT")),
    "method_returns": ("number","number","null")
    }
render_resolution = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_resolution",
    "method_parameters": (("resolution","array_of int","REQ")),
    "method_returns": ("array","array","null")
    }
render_settings = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "render_settings",
    "method_parameters": (("settings","int","OPT")),
    "method_returns": ("number","number","number")
    }
unit_absolute_tolerance = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_absolute_tolerance",
    "method_parameters": (("abs_tol","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
unit_angle_tolerance = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_angle_tolerance",
    "method_parameters": (("angle_tol","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
unit_custom_unit_system = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_custom_unit_system",
    "method_parameters": (("units","dbl","REQ"),("scale","bln","OPT"),("name","str","OPT")),
    "method_returns": ("number","null")
    }
unit_distance_display_mode = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_distance_display_mode",
    "method_parameters": (("mode","int","OPT")),
    "method_returns": ("number","number","null")
    }
unit_distance_display_precision = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_distance_display_precision",
    "method_parameters": (("precision","int","OPT")),
    "method_returns": ("number","number","null")
    }
unit_relative_tolerance = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_relative_tolerance",
    "method_parameters": (("rel_tol","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
unit_scale = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_scale",
    "method_parameters": (("to_system","int","REQ"),("from_system","int","OPT")),
    "method_returns": ("number","null")
    }
unit_system = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_system",
    "method_parameters": (("system","int","OPT"),("scale","bln","OPT")),
    "method_returns": ("number","null")
    }
unit_system_name = {
    "method_location": "document",
    "method_type": "FUNCTION",
    "method_name": "unit_system_name",
    "method_parameters": (("capitalize","bln","OPT"),("singular","bln","OPT"),("abbreviate","bln","OPT")),
    "method_returns": ("string")
    }
