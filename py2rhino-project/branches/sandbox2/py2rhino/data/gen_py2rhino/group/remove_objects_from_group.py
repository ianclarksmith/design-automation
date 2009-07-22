remove_objects_from_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "RemoveObjectsFromGroup",
    "output_package_name": "group",
    "output_module_name": "remove_objects_from_group",

    "doc_html": """
        Removes one or more objects from an existing group.
    """,

    "syntax_html": """
        Rhino.RemoveObjectsFromGroup (arrObjects, strGroup)
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of object identifiers.
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
            "type": "number",
            "doc": "The number of objects removed from the group if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 144,

    "params_com": {
        0: {
            "name": "vaObjects",
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

