dim_style_text_height = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dim_style_text_height",

    "doc_html": """
        Returns or changes the text height used by a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleTextHeight (strDimStyle [, dblHeight])
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "Height",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new text height.  If omitted, the current text height is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a height is not specified, the current text height if successful."
        },
        1: {
            "type": "number",
            "doc": "If a height is specified, the previous text height if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 465,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

