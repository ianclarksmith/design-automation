lock_group = {
    "module_name": "group",
    "class_name": "Group",
    "method_name": "lock_group",

    "doc_html": """
        Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": """
        Rhino.LockGroup (strGroup)
    """,

    "params_html": {
        0: {
            "name": "Group",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing group.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of object that were locked if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 873,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

