is_view_maximized = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "is_view_maximized",

    "doc_html": """
        Verifies that the specified view is maximized - enlarged so as to fill the entire Rhino window.
    """,

    "syntax_html": """
        Rhino.IsViewMaximized ([strView])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
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

    "id_com": 254,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

