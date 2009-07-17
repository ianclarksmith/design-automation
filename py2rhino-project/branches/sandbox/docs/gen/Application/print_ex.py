print_ex = {

    "class": "Application",
    "method": "print_ex",
    "doc": """
        Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.
    """,

    "syntax": """
        Rhino.PrintEx ([strMessage])
    """,

    "params": {
        0: {
            "name": "message",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A prompt, message, or value.
            """
        },
    },

    "returns": {
    }

}

