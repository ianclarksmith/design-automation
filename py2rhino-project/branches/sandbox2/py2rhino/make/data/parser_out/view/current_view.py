current_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "CurrentView",
    "output_package_name": "view",
    "output_module_name": "current_view",

    "doc_html": """
        Returns or sets the currently active view.
    """,

    "syntax_html": {
        0: ("strView", "bReturnName"),
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
        The title or identifier of the view to set current.  If omitted, only the title or identifier of the current view is returned.
            """
        },
        1: {
            "name": "blnReturnName",
            "py_name": "return_name",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnName",
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

