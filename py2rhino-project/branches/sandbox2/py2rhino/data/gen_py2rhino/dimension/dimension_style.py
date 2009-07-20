dimension_style = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dimension_style",

    "doc_html": """
        Returns or modifies the dimension style of a dimension object.
    """,

    "syntax_html": """
        Rhino.DimensionStyle (strObject [, strStyle]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Style",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strStyle is not specified, then the object's current dimension style if successful."
        },
        1: {
            "type": "string",
            "doc": "If strStyle is specified, then the object's previous dimension style if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 703,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

