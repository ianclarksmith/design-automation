brep_closest_point = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "BrepClosestPoint",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "brep_closest_point",

    "doc_html": """
        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint"),
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
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The test, or sampling, point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of closest point information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 514,

    "params_com": {
        0: {
            "name": "vaBrep",
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

