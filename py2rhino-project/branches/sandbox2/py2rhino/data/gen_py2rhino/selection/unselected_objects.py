unselected_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "UnselectedObjects",
    "output_package_name": "selection",
    "output_module_name": "unselected_objects",

    "doc_html": """
        Returns the identifiers of all objects that are currently unselected.
    """,

    "syntax_html": """
        Rhino.UnselectedObjects ([blnSelect [, blnIncludeLights [, blnIncludeGrips]]])
    """,

    "params_html": {
        0: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the objects.  If omitted, the object is not selected (False).
            """
        },
        1: {
            "name": "IncludeLights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
            """
        },
        2: {
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

    "id_com": 45,

    "params_com": {
        0: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIncludeLights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaIncludeGrips",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

