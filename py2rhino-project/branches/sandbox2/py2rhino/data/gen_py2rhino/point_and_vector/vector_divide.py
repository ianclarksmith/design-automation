vector_divide = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorDivide",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_divide",

    "doc_html": """
        Divides a 3-D vectors by a value
    """,

    "syntax_html": {
        0: ("arrVector", "dblDivide"),
    },

    "params_html": {
        0: {
            "name": "arrVector",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector",
            "doc": """
        The 3-D vector to divide.
            """
        },
        1: {
            "name": "dblDivide",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Divide",
            "doc": """
        The a non-zero value to divide.
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

    "id_com": 625,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

