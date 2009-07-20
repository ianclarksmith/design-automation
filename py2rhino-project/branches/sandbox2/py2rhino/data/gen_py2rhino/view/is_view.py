is_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsView",
    "output_package_name": "view",
    "output_module_name": "is_view",

    "doc_html": """
        Verifies that the specified view exists.
    """,

    "syntax_html": """
        Rhino.IsView (strView)
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.
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

    "id_com": 252,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

