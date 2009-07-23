integer_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "IntegerBox",
    "output_package_name": "user_interface",
    "output_module_name": "integer_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a whole number.
    """,

    "syntax_html": {
        0: ("strMessage", "intNumber", "strTitle"),
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
            "name": "intNumber",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Number",
            "doc": """
        A default whole number.
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
            "doc": "The whole number if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 55,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaInteger",
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

