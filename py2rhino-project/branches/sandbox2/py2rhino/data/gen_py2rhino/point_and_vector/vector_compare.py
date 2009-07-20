vector_compare = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorCompare",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_compare",

    "doc_html": """
        Compares two 3-D vectors.
    """,

    "syntax_html": """
        Rhino.VectorCompare (arrVector1, arrVector2)
    """,

    "params_html": {
        0: {
            "name": "Vector1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first 3-D vector to compare.
            """
        },
        1: {
            "name": "Vector2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second 3-D vector to compare.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 613,

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

