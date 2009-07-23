edit_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "EditBox",
    "output_package_name": "user_interface",
    "output_module_name": "edit_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a string value.  The string value may span multiple lines.
    """,

    "syntax_html": {
        0: ("strString", "strMessage", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "strString",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "String",
            "doc": """
        A default string value.
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
        A dialog box  title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "Multiple lines that are separated by carriage return-linefeed combinations if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 54,

    "params_com": {
        0: {
            "name": "vaString",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrompt",
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

