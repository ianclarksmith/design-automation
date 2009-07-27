lock_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "LockObjects",
    "output_package_name": "object",
    "output_module_name": "lock_objects",

    "doc_html": """
        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": {
        0: ("arrObjects"),
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
        An array of strings identifying the objects to lock.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects locked if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 304,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

