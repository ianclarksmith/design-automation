block_path = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockPath",
    "output_package_name": "block",
    "output_module_name": "block_path",

    "doc_html": """
        Returns the path to the source of a linked or embedded block definition.  A linked or embedded block definition is a block definition that was inserted from an external file.
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
            "type": "string",
            "doc": "The path to the linked block file is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 408,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

