is_block = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "IsBlock",
    "output_package_name": "block",
    "output_module_name": "is_block",

    "doc_html": """
        Verifies the existence of a block definition in the document.
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
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 398,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

