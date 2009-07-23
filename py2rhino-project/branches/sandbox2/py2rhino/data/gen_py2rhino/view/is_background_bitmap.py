is_background_bitmap = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsBackgroundBitmap",
    "output_package_name": "view",
    "output_module_name": "is_background_bitmap",

    "doc_html": """
        Verifies that the specified view contains a background bitmap.
    """,

    "syntax_html": {
        0: ("strView"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
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

    "id_com": 779,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

