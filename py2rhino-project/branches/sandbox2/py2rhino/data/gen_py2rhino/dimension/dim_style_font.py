dim_style_font = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleFont",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_font",

    "doc_html": """
        Returns or changes the font used by a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleFont (strDimStyle [, strFont])
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
            "name": "Font",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new font face name.  If omitted, the current font is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a font is not specified, the current font if successful."
        },
        1: {
            "type": "string",
            "doc": "If a font is specified, the previous font if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 462,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFont",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

