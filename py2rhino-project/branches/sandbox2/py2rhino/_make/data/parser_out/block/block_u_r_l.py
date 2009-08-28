block_u_r_l = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockURL",
    "output_package_name": "block",
    "output_module_name": "block_u_r_l",

    "doc_html": """
        Returns or sets the URL of a block definition.
    """,

    "syntax_html": {
        0: ("strBlock", "strURL"),
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
            "name": "strURL",
            "py_name": "u_r_l",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "URL",
            "doc": """
        The new URL.  If omitted, the current URL is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a URL is not specified,  the current URL if successful."
        },
        1: {
            "type": "string",
            "doc": "If a URL is specified, the previous URL if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 402,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNew",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

