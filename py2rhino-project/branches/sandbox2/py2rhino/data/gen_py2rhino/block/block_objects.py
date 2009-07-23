block_objects = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockObjects",
    "output_package_name": "block",
    "output_module_name": "block_objects",

    "doc_html": """
        Returns the identifiers of the objects that make up a block definition.
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
            "doc": "An array of strings identifying the objects that make up a block definition if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 417,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

