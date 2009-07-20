is_poly_surface_closed = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsPolySurfaceClosed",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_poly_surface_closed",

    "doc_html": """
        Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.
    """,

    "syntax_html": """
        Rhino.IsPolySurfaceClosed (strObject)
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

    "id_com": 208,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

