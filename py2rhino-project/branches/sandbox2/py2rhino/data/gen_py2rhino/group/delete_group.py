delete_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "DeleteGroup",
    "output_package_name": "group",
    "output_module_name": "delete_group",

    "doc_html": """
        Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.
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
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 136,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

