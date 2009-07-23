show_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ShowObjects",
    "output_package_name": "object",
    "output_module_name": "show_objects",

    "doc_html": """
        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
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
        An array of strings identifying the objects to show.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects shown if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 305,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

