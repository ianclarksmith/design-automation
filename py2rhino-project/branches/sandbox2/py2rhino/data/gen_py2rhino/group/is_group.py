is_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "IsGroup",
    "output_package_name": "group",
    "output_module_name": "is_group",

    "doc_html": """
        Verifies the existence of a group.
    """,

    "syntax_html": {
        0: ("strGroup"),
    },

    "params_html": {
        0: {
            "name": "strGroup",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Group",
            "doc": """
        The name of an existing group.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 139,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

