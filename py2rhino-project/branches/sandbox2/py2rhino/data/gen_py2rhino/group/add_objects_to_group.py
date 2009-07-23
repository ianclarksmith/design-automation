add_objects_to_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "AddObjectsToGroup",
    "output_package_name": "group",
    "output_module_name": "add_objects_to_group",

    "doc_html": """
        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.
    """,

    "syntax_html": {
        0: ("arrObjects", "strGroup"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of object identifiers.
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
            "type": "number",
            "doc": "The number of objects added to the group if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 135,

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

