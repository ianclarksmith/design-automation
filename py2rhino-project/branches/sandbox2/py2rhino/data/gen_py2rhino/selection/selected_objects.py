selected_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "SelectedObjects",
    "output_package_name": "selection",
    "output_module_name": "selected_objects",

    "doc_html": """
        Returns the identifiers of all objects that are currently selected.
    """,

    "syntax_html": """
        Rhino.SelectedObjects ([blnIncludeLights [, blnIncludeGrips]])
    """,

    "params_html": {
        0: {
            "name": "IncludeLights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
            """
        },
        1: {
            "name": "IncludeGrips",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Include grips objects.  If omitted, grips objects are not returned (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 43,

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

