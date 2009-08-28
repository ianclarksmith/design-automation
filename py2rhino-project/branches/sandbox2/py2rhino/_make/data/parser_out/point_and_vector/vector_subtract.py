vector_subtract = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorSubtract",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_subtract",

    "doc_html": """
        Subtracts two 3-D vectors.
    """,

    "syntax_html": {
        0: ("arrVector1", "arrVector2"),
    },

    "params_html": {
        0: {
            "name": "arrVector1",
            "py_name": "vector_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector1",
            "doc": """
        The 3-D vector to subtract from.
            """
        },
        1: {
            "name": "arrVector2",
            "py_name": "vector_2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector2",
            "doc": """
        The 3-D vector to subtract.
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

    "id_com": 620,

    "params_com": {
        0: {
            "name": "vaVec0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaVec1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

