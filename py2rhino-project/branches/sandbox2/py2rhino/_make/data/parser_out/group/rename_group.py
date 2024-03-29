rename_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "RenameGroup",
    "output_package_name": "group",
    "output_module_name": "rename_group",

    "doc_html": """
        Renames an existing group.
    """,

    "syntax_html": {
        0: ("strOldGroup", "strNewGroup"),
    },

    "params_html": {
        0: {
            "name": "strOldGroup",
            "py_name": "old_group",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "OldGroup",
            "doc": """
        The name of an existing group.
            """
        },
        1: {
            "name": "strNewGroup",
            "py_name": "new_group",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "NewGroup",
            "doc": """
        The new group name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The new group name if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 145,

    "params_com": {
        0: {
            "name": "vaOld",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNew",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

