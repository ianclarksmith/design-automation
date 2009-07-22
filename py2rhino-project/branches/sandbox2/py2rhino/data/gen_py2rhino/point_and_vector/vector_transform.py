vector_transform = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "VectorTransform",
    "output_package_name": "point_and_vector",
    "output_module_name": "vector_transform",

    "doc_html": """
        Transforms a 3-D vector.
    """,

    "syntax_html": """
        Rhino.VectorTransform (arrVector, arrXform)
    """,

    "params_html": {
        0: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D vector to transform.
            """
        },
        1: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A valid 4x4 transformation matrix.
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

    "id_com": 800,

    "params_com": {
        0: {
            "name": "vaVector",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

