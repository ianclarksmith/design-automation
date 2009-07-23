surface_edit_points = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceEditPoints",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_edit_points",

    "doc_html": """
        Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.
    """,

    "syntax_html": {
        0: ("strObject", "blnReturnParameters", "blnReturnAll"),
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
        1: {
            "name": "blnReturnParameters",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnParameters",
            "doc": """
        If False (default), edit points are returned as an array of 3-D points. If True, edit points are returned as an array U,V surface parameters.
            """
        },
        2: {
            "name": "blnReturnAll",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnAll",
            "doc": """
        If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnReturnParameters is True, then an array of U,V parameter values if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 427,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReturnParameters",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaReturnAll",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

