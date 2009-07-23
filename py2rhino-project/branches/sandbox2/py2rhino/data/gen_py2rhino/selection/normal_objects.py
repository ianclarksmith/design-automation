normal_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "NormalObjects",
    "output_package_name": "selection",
    "output_module_name": "normal_objects",

    "doc_html": """
        Returns the identifiers of all normal objects in the document.  Normal objects are visible, can be snapped to, and are independent of selection state.
    """,

    "syntax_html": {
        0: ("blnIncludeLights", "blnIncludeGrips"),
    },

    "params_html": {
        0: {
            "name": "blnIncludeLights",
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
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 364,

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

