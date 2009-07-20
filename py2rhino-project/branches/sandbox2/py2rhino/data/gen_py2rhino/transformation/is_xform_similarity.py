is_xform_similarity = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "is_xform_similarity",

    "doc_html": """
        Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.
    """,

    "syntax_html": """
        Rhino.IsXformSimilarity (arrXform)
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
            "doc": "True if this transformation is an orientation preserving similarity, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 787,

    "params_com": {
        0: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

