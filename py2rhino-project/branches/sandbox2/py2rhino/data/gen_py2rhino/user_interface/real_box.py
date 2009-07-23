real_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "RealBox",
    "output_package_name": "user_interface",
    "output_module_name": "real_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a number.
    """,

    "syntax_html": {
        0: ("strMessage", "dblNumber", "strTitle"),
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
            "name": "dblNumber",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Number",
            "doc": """
        A default number..
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
            "type": "number",
            "doc": "The number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 59,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReal",
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

