block_u_r_l_tag = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "BlockURLTag",
    "output_package_name": "block",
    "output_module_name": "block_u_r_l_tag",

    "doc_html": """
        Returns or sets the URL tag, or description, of a block definition.
    """,

    "syntax_html": {
        0: ("strBlock", "strURLTag"),
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
        1: {
            "name": "strURL",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "URL",
            "doc": """
        The new URL tag.  If omitted, the current URL tag is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a URL tag is not specified,  the current URL tag if successful."
        },
        1: {
            "type": "string",
            "doc": "If a URL tag is specified, the previous URL tag if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 403,

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

