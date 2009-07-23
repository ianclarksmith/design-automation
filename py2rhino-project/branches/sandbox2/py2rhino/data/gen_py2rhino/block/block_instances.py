block_instances = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockInstances",
    "output_package_name": "block",
    "output_module_name": "block_instances",

    "doc_html": """
        Returns the identifiers of the inserted instances of a block.
    """,

    "syntax_html": {
        0: ("strBlock"),
    },

    "params_html": {
        0: {
            "name": "strBlock",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Block",
            "doc": """
        The name of an existing block definition.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the instances of a block if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 414,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

