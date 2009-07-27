is_object_selectable = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectSelectable",
    "output_package_name": "object",
    "output_module_name": "is_object_selectable",

    "doc_html": """
        Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.
    """,

    "syntax_html": {
        0: ("strObject"),
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

    "id_com": 307,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

