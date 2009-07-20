restore_named_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "RestoreNamedView",
    "output_package_name": "view",
    "output_module_name": "restore_named_view",

    "doc_html": """
        Restores a named view to the specified view.
    """,

    "syntax_html": """
        Rhino.RestoreNamedView (strName [, strView [, blnRestoreBitmap]])
    """,

    "params_html": {
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the restored named view if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 283,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRestoreBitmap",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

