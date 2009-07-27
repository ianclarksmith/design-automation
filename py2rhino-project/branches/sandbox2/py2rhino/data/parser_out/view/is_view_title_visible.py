is_view_title_visible = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsViewTitleVisible",
    "output_package_name": "view",
    "output_module_name": "is_view_title_visible",

    "doc_html": """
        Verifies that the specified view's title window is visible.
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
        The title or identifier of the view.  If omitted, the current active view is omitted.
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

    "id_com": 256,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

