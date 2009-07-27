is_dim_style_reference = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "IsDimStyleReference",
    "output_package_name": "dimension",
    "output_module_name": "is_dim_style_reference",

    "doc_html": """
        Verifies that an existing dimension style is from a reference file.
    """,

    "syntax_html": {
        0: ("strDimStyle"),
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
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 457,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

