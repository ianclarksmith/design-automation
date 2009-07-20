vector_divide = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorDivide",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_divide",

    "doc_html": """
        Divides a 3-D vectors by a value
    """,

    "syntax_html": """
        Rhino.VectorDivide (arrVector, dblDivide)
    """,

    "params_html": {
        0: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D vector to divide.
            """
        },
        1: {
            "name": "Divide",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
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

