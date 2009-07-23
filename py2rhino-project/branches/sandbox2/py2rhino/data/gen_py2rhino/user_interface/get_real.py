get_real = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetReal",
    "output_package_name": "user_interface",
    "output_module_name": "get_real",

    "doc_html": """
        Pauses for user input of a number.
    """,

    "syntax_html": {
        0: ("strMessage", "dblNumber", "dblMin", "dblMax"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
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
            "py_name": "number",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Number",
            "doc": """
        A default number value.
            """
        },
        2: {
            "name": "dblMin",
            "py_name": "min",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Min",
            "doc": """
        A minimum allowable value.
            """
        },
        3: {
            "name": "dblMax",
            "py_name": "max",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Max",
            "doc": """
        A maximum allowable value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number input by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 63,

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

