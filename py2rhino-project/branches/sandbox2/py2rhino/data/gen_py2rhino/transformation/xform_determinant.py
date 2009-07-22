xform_determinant = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformDeterminant",
    "output_package_name": "transformation",
    "output_module_name": "xform_determinant",

    "doc_html": """
        Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.
    """,

    "syntax_html": """
        Rhino.XformDeterminant (arrXform)
    """,

    "params_html": {
        0: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The determinant if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 818,

    "params_com": {
        0: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

