dim_style_text_gap = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleTextGap",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_text_gap",

    "doc_html": """
        Returns or changes the text gap used by a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleTextGap (strDimStyle [, dblGap])
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
            "name": "Gap",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new text gap.  If omitted, the current text gap is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a gap is not specified, the current text gap if successful."
        },
        1: {
            "type": "number",
            "doc": "If a gap is specified, the previous text gap if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 741,

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

