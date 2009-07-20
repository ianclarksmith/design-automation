show_view_title = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ShowViewTitle",
    "output_package_name": "view",
    "output_module_name": "show_view_title",

    "doc_html": """
        Shows or hides the title window of a view.
    """,

    "syntax_html": """
        Rhino.ShowViewTitle ([strView [, blnState]])
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
            "name": "State",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The visible state of the view's title window.  If omitted, the title will be shown (True).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 261,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

