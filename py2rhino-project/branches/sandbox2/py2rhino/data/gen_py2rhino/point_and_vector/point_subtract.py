point_subtract = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointSubtract",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_subtract",

    "doc_html": """
        Subtracts a 3-D point or a 3-D vector from a 3-D point.
    """,

    "syntax_html": """
        Rhino.PointSubtract (arrPoint1, arrPoint2)
    """,

    "params_html": {
        0: {
            "name": "Point1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point to subtract from.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point or a 3-D vector to subtract.
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

    "id_com": 670,

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
