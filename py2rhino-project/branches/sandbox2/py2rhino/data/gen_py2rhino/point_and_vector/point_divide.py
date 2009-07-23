point_divide = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointDivide",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_divide",

    "doc_html": """
        Divides a 3-D point by a value
    """,

    "syntax_html": {
        0: ("arrPoint", "dblDivide"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The 3-D point to divide.
            """
        },
        1: {
            "name": "dblScale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The a non-zero value to divide.
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

    "id_com": 668,

    "params_com": {
        0: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDivide",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

