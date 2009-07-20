is_surface_closed = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsSurfaceClosed",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_surface_closed",

    "doc_html": """
        Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.
    """,

    "syntax_html": """
        Rhino.IsSurfaceClosed (strObject, intDirection)
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

    "id_com": 211,

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

