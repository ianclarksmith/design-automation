delete_dim_style = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DeleteDimStyle",
    "output_package_name": "dimension",
    "output_module_name": "delete_dim_style",

    "doc_html": """
        Removes an existing dimension style from the document.  The dimension style to be removed cannot be the reference by any dimension objects.
    """,

    "syntax_html": {
        0: ("strDimStyle"),
    },

    "params_html": {
        0: {
            "name": "strDimStyle",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "DimStyle",
            "doc": """
        The name of an un-referenced dimension style.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the deleted dimension style if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 456,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

