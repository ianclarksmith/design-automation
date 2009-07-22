xform_multiply = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformMultiply",
    "output_package_name": "transformation",
    "output_module_name": "xform_multiply",

    "doc_html": """
        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.
    """,

    "syntax_html": """
        Rhino.XformMultiply (arrXform1, arrXform2)
    """,

    "params_html": {
        0: {
            "name": "Xform1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The first 4x4 transformation matrix to multiply.
            """
        },
        1: {
            "name": "Xform2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

