add_dim_style = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "AddDimStyle",
    "output_package_name": "dimension",
    "output_module_name": "add_dim_style",

    "doc_html": """
        Adds a new dimension style to the document.  The new dimension style will be initialized with the current default dimension style properties.
    """,

    "syntax_html": {
        0: ("strDimStyle"),
    },

    "params_html": {
        0: {
            "name": "strDimStyle",
            "py_name": "dim_style",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "DimStyle",
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

