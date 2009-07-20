is_view_perspective = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsViewPerspective",
    "output_package_name": "view",
    "output_module_name": "is_view_perspective",

    "doc_html": """
        Verifies that the specified view's projection is set to perspective.
    """,

    "syntax_html": """
        Rhino.IsViewPerspective (strView)
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

    "id_com": 255,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

