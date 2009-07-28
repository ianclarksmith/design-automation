#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_material_to_layer = {
    "function_location": "material",
    "function_com_id": 173,
    "function_vb_name": "AddMaterialToLayer",
    "function_name": "add_material_to_layer",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
add_material_to_object = {
    "function_location": "material",
    "function_com_id": 174,
    "function_vb_name": "AddMaterialToObject",
    "function_name": "add_material_to_object",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("number","null")
    }
copy_material = {
    "function_location": "material",
    "function_com_id": 812,
    "function_vb_name": "CopyMaterial",
    "function_name": "copy_material",
    "function_parameters": (("src_index","int","REQ"),("dst_index","int","REQ")),
    "function_returns": ("boolean","null")
    }
is_material_default = {
    "function_location": "material",
    "function_com_id": 175,
    "function_vb_name": "IsMaterialDefault",
    "function_name": "is_material_default",
    "function_parameters": (("material_index","int","REQ")),
    "function_returns": ("null")
    }
is_material_reference = {
    "function_location": "material",
    "function_com_id": 176,
    "function_vb_name": "IsMaterialReference",
    "function_name": "is_material_reference",
    "function_parameters": (("material_index","int","REQ")),
    "function_returns": ("boolean","null")
    }
match_material = {
    "function_location": "material",
    "function_com_id": 322,
    "function_vb_name": "MatchMaterial",
    "function_name": "match_material",
    "function_parameters": (("src_material_index","int","REQ")),
    "function_returns": ("number","null")
    }
match_material_2 = {
    "function_location": "material",
    "function_com_id": 322,
    "function_vb_name": "MatchMaterial",
    "function_name": "match_material_2",
    "function_parameters": (("src_object","str","REQ"),("dest_objects","array_of str","REQ")),
    "function_returns": ("number","null")
    }
material_bump = {
    "function_location": "material",
    "function_com_id": 177,
    "function_vb_name": "MaterialBump",
    "function_name": "material_bump",
    "function_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "function_returns": ("string","string","null")
    }
material_color = {
    "function_location": "material",
    "function_com_id": 178,
    "function_vb_name": "MaterialColor",
    "function_name": "material_color",
    "function_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
material_environment_map = {
    "function_location": "material",
    "function_com_id": 754,
    "function_vb_name": "MaterialEnvironmentMap",
    "function_name": "material_environment_map",
    "function_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "function_returns": ("string","string","null")
    }
material_name = {
    "function_location": "material",
    "function_com_id": 179,
    "function_vb_name": "MaterialName",
    "function_name": "material_name",
    "function_parameters": (("material_index","int","REQ"),("name","str","OPT")),
    "function_returns": ("string","string","null")
    }
material_reflective_color = {
    "function_location": "material",
    "function_com_id": 180,
    "function_vb_name": "MaterialReflectiveColor",
    "function_name": "material_reflective_color",
    "function_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
material_shine = {
    "function_location": "material",
    "function_com_id": 181,
    "function_vb_name": "MaterialShine",
    "function_name": "material_shine",
    "function_parameters": (("material_index","int","REQ"),("shine","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
material_texture = {
    "function_location": "material",
    "function_com_id": 182,
    "function_vb_name": "MaterialTexture",
    "function_name": "material_texture",
    "function_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "function_returns": ("string","string","null")
    }
material_transparency = {
    "function_location": "material",
    "function_com_id": 183,
    "function_vb_name": "MaterialTransparency",
    "function_name": "material_transparency",
    "function_parameters": (("material_index","int","REQ"),("transparency","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
material_transparency_map = {
    "function_location": "material",
    "function_com_id": 753,
    "function_vb_name": "MaterialTransparencyMap",
    "function_name": "material_transparency_map",
    "function_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
    "function_returns": ("string","string","null")
    }
