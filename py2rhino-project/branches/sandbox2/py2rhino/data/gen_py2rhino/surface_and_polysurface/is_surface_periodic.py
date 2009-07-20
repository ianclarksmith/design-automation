is_surface_periodic = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsSurfacePeriodic",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_surface_periodic",

    "doc_html": """
        Verifies a surface object is periodic in the specified direction.
    """,

    "syntax_html": """
        Rhino.IsSurfacePeriodic (strObject, intDirection)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction, either 0 = U, or 1 = V.
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

    "id_com": 212,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

