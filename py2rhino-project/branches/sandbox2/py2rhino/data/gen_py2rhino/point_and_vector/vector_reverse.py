vector_reverse = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorReverse",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_reverse",

    "doc_html": """
        Reverses the direction of a 3-D vector.
    """,

    "syntax_html": """
        Rhino.VectorReverse (arrVector)
    """,

    "params_html": {
        0: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

