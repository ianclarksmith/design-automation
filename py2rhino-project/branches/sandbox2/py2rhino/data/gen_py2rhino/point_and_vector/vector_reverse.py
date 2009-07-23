vector_reverse = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorReverse",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_reverse",

    "doc_html": """
        Reverses the direction of a 3-D vector.
    """,

    "syntax_html": {
        0: ("arrVector"),
    },

    "params_html": {
        0: {
            "name": "arrVector",
            "py_name": "vector",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector",
            "doc": """
        The 3-D vector.
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

    "id_com": 618,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

