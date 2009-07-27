is_group_empty = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "IsGroupEmpty",
    "output_package_name": "group",
    "output_module_name": "is_group_empty",

    "doc_html": """
        Verifies that an existing group is empty, or contains no object members.
    """,

    "syntax_html": {
        0: ("strGroup"),
    },

    "params_html": {
        0: {
            "name": "strGroup",
            "py_name": "group",
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

    "id_com": 140,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

