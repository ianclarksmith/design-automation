in_command = {

    "class": "Application",
    "method": "in_command",
    "doc": """
        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.
    """,

    "syntax": """
        Rhino.InCommand ([blnIgnoreRunners])
    """,

    "params": {
        0: {
            "name": "ignore_runners",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        If true, script running commands, such as LoadScript, RunScript, and ReadCommandFile will not counted. The default is not to count script running command (true).
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "The number of active commands."
        },
    }

}

