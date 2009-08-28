add_object_to_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "AddObjectToGroup",
    "output_package_name": "group",
    "output_module_name": "add_object_to_group",

    "doc_html": """
        Adds a single object to an existing group. Neither the object nor the group can be reference objects.
    """,

    "syntax_html": {
        0: ("strObject", "strGroup"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object to add to the group.
            """
        },
        1: {
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

