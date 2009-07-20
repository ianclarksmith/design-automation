rename_dim_style = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "rename_dim_style",

    "doc_html": """
        Renames an existing dimension style.
    """,

    "syntax_html": """
        Rhino.RenameDimStyle (strOldStyle, strNewStyle)
    """,

    "params_html": {
        0: {
            "name": "OldStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "NewStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new dimension style name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The new dimension style name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 458,

    "params_com": {
        0: {
            "name": "vaOld",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNew",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

