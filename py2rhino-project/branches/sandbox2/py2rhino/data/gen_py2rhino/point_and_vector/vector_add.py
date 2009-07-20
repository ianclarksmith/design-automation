vector_add = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "vector_add",

    "doc_html": """
        Adds two 3-D vectors.
    """,

    "syntax_html": """
        Rhino.VectorAdd (arrVector1, arrVector2)
    """,

    "params_html": {
        0: {
            "name": "Vector1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D vector to add to.
            """
        },
        1: {
            "name": "Vector2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D vector to add.
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

    "id_com": 612,

    "params_com": {
        0: {
            "name": "vaVec0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaVec1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

