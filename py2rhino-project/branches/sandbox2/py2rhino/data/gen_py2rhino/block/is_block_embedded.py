is_block_embedded = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "IsBlockEmbedded",
    "output_package_name": "block",
    "output_module_name": "is_block_embedded",

    "doc_html": """
        Verifies that a block definition is embedded, or linked, from an external file.
    """,

    "syntax_html": """
        Rhino.IsBlockEmbedded (strBlock)
    """,

    "params_html": {
        0: {
            "name": "Block",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing block definition.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 405,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

