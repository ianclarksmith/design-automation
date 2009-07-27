dim_style_text_height = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleTextHeight",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_text_height",

    "doc_html": """
        Returns or changes the text height used by a dimension style.
    """,

    "syntax_html": {
        0: ("strDimStyle", "dblHeight"),
    },

    "params_html": {
        0: {
            "name": "strDimStyle",
            "py_name": "dim_style",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "DimStyle",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "dblHeight",
            "py_name": "height",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Height",
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

