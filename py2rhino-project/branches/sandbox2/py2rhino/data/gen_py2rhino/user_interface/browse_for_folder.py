browse_for_folder = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "BrowseForFolder",
    "output_package_name": "user_interface",
    "output_module_name": "browse_for_folder",

    "doc_html": """
        Displays the Windows browse-for-folder dialog box allowing the user to select a folder.
    """,

    "syntax_html": {
        0: ("strFolder", "strMessage", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "strFolder",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Folder",
            "doc": """
        A default folder.
            """
        },
        1: {
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        2: {
            "name": "strTitle",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Title",
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

