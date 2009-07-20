rename_group = {
    "module_name": "group",
    "class_name": "Group",
    "method_name": "rename_group",

    "doc_html": """
        Renames an existing group.
    """,

    "syntax_html": """
        Rhino.RenameGroup (strOldGroup, strNewGroup)
    """,

    "params_html": {
        0: {
            "name": "OldGroup",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing group.
            """
        },
        1: {
            "name": "NewGroup",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

