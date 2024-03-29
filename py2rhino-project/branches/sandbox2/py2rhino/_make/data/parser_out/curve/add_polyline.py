add_polyline = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddPolyline",
    "output_package_name": "curve",
    "output_module_name": "add_polyline",

    "doc_html": """
        Adds a polyline curve object to the current model.
    """,

    "syntax_html": {
        0: ("arrPoints"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.  Duplicate, consecutive points found in the array will be removed.  The array must contain at least two 3-D points.  If the array contains less than four points, then the first point and the last point must be different.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 85,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

