is_torus = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsTorus",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_torus",

    "doc_html": """
        Determines if a surface is a portion of a torus.
    """,

    "syntax_html": {
        0: ("strSurface"),
    },

    "params_html": {
        0: {
            "name": "strSurface",
            "py_name": "surface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
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

    "id_com": 886,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

