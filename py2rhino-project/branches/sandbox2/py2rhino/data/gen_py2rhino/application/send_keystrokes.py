send_keystrokes = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "send_keystrokes",

    "doc_html": """
        Sends a string of printable characters, including spaces, to Rhino's command line.
    """,

    "syntax_html": """
        Rhino.SendKeystrokes ([strKeys [, blnAddReturn]])
    """,

    "params_html": {
        0: {
            "name": "Keys",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A string to characters to send to the command line.
            """
        },
        1: {
            "name": "AddReturn",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "bln",
            "doc": """
        Append a return character to the end of the string. The default is to append a return character (True).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 496,

    "params_com": {
        0: {
            "name": "vaStr",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReturn",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

