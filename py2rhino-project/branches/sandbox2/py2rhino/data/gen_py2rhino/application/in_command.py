in_command = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "in_command",

    "doc_html": """
        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.
    """,

    "syntax_html": """
        Rhino.InCommand ([blnIgnoreRunners])
    """,

    "params_html": {
        0: {
            "name": "IgnoreRunners",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If true, script running commands, such as LoadScript, RunScript, and ReadCommandFile will not counted. The default is not to count script running command (true).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of active commands."
        },
    },

    "id_com": 596,

    "params_com": {
        0: {
            "name": "vaScript",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

