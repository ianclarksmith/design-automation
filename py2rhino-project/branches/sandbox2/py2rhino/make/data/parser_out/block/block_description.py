block_description = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockDescription",
    "output_package_name": "block",
    "output_module_name": "block_description",

    "doc_html": """
        Returns or sets the description of a block definition.
    """,

    "syntax_html": {
        0: ("strBlock", "strText"),
    },

    "params_html": {
        0: {
            "name": "strBlock",
            "py_name": "block",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Block",
            "doc": """
        The name of an existing block definition.
            """
        },
        1: {
            "name": "strText",
            "py_name": "text",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        The new description.  If omitted, the current description is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a description is not specified,  the current description if successful."
        },
        1: {
            "type": "string",
            "doc": "If a description is specified, the previous description if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 400,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDesc",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

