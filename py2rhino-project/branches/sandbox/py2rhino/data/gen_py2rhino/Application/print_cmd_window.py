print_cmd_window = {

    "class": "Application",
    "method": "print_cmd_window",
    "doc": """
        Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.
    """,

    "syntax": """
        Rhino.Print ([strMessage])
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

