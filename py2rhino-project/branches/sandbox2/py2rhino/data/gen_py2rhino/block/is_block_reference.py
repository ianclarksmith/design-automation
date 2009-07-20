is_block_reference = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "IsBlockReference",
    "output_package_name": "block",
    "output_module_name": "is_block_reference",

    "doc_html": """
        Verifies that a block definition is from a reference file.
    """,

    "syntax_html": """
        Rhino.IsBlockReference (strBlock)
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

    "id_com": 407,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

