is_point_in_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsPointInSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_point_in_surface",

    "doc_html": """
        Verifies that a point is inside a closed surface or polysurface.
    """,

    "syntax_html": """
        Rhino.IsPointInSurface (strObject, arrPoint)
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
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The test, or sampling, point.
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

    "id_com": 443,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

