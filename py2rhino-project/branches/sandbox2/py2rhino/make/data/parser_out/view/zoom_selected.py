zoom_selected = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ZoomSelected",
    "output_package_name": "view",
    "output_module_name": "zoom_selected",

    "doc_html": """
        Zooms to the extents of selected objects in the specified view, or in the active view.
    """,

    "syntax_html": {
        0: ("strView", "blnAll"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "blnAll",
            "py_name": "all",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "All",
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

