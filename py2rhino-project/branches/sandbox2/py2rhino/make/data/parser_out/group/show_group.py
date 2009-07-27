show_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "ShowGroup",
    "output_package_name": "group",
    "output_module_name": "show_group",

    "doc_html": """
        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": {
        0: ("strGroup"),
    },

    "params_html": {
        0: {
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

