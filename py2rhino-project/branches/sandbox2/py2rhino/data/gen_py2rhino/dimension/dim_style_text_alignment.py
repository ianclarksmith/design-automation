dim_style_text_alignment = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dim_style_text_alignment",

    "doc_html": """
        Returns or changes the text alignment mode of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleTextAlignment (strDimStyle [, intAlignment])
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
            "name": "Alignment",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new text alignment.  If omitted, the current text alignment is returned.  The text alignment values are as follows:
		Value
		Description
		0
		Normal (same as 2)
		1
		Horizontal to view
		2
		Above the dimension line
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a mode is not specified, the current text alignment mode  if successful."
        },
        1: {
            "type": "number",
            "doc": "If a mode is specified, the previous text alignment mode if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 461,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAlignment",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

