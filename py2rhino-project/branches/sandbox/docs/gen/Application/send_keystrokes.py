send_keystrokes = {

    "class": "Application",
    "method": "send_keystrokes",
    "doc": """
        Sends a string of printable characters, including spaces, to Rhino's command line.
    """,

    "syntax": """
        Rhino.SendKeystrokes ([strKeys [, blnAddReturn]])
    """,

    "params": {
        0: {
            "name": "keys",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A string to characters to send to the command line.
            """
        },
        1: {
            "name": "add_return",
            "optional": True,
            "type_vb": "string",
            "type_string": "bln",
            "doc": """
        Append a return character to the end of the string. The default is to append a return character (True).
            """
        },
    },

    "returns": {
    }

}

