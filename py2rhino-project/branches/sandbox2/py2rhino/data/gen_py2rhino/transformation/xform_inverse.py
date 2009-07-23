xform_inverse = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformInverse",
    "output_package_name": "transformation",
    "output_module_name": "xform_inverse",

    "doc_html": """
        Returns the inverse of a non-singular transformation matrix.
    """,

    "syntax_html": {
        0: ("arrXform"),
    },

    "params_html": {
        0: {
            "name": "arrXform",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xform",
            "doc": """
        A 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The inverted 4x4 transformation matrix if successful."
        },
        1: {
            "type": "null",
            "doc": "If matrix is non-singular, On error."
        },
    },

    "id_com": 817,

    "params_com": {
        0: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

