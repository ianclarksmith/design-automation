invert_selected_objects = {
    "module_name": "selection",
    "class_name": "Selection",
    "method_name": "invert_selected_objects",

    "doc_html": """
        Inverts the current object selection.  The identifiers of the newly selected objects are returned.
    """,

    "syntax_html": """
        Rhino.InvertSelectedObjects ([blnIncludeLights [, blnIncludeGrips]])
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

