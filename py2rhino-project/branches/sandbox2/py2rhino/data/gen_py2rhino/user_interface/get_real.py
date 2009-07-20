get_real = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetReal",
    "output_package_name": "user_interface",
    "output_module_name": "get_real",

    "doc_html": """
        Pauses for user input of a number.
    """,

    "syntax_html": """
        Rhino.GetReal (strMessage [, dblNumber [, dblMin [, dblMax]]])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "Number",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A default number value.
            """
        },
        2: {
            "name": "Min",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A minimum allowable value.
            """
        },
        3: {
            "name": "Max",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

