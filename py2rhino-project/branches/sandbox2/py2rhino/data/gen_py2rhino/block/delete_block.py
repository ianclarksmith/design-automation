delete_block = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "DeleteBlock",
    "output_package_name": "block",
    "output_module_name": "delete_block",

    "doc_html": """
        Deletes a block definition and all of it's inserted instances.
    """,

    "syntax_html": """
        Rhino.DeleteBlock (strBlock)
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

    "id_com": 418,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

