#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

add_dim_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "add_dim_style",
    "method_parameters": (("dim_style","str","OPT")),
    "method_returns": ("string","null")
    }
add_leader = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "add_leader",
    "method_parameters": (("points","arr_of_dbl","REQ"),("view","str","OPT"),("text","str","OPT")),
    "method_returns": ("string","null")
    }
current_dim_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "current_dim_style",
    "method_parameters": (("dim_style","str","OPT")),
    "method_returns": ("string","string","null")
    }
delete_dim_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "delete_dim_style",
    "method_parameters": (("dim_style","str","REQ")),
    "method_returns": ("string","null")
    }
dim_scale = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_scale",
    "method_parameters": (("scale","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_angle_precision = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_angle_precision",
    "method_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_arrow_size = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_arrow_size",
    "method_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_count = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
dim_style_extension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_extension",
    "method_parameters": (("dim_style","str","REQ"),("extension","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_font = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_font",
    "method_parameters": (("dim_style","str","REQ"),("font","str","OPT")),
    "method_returns": ("string","string","null")
    }
dim_style_leader_arrow_size = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_leader_arrow_size",
    "method_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_linear_precision = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_linear_precision",
    "method_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_names = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_names",
    "method_parameters": (("sort","bln","OPT")),
    "method_returns": ("array","null")
    }
dim_style_number_format = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_number_format",
    "method_parameters": (("dim_style","str","REQ"),("format","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_offset = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_offset",
    "method_parameters": (("dim_style","str","REQ"),("offset","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_alignment = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_alignment",
    "method_parameters": (("dim_style","str","REQ"),("alignment","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_gap = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_gap",
    "method_parameters": (("dim_style","str","REQ"),("gap","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_height = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_height",
    "method_parameters": (("dim_style","str","REQ"),("height","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dimension_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_style",
    "method_parameters": (("object","str","REQ"),("style","str","OPT")),
    "method_returns": ("string","string","null")
    }
dimension_text = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_text",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("string","null")
    }
dimension_user_text = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_user_text",
    "method_parameters": (("object","str","REQ"),("user_text","str","OPT")),
    "method_returns": ("string","string","null")
    }
dimension_value = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_value",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
is_aligned_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_aligned_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_angular_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_angular_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_diameter_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_diameter_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_dim_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_dim_style",
    "method_parameters": (("dim_style","str","REQ")),
    "method_returns": ("null")
    }
is_dim_style_reference = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_dim_style_reference",
    "method_parameters": (("dim_style","str","REQ")),
    "method_returns": ("null")
    }
is_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_leader = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_leader",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_linear_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_linear_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_ordinate_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_ordinate_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_radial_dimension = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "is_radial_dimension",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
leader_text = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "leader_text",
    "method_parameters": (("object","str","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
rename_dim_style = {
    "method_location": "Dimension",
    "method_type": "METHOD",
    "method_name": "rename_dim_style",
    "method_parameters": (("old_style","str","REQ"),("new_style","str","REQ")),
    "method_returns": ("string","null")
    }
