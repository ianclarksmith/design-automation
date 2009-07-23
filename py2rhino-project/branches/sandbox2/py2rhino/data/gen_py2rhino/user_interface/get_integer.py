get_integer = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetInteger",
    "output_package_name": "user_interface",
    "output_module_name": "get_integer",

    "doc_html": """
        Pauses for user input of a whole number.
    """,

    "syntax_html": {
        0: ("strMessage", "intNumber", "intMin", "intMax"),
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
        A default whole number value.
            """
        },
        2: {
            "name": "intMin",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Min",
            "doc": """
        A minimum allowable value.
            """
        },
        3: {
            "name": "intMax",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Max",
            "doc": """
        A maximum allowable value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The whole number input by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 64,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDefault",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaMin",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaMax",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

