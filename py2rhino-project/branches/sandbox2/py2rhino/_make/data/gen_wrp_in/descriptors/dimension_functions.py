#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_dim_style = {
    "function_location": "dimension",
    "function_com_id": 455,
    "function_vb_name": "AddDimStyle",
    "function_name": "add_dim_style",
    "function_parameters": (("dim_style","str","OPT"),),
    "function_returns": ("string","null")
    }
add_leader = {
    "function_location": "dimension",
    "function_com_id": 321,
    "function_vb_name": "AddLeader",
    "function_name": "add_leader",
    "function_parameters": (("points","array_of dbl","REQ"),("view","str","OPT"),("text","str","OPT")),
    "function_returns": ("string","null")
    }
current_dim_style = {
    "function_location": "dimension",
    "function_com_id": 453,
    "function_vb_name": "CurrentDimStyle",
    "function_name": "current_dim_style",
    "function_parameters": (("dim_style","str","OPT"),),
    "function_returns": ("string","string","null")
    }
delete_dim_style = {
    "function_location": "dimension",
    "function_com_id": 456,
    "function_vb_name": "DeleteDimStyle",
    "function_name": "delete_dim_style",
    "function_parameters": (("dim_style","str","REQ"),),
    "function_returns": ("string","null")
    }
dim_scale = {
    "function_location": "dimension",
    "function_com_id": 460,
    "function_vb_name": "DimScale",
    "function_name": "dim_scale",
    "function_parameters": (("scale","dbl","OPT"),),
    "function_returns": ("number","number","null")
    }
dim_style_angle_precision = {
    "function_location": "dimension",
    "function_com_id": 464,
    "function_vb_name": "DimStyleAnglePrecision",
    "function_name": "dim_style_angle_precision",
    "function_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_arrow_size = {
    "function_location": "dimension",
    "function_com_id": 468,
    "function_vb_name": "DimStyleArrowSize",
    "function_name": "dim_style_arrow_size",
    "function_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_count = {
    "function_location": "dimension",
    "function_com_id": 451,
    "function_vb_name": "DimStyleCount",
    "function_name": "dim_style_count",
    "function_parameters": (),
    "function_returns": ("number",)
    }
