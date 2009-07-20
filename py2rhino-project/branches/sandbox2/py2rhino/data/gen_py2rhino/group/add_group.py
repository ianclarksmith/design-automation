add_group = {
    "module_name": "group",
    "class_name": "Group",
    "method_name": "add_group",

    "doc_html": """
        Adds a new empty group to the document.
    """,

    "syntax_html": """
        Rhino.AddGroup ([strGroup])
    """,

    "params_html": {
        0: {
            "name": "Group",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new group.  If omitted, Rhino automatically generates the group name.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the new group if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 133,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

