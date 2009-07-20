is_background_bitmap = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "is_background_bitmap",

    "doc_html": """
        Verifies that the specified view contains a background bitmap.
    """,

    "syntax_html": """
        Rhino.IsBackgroundBitmap (strView)
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 779,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

