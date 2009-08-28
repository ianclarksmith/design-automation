point_compare = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointCompare",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_compare",

    "doc_html": """
        Compares two 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoint1", "arrPoint2", "dblTolerance"),
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
        The first 3-D point to compare.
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
        The second 3-D point to compare.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The tolerance to use for the comparison. If omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 667,

    "params_com": {
        0: {
            "name": "vaPt0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

