unlock_group = {
    "input_folder_name": "Group_Methods",
    "input_file_name": "UnlockGroup",
    "output_package_name": "group",
    "output_module_name": "unlock_group",

    "doc_html": """
        Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": """
        Rhino.UnlockGroup (strGroup)
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
            "doc": "The number of object that were unlocked if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 874,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

