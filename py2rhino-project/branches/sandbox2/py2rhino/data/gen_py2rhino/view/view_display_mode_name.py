view_display_mode_name = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_display_mode_name",

    "doc_html": """
        Returns the name of a display mode given a display mode's identifier.
    """,

    "syntax_html": """
        Rhino.ViewDisplayModeName (strMode])
    """,

    "params_html": {
        0: {
            "name": "Mode",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the display mode obtained from the ViewDisplayModes method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the display mode if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 909,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

