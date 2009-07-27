surface_point_count = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfacePointCount",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_point_count",

    "doc_html": """
        Returns the control points count of a surface object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
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
            "type": "array",
            "doc": "The number of control points in the U and V directions if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 218,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

