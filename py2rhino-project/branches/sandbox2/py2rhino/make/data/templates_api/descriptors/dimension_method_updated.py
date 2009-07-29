#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# Dimension
#===============================================================================
add_dim_style = {
    "method_location": "_Entity.Dimension",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("","self","OPT")),
    "method_returns": ("_Entity.Dimension","null")
    }
current_dim_style = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "current_dim_style",
    "method_parameters": (("","self","OPT")),
    "method_returns": ("string","string","null")
    }
delete_dim_style = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "delete_dim_style",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("string","null")
    }
dim_scale = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_scale",
    "method_parameters": (("scale","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_angle_precision = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_angle_precision",
    "method_parameters": (("","self","REQ"),("precision","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_arrow_size = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_arrow_size",
    "method_parameters": (("","self","REQ"),("size","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_count = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
dim_style_extension = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_extension",
    "method_parameters": (("","self","REQ"),("extension","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_font = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_font",
    "method_parameters": (("dim_style","str","REQ"),("font","str","OPT")),
    "method_returns": ("string","string","null")
    }
dim_style_leader_arrow_size = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_leader_arrow_size",
    "method_parameters": (("","self","REQ"),("size","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_linear_precision = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_linear_precision",
    "method_parameters": (("","self","REQ"),("precision","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_names = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_names",
    "method_parameters": (("sort","bln","OPT")),
    "method_returns": ("array","null")
    }
dim_style_number_format = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_number_format",
    "method_parameters": (("","self","REQ"),("format","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_offset = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_offset",
    "method_parameters": (("","self","REQ"),("offset","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_alignment = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_alignment",
    "method_parameters": (("","self","REQ"),("alignment","int","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_gap = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_gap",
    "method_parameters": (("","self","REQ"),("gap","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dim_style_text_height = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dim_style_text_height",
    "method_parameters": (("","self","REQ"),("height","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
dimension_style = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_style",
    "method_parameters": (("","self","REQ"),("style","str","OPT")),
    "method_returns": ("string","string","null")
    }
dimension_text = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_text",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("string","null")
    }
dimension_user_text = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_user_text",
    "method_parameters": (("","self","REQ"),("user_text","str","OPT")),
    "method_returns": ("string","string","null")
    }
dimension_value = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "dimension_value",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
rename_dim_style = {
    "method_location": "_Entity.Dimension",
    "method_type": "METHOD",
    "method_name": "rename_dim_style",
    "method_parameters": (("","self","REQ"),("new_style","str","REQ")),
    "method_returns": ("string","null")
    }
#===============================================================================
# _Entity
#===============================================================================
add_leader = {
    "method_location": "_Entity",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("points","arr_of_dbl","REQ"),("view","str","OPT"),("text","str","OPT")),
    "method_returns": ("_Entity","null")
    }
leader_text = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "leader_text",
    "method_parameters": (("","self","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
is_aligned_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_aligned_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_angular_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_angular_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_diameter_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_diameter_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_dim_style = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_dim_style",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("null")
    }
is_dim_style_reference = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_dim_style_reference",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_leader = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_leader",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_linear_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_linear_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_ordinate_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_ordinate_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_radial_dimension = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_radial_dimension",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
