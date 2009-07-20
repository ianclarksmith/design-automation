xform_translation = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_translation",

    "doc_html": """
        Creates a translation transformation matrix.
    """,

    "syntax_html": """
        Rhino.XformTranslation (arrVector)
    """,

    "params_html": {
        0: {
            "name": "Vector",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D translation vector.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 792,

    "params_com": {
        0: {
            "name": "vaVector",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

