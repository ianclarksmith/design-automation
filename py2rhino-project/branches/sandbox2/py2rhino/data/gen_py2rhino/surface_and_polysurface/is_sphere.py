is_sphere = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsSphere",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_sphere",

    "doc_html": """
        Determines if a surface is a portion of a sphere.
    """,

    "syntax_html": """
        Rhino.IsSphere (strSurface)
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 883,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

