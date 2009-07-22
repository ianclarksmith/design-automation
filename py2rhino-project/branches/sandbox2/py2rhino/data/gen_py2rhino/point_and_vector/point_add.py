point_add = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointAdd",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_add",

    "doc_html": """
        Adds a 3-D point or a 3-D vector to a 3-D point.
    """,

    "syntax_html": """
        Rhino.PointAdd (arrPoint1, arrPoint2)
    """,

    "params_html": {
        0: {
            "name": "Point1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D point to add to.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D point or a 3-D vector to add.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 666,

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

