is_xform_zero = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "IsXformZero",
    "output_package_name": "transformation",
    "output_module_name": "is_xform_zero",

    "doc_html": """
        Verifies that a matrix is the zero transformation.
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
    """,

    "syntax_html": {
        0: ("arrXform"),
    },

    "params_html": {
        0: {
            "name": "arrXform",
            "py_name": "xform",
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
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 785,

    "params_com": {
        0: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

