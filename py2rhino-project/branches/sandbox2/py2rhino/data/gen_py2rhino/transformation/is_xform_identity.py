is_xform_identity = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "is_xform_identity",

    "doc_html": """
        Verifies that a matrix is the identity transformation.
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
    """,

    "syntax_html": """
        Rhino.IsXformIdentity (arrXform)
    """,

    "params_html": {
        0: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

    "id_com": 786,

    "params_com": {
        0: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

