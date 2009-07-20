remove_object_from_top_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "RemoveObjectFromTopGroup",
    "output_package_name": "group",
    "output_module_name": "remove_object_from_top_group",

    "doc_html": """
        Removes a single object from it's top-most group.
    """,

    "syntax_html": """
        Rhino.RemoveObjectFromTopGroup (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

    "id_com": 143,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

