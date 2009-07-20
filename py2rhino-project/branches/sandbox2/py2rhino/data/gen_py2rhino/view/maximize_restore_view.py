maximize_restore_view = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "maximize_restore_view",

    "doc_html": """
        Toggles a view's maximized/restore window state of the specified view.
    """,

    "syntax_html": """
        Rhino.MaximizeRestoreView (strView)
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
    },

    "id_com": 257,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

