surface_points = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfacePoints",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_points",

    "doc_html": """
        Returns the control points, or control vertices, of a surface object.
    """,

    "syntax_html": """
        Rhino.SurfacePoints (strObject [, blnReturnAll])
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
            "name": "ReturnAll",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The control points of the surface if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 372,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReturnAll",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

