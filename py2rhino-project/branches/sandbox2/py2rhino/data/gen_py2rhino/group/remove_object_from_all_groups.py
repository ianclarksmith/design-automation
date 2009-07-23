remove_object_from_all_groups = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "RemoveObjectFromAllGroups",
    "output_package_name": "group",
    "output_module_name": "remove_object_from_all_groups",

    "doc_html": """
        Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object.
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

    "id_com": 141,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

