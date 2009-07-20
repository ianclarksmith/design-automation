add_dim_style = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "add_dim_style",

    "doc_html": """
        Adds a new dimension style to the document.  The new dimension style will be initialized with the current default dimension style properties.
    """,

    "syntax_html": """
        Rhino.AddDimStyle ([strDimStyle])
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new dimension style.  If omitted, Rhino automatically generates the dimension style name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the new dimension style if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 455,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

