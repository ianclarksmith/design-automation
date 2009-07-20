rename_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "RenameView",
    "output_package_name": "view",
    "output_module_name": "rename_view",

    "doc_html": """
        Renames, or changes the title, of the specified view..
    """,

    "syntax_html": """
        Rhino.RenameView (strOldTitle, strNewTitle)
    """,

    "params_html": {
        0: {
            "name": "OldTitle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view to rename.
            """
        },
        1: {
            "name": "NewTitle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new title of the view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The view's previous title is successful."
        },
        1: {
            "type": "null",
            "doc": "if not successful, or on error."
        },
    },

    "id_com": 260,

    "params_com": {
        0: {
            "name": "vaOld",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNew",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

