add_object_to_group = {
    "module_name": "group",
    "class_name": "Group",
    "method_name": "add_object_to_group",

    "doc_html": """
        Adds a single object to an existing group. Neither the object nor the group can be reference objects.
    """,

    "syntax_html": """
        Rhino.AddObjectToGroup (strObject, strGroup)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to add to the group.
            """
        },
        1: {
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
            "type": "boolean",
            "doc": "True or False indicating success or failure"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 134,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

