in_command = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "InCommand",
    "output_package_name": "application",
    "output_module_name": "in_command",

    "doc_html": """
        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.
    """,

    "syntax_html": {
        0: ("blnIgnoreRunners"),
    },

    "params_html": {
        0: {
            "name": "blnIgnoreRunners",
            "py_name": "ignore_runners",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IgnoreRunners",
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

