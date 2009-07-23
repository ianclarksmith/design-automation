is_object_locked = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectLocked",
    "output_package_name": "object",
    "output_module_name": "is_object_locked",

    "doc_html": """
        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
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
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 48,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

