distance = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "Distance",
    "output_package_name": "math",
    "output_module_name": "distance",

    "doc_html": """
        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoint1", "arrPoint2"),
        1: ("arrPoint1", "arrPointArray"),
    },

    "params_html": {
        0: {
            "name": "arrPoint1",
            "py_name": "point_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point1",
            "doc": """
        The first 3-D point.
            """
        },
        1: {
            "name": "arrPoint2",
            "py_name": "point_2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point2",
            "doc": """
        The second 3-D point.
            """
        },
        2: {
            "name": "arrPointArray",
            "py_name": "point_array",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "PointArray",
            "doc": """
        An array of 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If arrPoint1 and arrPoint2 are specified, then the distance is successful."
        },
        1: {
            "type": "array",
            "doc": "If arrPoint1 and arrPointArray are specified, then an array of distances if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 118,

    "params_com": {
        0: {
            "name": "vaFrom",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTo",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

