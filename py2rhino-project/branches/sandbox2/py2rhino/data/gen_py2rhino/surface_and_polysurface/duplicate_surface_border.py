duplicate_surface_border = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "DuplicateSurfaceBorder",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "duplicate_surface_border",

    "doc_html": """
        Creates a curve that duplicates a surface or polysurface border.
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
        The identifier of the surface or polysurface object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the new curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 852,

    "params_com": {
        0: {
            "name": "vaSurface",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

