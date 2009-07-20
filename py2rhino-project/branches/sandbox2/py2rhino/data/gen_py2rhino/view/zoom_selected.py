zoom_selected = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "zoom_selected",

    "doc_html": """
        Zooms to the extents of selected objects in the specified view, or in the active view.
    """,

    "syntax_html": """
        Rhino.ZoomSelected ([strView [, blnAll]])
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
        1: {
            "name": "All",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Zoom selected in all views.  If omitted, only the specified view is zoomed (False).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 376,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAll",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

