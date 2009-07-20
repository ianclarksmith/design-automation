flip_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "FlipSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "flip_surface",

    "doc_html": """
        Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.
    """,

    "syntax_html": """
        Rhino.FlipSurface (strObject [, blnFlip])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a surface object.
            """
        },
        1: {
            "name": "Flip",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The new normal orientation, either flipped (True) or not flipped (False).  If omitted, the current normal orientation is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnFlip is not specified, the current normal orientation if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnFlip is specified, the previous normal orientation if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 718,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReverse",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

