get_integer = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_integer",

    "doc_html": """
        Pauses for user input of a whole number.
    """,

    "syntax_html": """
        Rhino.GetInteger (strMessage [, intNumber [, intMin [, intMax]]])
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
            "type_string": "int",
            "doc": """
        A default whole number value.
            """
        },
        2: {
            "name": "Min",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        A minimum allowable value.
            """
        },
        3: {
            "name": "Max",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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

