vector_create = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorCreate",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_create",

    "doc_html": """
        Creates a vector from two 3-D points.
    """,

    "syntax_html": {
        0: ("arrPoint1", "arrPoint2"),
    },

    "params_html": {
        0: {
            "name": "arrPoint1",
            "py_name": "point1",
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
            "py_name": "point2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point2",
            "doc": """
        The second 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D vector if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 614,

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
    },

    "returns_com": "tagVARIANT",

}

