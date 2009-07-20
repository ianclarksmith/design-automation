current_dim_style = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "current_dim_style",

    "doc_html": """
        Returns or changes the current default dimension style.
    """,

    "syntax_html": """
        Rhino.CurrentDimStyle ([strDimStyle])
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style to make current.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a dimension style is not specified, the name of the current dimension style if successful."
        },
        1: {
            "type": "string",
            "doc": "If a dimension style is specified, the name of the previous current dimension style if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 453,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

