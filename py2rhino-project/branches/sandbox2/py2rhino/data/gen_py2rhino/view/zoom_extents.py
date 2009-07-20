zoom_extents = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ZoomExtents",
    "output_package_name": "view",
    "output_module_name": "zoom_extents",

    "doc_html": """
        Zooms to the extents of visible objects in the specified view, or in the active view.
    """,

    "syntax_html": """
        Rhino.ZoomExtents ([strView [, blnAll]])
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
        Zoom extents in all views.  If omitted, only the specified view is zoomed (False).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 375,

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

