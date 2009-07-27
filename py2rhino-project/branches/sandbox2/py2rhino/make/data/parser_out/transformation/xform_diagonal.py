xform_diagonal = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformDiagonal",
    "output_package_name": "transformation",
    "output_module_name": "xform_diagonal",

    "doc_html": """
        Returns a diagonal  transformation matrix. Diagonal matrices are 3x3 with the bottom row = 0,0,0,1.
		d
		0
		0
		0
		0
		d
		0
		0
		0
		0
		d
		0
		0
		0
		0
		1
    """,

    "syntax_html": {
        0: ("dblValue"),
    },

    "params_html": {
        0: {
            "name": "dblValue",
            "py_name": "value",
            "opt_or_req": "Required",
            "type": "number",
            "name_prefix": "dbl",
            "name_main": "Value",
            "doc": """
        The diagonal value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 784,

    "params_com": {
        0: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

