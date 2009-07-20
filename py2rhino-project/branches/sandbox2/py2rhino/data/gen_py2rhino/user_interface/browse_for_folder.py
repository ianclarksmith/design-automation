browse_for_folder = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "browse_for_folder",

    "doc_html": """
        Displays the Windows browse-for-folder dialog box allowing the user to select a folder.
    """,

    "syntax_html": """
        Rhino.BrowseForFolder ([strFolder [, strMessage [, strTitle]]])
    """,

    "params_html": {
        0: {
            "name": "Folder",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A default folder.
            """
        },
        1: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        2: {
            "name": "Title",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A dialog box title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The selected folder if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 146,

    "params_com": {
        0: {
            "name": "vaPath",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMessage",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

