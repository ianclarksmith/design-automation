string_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "StringBox",
    "output_package_name": "user_interface",
    "output_module_name": "string_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a string value.
    """,

    "syntax_html": {
        0: ("strMessage", "strString", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "strString",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "String",
            "doc": """
        A default string value.
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
            "doc": "The string value if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 60,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaString",
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

