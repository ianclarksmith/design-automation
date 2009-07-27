select_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "SelectObjects",
    "output_package_name": "object",
    "output_module_name": "select_objects",

    "doc_html": """
        Selects one or more objects.
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
        An array of strings identifying the objects to select.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects selected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 298,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

