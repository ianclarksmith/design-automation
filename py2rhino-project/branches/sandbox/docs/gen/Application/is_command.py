is_command = {

    "class": "Application",
    "method": "is_command",
    "doc": """
        Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.
    """,

    "syntax": """
        Rhino.IsCommand (strCommandName])
    """,

    "params": {
        0: {
            "name": "command_name",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The command name to test.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type_vb": "Null",
            "doc": "On error."
        },
    }

}

