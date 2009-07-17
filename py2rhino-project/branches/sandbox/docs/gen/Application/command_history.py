command_history = {

    "class": "Application",
    "method": "command_history",
    "doc": """
        Returns the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.
    """,

    "syntax": """
        Rhino.CommandHistory ()
    """,

    "params": {
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "A string containing the contents of Rhino's command history window if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

