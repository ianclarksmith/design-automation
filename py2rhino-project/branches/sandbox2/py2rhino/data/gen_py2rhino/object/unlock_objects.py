unlock_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "UnlockObjects",
    "output_package_name": "object",
    "output_module_name": "unlock_objects",

    "doc_html": """
        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": {
        0: ("arrObjects"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to unlock.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects unlocked if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 306,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

