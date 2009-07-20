dim_style_extension = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleExtension",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_extension",

    "doc_html": """
        Returns or changes the extension line extension of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleExtension (strDimStyle [, dblExtension])
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
            "name": "Extension",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new extension line extension.  If omitted, the current extension line extension is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If an extension is not specified, the current extension line extension if successful."
        },
        1: {
            "type": "number",
            "doc": "If an extension is specified, the previous extension line extension if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 466,

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

