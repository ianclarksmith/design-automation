invert_selected_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "InvertSelectedObjects",
    "output_package_name": "selection",
    "output_module_name": "invert_selected_objects",

    "doc_html": """
        Inverts the current object selection.  The identifiers of the newly selected objects are returned.
    """,

    "syntax_html": {
        0: ("blnIncludeLights", "blnIncludeGrips"),
    },

    "params_html": {
        0: {
            "name": "blnIncludeLights",
            "py_name": "include_lights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IncludeLights",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
            """
        },
        1: {
            "name": "blnIncludeGrips",
            "py_name": "include_grips",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IncludeGrips",
            "doc": """
        Include grips objects.  If omitted, grips objects are not returned (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly selected objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 34,

    "params_com": {
        0: {
            "name": "vaIncludeLights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIncludeGrips",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