dim_style_extension = {
    "function_location": "dimension",
    "function_com_id": 466,
    "function_vb_name": "DimStyleExtension",
    "function_name": "dim_style_extension",
    "function_parameters": (("dim_style","str","REQ"),("extension","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_font = {
    "function_location": "dimension",
    "function_com_id": 462,
    "function_vb_name": "DimStyleFont",
    "function_name": "dim_style_font",
    "function_parameters": (("dim_style","str","REQ"),("font","str","OPT")),
    "function_returns": ("string","string","null")
    }
dim_style_leader_arrow_size = {
    "function_location": "dimension",
    "function_com_id": 704,
    "function_vb_name": "DimStyleLeaderArrowSize",
    "function_name": "dim_style_leader_arrow_size",
    "function_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_linear_precision = {
    "function_location": "dimension",
    "function_com_id": 463,
    "function_vb_name": "DimStyleLinearPrecision",
    "function_name": "dim_style_linear_precision",
    "function_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_names = {
    "function_location": "dimension",
    "function_com_id": 452,
    "function_vb_name": "DimStyleNames",
    "function_name": "dim_style_names",
    "function_parameters": (("sort","bln","OPT"),),
    "function_returns": ("array","null")
    }
dim_style_number_format = {
    "function_location": "dimension",
    "function_com_id": 459,
    "function_vb_name": "DimStyleNumberFormat",
    "function_name": "dim_style_number_format",
    "function_parameters": (("dim_style","str","REQ"),("format","int","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_offset = {
    "function_location": "dimension",
    "function_com_id": 467,
    "function_vb_name": "DimStyleOffset",
    "function_name": "dim_style_offset",
    "function_parameters": (("dim_style","str","REQ"),("offset","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_text_alignment = {
    "function_location": "dimension",
    "function_com_id": 461,
    "function_vb_name": "DimStyleTextAlignment",
    "function_name": "dim_style_text_alignment",
    "function_parameters": (("dim_style","str","REQ"),("alignment","int","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_text_gap = {
    "function_location": "dimension",
    "function_com_id": 741,
    "function_vb_name": "DimStyleTextGap",
    "function_name": "dim_style_text_gap",
    "function_parameters": (("dim_style","str","REQ"),("gap","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dim_style_text_height = {
    "function_location": "dimension",
    "function_com_id": 465,
    "function_vb_name": "DimStyleTextHeight",
    "function_name": "dim_style_text_height",
    "function_parameters": (("dim_style","str","REQ"),("height","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
dimension_style = {
    "function_location": "dimension",
    "function_com_id": 703,
    "function_vb_name": "DimensionStyle",
    "function_name": "dimension_style",
    "function_parameters": (("object","str","REQ"),("style","str","OPT")),
    "function_returns": ("string","string","null")
    }
dimension_text = {
    "function_location": "dimension",
    "function_com_id": 469,
    "function_vb_name": "DimensionText",
    "function_name": "dimension_text",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("string","null")
    }
dimension_user_text = {
    "function_location": "dimension",
    "function_com_id": 563,
    "function_vb_name": "DimensionUserText",
    "function_name": "dimension_user_text",
    "function_parameters": (("object","str","REQ"),("user_text","str","OPT")),
    "function_returns": ("string","string","null")
    }
dimension_value = {
    "function_location": "dimension",
    "function_com_id": 568,
    "function_vb_name": "DimensionValue",
    "function_name": "dimension_value",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
is_aligned_dimension = {
    "function_location": "dimension",
    "function_com_id": 566,
    "function_vb_name": "IsAlignedDimension",
    "function_name": "is_aligned_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_angular_dimension = {
    "function_location": "dimension",
    "function_com_id": 338,
    "function_vb_name": "IsAngularDimension",
    "function_name": "is_angular_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_diameter_dimension = {
    "function_location": "dimension",
    "function_com_id": 565,
    "function_vb_name": "IsDiameterDimension",
    "function_name": "is_diameter_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_dim_style = {
    "function_location": "dimension",
    "function_com_id": 454,
    "function_vb_name": "IsDimStyle",
    "function_name": "is_dim_style",
    "function_parameters": (("dim_style","str","REQ"),),
    "function_returns": ("null",)
    }
is_dim_style_reference = {
    "function_location": "dimension",
    "function_com_id": 457,
    "function_vb_name": "IsDimStyleReference",
    "function_name": "is_dim_style_reference",
    "function_parameters": (("dim_style","str","REQ"),),
    "function_returns": ("null",)
    }
is_dimension = {
    "function_location": "dimension",
    "function_com_id": 564,
    "function_vb_name": "IsDimension",
    "function_name": "is_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_leader = {
    "function_location": "dimension",
    "function_com_id": 337,
    "function_vb_name": "IsLeader",
    "function_name": "is_leader",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_linear_dimension = {
    "function_location": "dimension",
    "function_com_id": 339,
    "function_vb_name": "IsLinearDimension",
    "function_name": "is_linear_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_ordinate_dimension = {
    "function_location": "dimension",
    "function_com_id": 659,
    "function_vb_name": "IsOrdinateDimension",
    "function_name": "is_ordinate_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_radial_dimension = {
    "function_location": "dimension",
    "function_com_id": 340,
    "function_vb_name": "IsRadialDimension",
    "function_name": "is_radial_dimension",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
leader_text = {
    "function_location": "dimension",
    "function_com_id": 895,
    "function_vb_name": "LeaderText",
    "function_name": "leader_text",
    "function_parameters": (("object","str","REQ"),("text","str","OPT")),
    "function_returns": ("string","string","null")
    }
rename_dim_style = {
    "function_location": "dimension",
    "function_com_id": 458,
    "function_vb_name": "RenameDimStyle",
    "function_name": "rename_dim_style",
    "function_parameters": (("old_style","str","REQ"),("new_style","str","REQ")),
    "function_returns": ("string","null")
    }
