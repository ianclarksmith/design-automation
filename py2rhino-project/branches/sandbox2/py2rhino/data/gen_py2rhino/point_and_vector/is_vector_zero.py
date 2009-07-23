is_vector_zero = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "IsVectorZero",
    "output_package_name": "point_and_vector",
    "output_module_name": "is_vector_zero",

    "doc_html": """
        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.
    """,

    "syntax_html": {
        0: ("arrVector"),
    },

    "params_html": {
        0: {
            "name": "arrVector",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector",
            "doc": """
        The 3-D vector to test.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the vector is zero, otherwise False, if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 611,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

