is_poly_surface_planar = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsPolySurfacePlanar",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_poly_surface_planar",

    "doc_html": """
        Verifies a polysurface object is planar.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
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

    "id_com": 209,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

