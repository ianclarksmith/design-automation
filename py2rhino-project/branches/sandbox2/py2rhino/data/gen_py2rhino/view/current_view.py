current_view = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "current_view",

    "doc_html": """
        Returns or sets the currently active view.
    """,

    "syntax_html": """
        Rhino.CurrentView ([strView [, bReturnName]])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view to set current.  If omitted, only the title or identifier of the current view is returned.
            """
        },
        1: {
            "name": "ReturnName",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), then the name, or title, of the view is returned. If False, then the identifier of the view is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If the title is not specified, the title or identifier of the current view if successful."
        },
        1: {
            "type": "string",
            "doc": "If the title is specified, the title or identifier of the previous current view is successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 251,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

