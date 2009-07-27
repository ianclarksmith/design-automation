#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

add_material_to_layer = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "add_material_to_layer",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
add_material_to_object = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "add_material_to_object",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
copy_material = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "copy_material",
    "method_parameters": (("src_index","int","REQ"),("dst_index","int","REQ")),
    "method_returns": ("boolean","null")
    }
is_material_default = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "is_material_default",
    "method_parameters": (("material_index","int","REQ")),
    "method_returns": ("null")
    }
is_material_reference = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "is_material_reference",
    "method_parameters": (("material_index","int","REQ")),
    "method_returns": ("boolean","null")
    }
match_material = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "match_material",
    "method_parameters": (("src_material_index","int","REQ"),("src_object","str","REQ"),("dest_objects","arr_of_str","REQ")),
    "method_returns": ("number","null")
    }
material_bump = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_bump",
    "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "method_returns": ("string","string","null")
    }
material_color = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_color",
    "method_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
material_environment_map = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_environment_map",
    "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "method_returns": ("string","string","null")
    }
material_name = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_name",
    "method_parameters": (("material_index","int","REQ"),("name","str","OPT")),
    "method_returns": ("string","string","null")
    }
material_reflective_color = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_reflective_color",
    "method_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
material_shine = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_shine",
    "method_parameters": (("material_index","int","REQ"),("shine","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
material_texture = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_texture",
    "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "method_returns": ("string","string","null")
    }
material_transparency = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_transparency",
    "method_parameters": (("material_index","int","REQ"),("transparency","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
material_transparency_map = {
    "method_location": "Material",
    "method_type": "METHOD",
    "method_name": "material_transparency_map",
    "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "method_returns": ("string","string","null")
    }
