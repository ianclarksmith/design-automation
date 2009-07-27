view_title = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewTitle",
    "output_package_name": "view",
    "output_module_name": "view_title",

    "doc_html": """
        Returns the name, or title, of a view given a view's identifier.
    """,

    "syntax_html": {
        0: ("strView"),
    },

    "params_html": {
        0: {
            "name": "strMode",
            "py_name": "mode",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mode",
            "doc": """
        The identifier of the display mode obtained from the ViewNames method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name, or title, of the view if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 907,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

