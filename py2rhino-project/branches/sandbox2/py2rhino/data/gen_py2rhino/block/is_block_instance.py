is_block_instance = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "IsBlockInstance",
    "output_package_name": "block",
    "output_module_name": "is_block_instance",

    "doc_html": """
        Verifies an object is a block instance.
    """,

    "syntax_html": """
        Rhino.IsBlockInstance (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an existing block definition.
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

    "id_com": 420,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

