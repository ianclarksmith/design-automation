unselect_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "UnselectObjects",
    "output_package_name": "object",
    "output_module_name": "unselect_objects",

    "doc_html": """
        Unselects one or more selected objects.
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
        An array of strings identifying the objects to unselect.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects unselected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 300,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

