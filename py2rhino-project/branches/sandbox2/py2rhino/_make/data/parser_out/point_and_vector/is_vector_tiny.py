is_vector_tiny = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "IsVectorTiny",
    "output_package_name": "point_and_vector",
    "output_module_name": "is_vector_tiny",

    "doc_html": """
        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.
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
        The 3-D vector to test.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the vector is tiny, otherwise False, if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 610,

    "params_com": {
        0: {
            "name": "vaVec",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

