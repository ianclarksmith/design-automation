view_size = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "view_size",

    "doc_html": """
        Returns the width and height in pixels of the specified view.
    """,

    "syntax_html": """
        Rhino.ViewSize ([strView])
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
            "type": "array",
            "doc": "A zero-based, one-dimensional array containing two numbers identifying the width and height if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 267,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

