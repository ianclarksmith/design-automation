hide_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "HideObjects",
    "output_package_name": "object",
    "output_module_name": "hide_objects",

    "doc_html": """
        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": """
        Rhino.HideObjects (arrObjects)
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of strings identifying the objects to hide.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects hidden if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 303,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

