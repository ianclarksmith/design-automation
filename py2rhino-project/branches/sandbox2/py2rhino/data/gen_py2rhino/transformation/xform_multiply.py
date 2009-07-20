xform_multiply = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_multiply",

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
            "type_string": "arr",
            "doc": """
        The first 4x4 transformation matrix to multiply.
            """
        },
        1: {
            "name": "Xform2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

