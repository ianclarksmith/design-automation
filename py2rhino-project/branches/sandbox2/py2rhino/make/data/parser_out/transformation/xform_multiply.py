xform_multiply = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformMultiply",
    "output_package_name": "transformation",
    "output_module_name": "xform_multiply",

    "doc_html": """
        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.
    """,

    "syntax_html": {
        0: ("arrXform1", "arrXform2"),
    },

    "params_html": {
        0: {
            "name": "arrXform1",
            "py_name": "xform_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xform1",
            "doc": """
        The first 4x4 transformation matrix to multiply.
            """
        },
        1: {
            "name": "arrXform2",
            "py_name": "xform_2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xform2",
            "doc": """
        The second 4x4 transformation matrix to multiply.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 788,

    "params_com": {
        0: {
            "name": "vaXform0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

