is_dim_style = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "IsDimStyle",
    "output_package_name": "dimension",
    "output_module_name": "is_dim_style",

    "doc_html": """
        Verifies the existence of a dimension style in the document.
    """,

    "syntax_html": """
        Rhino.IsDimStyle (strDimStyle)
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a dimension style to test.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 454,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

