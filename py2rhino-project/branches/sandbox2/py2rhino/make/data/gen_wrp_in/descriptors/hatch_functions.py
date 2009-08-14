#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_hatch = {
    "function_location": "hatch",
    "function_com_id": 835,
    "function_vb_name": "AddHatch",
    "function_name": "add_hatch",
    "function_parameters": (("curve","str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
    "function_returns": ("string","null")
    }
add_hatch_patterns = {
    "function_location": "hatch",
    "function_com_id": 826,
    "function_vb_name": "AddHatchPatterns",
    "function_name": "add_hatch_patterns",
    "function_parameters": (("file_name","str","REQ"),("replace","bln","OPT")),
    "function_returns": ("array","null")
    }
add_hatches = {
    "function_location": "hatch",
    "function_com_id": 836,
    "function_vb_name": "AddHatches",
    "function_name": "add_hatches",
    "function_parameters": (("curves","array_of str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
    "function_returns": ("array","null")
    }
current_hatch_pattern = {
    "function_location": "hatch",
    "function_com_id": 827,
    "function_vb_name": "CurrentHatchPattern",
    "function_name": "current_hatch_pattern",
    "function_parameters": (("hatch","str","OPT"),),
    "function_returns": ("string","string","null")
    }
explode_hatch = {
    "function_location": "hatch",
    "function_com_id": 841,
    "function_vb_name": "ExplodeHatch",
    "function_name": "explode_hatch",
    "function_parameters": (("hatch","str","REQ"),("delete","bln","OPT")),
    "function_returns": ("array","null")
    }
hatch_pattern = {
    "function_location": "hatch",
    "function_com_id": 837,
    "function_vb_name": "HatchPattern",
    "function_name": "hatch_pattern",
    "function_parameters": (("object","str","REQ"),("hatch","str","OPT")),
    "function_returns": ("string","string","null")
    }
hatch_pattern_count = {
    "function_location": "hatch",
    "function_com_id": 828,
    "function_vb_name": "HatchPatternCount",
    "function_name": "hatch_pattern_count",
    "function_parameters": (),
    "function_returns": ("number",)
    }
hatch_pattern_description = {
    "function_location": "hatch",
    "function_com_id": 829,
    "function_vb_name": "HatchPatternDescription",
    "function_name": "hatch_pattern_description",
    "function_parameters": (("hatch","str","REQ"),),
    "function_returns": ("string","null")
    }
hatch_pattern_fill_type = {
    "function_location": "hatch",
    "function_com_id": 831,
    "function_vb_name": "HatchPatternFillType",
    "function_name": "hatch_pattern_fill_type",
    "function_parameters": (("hatch","str","REQ"),),
    "function_returns": ("number","null")
    }
hatch_pattern_names = {
    "function_location": "hatch",
    "function_com_id": 830,
    "function_vb_name": "HatchPatternNames",
    "function_name": "hatch_pattern_names",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
hatch_rotation = {
    "function_location": "hatch",
    "function_com_id": 839,
    "function_vb_name": "HatchRotation",
    "function_name": "hatch_rotation",
    "function_parameters": (("object","str","REQ"),("rotation","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
hatch_scale = {
    "function_location": "hatch",
    "function_com_id": 838,
    "function_vb_name": "HatchScale",
    "function_name": "hatch_scale",
    "function_parameters": (("object","str","REQ"),("scale","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
is_hatch = {
    "function_location": "hatch",
    "function_com_id": 840,
    "function_vb_name": "IsHatch",
    "function_name": "is_hatch",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_hatch_pattern = {
    "function_location": "hatch",
    "function_com_id": 832,
    "function_vb_name": "IsHatchPattern",
    "function_name": "is_hatch_pattern",
    "function_parameters": (("hatch","str","REQ"),),
    "function_returns": ("null",)
    }
is_hatch_pattern_current = {
    "function_location": "hatch",
    "function_com_id": 833,
    "function_vb_name": "IsHatchPatternCurrent",
    "function_name": "is_hatch_pattern_current",
    "function_parameters": (("hatch","str","REQ"),),
    "function_returns": ("null",)
    }
is_hatch_pattern_reference = {
    "function_location": "hatch",
    "function_com_id": 834,
    "function_vb_name": "IsHatchPatternReference",
    "function_name": "is_hatch_pattern_reference",
    "function_parameters": (("hatch","str","REQ"),),
    "function_returns": ("null",)
    }
