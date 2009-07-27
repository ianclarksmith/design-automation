reverse_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ReverseSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "reverse_surface",

    "doc_html": """
        Reverses the U and V directions of a surface object. This feature can also be found in Rhino's Dir command.
		To reverse the normal direction of a surface, use the FlipSurface method.
    """,

    "syntax_html": {
        0: ("strObject", "intDirection"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "intDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The direction to reverse. Values can be added together so as to reverse more than one direction.
		Value
		Description
		1
		Reverse the surface in the U direction.
		2
		Reverse the surface in the V direction.
		4
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 927,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

