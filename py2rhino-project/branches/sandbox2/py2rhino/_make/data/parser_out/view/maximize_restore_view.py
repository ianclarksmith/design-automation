maximize_restore_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "MaximizeRestoreView",
    "output_package_name": "view",
    "output_module_name": "maximize_restore_view",

    "doc_html": """
        Toggles a view's maximized/restore window state of the specified view.
    """,

    "syntax_html": {
        0: ("strView"),
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

