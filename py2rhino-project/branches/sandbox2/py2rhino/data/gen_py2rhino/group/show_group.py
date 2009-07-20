show_group = {
    "module_name": "group",
    "class_name": "Group",
    "method_name": "show_group",

    "doc_html": """
        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": """
        Rhino.ShowGroup (strGroup)
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
            "doc": "The number of object that were shown if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 872,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

