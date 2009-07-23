rename_block = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "RenameBlock",
    "output_package_name": "block",
    "output_module_name": "rename_block",

    "doc_html": """
        Renames an existing block definition.
    """,

    "syntax_html": {
        0: ("strOldBlock", "strNewBlock"),
    },

    "params_html": {
        0: {
            "name": "strOldBlock",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "OldBlock",
            "doc": """
        The name of an existing block definition.
            """
        },
        1: {
            "name": "strNewBlock",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "NewBlock",
            "doc": """
        The new block definition name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The new block definition name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 399,

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

