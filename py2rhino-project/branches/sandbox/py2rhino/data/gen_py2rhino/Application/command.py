command = {

    "class": "Application",
    "method": "command",
    "doc": """
        Runs a Rhino command script.  All Rhino commands can be used in command scripts.  The command can be a build-in Rhino command or a command that is provided by a 3rd party plug-in.
		Write command scripts just as you would type the command sequence at the command line. A space between characters or a new line act like pressing <Enter> at the command line.  For more information on writing command scripts, see "Scripting" in the Rhino help file.
		Note, this method is designed to run one command and one command only.  Do not combine multiple Rhino commands into a single call to this method.  For example:
		WRONG:
		Rhino.Command "_Line _SelLast _Invert"
		CORRECT:
		Rhino.Command "_Line"
		Rhino.Command "_SelLast"
		Rhino.Command "_Invert"
		Also, the exclamation point and space character ( ! ) combination used by button macros and batch-driven scripts to cancel the previous command is not valid.  For example:
		WRONG:
		Rhino.Command "! _Line _Pause _Pause"
		CORRECT:
		Rhino.Command "_Line _Pause _Pause"
		After the command script has run, you can obtain the identifiers of most recently created or changed object by calling LastCreatedObjects.
    """,

    "syntax": """
        Rhino.Command (strCommand [, blnEcho])
    """,

    "params": {
        0: {
            "name": "command",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A Rhino command including any arguments.
            """
        },
        1: {
            "name": "echo",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The command echo mode.  If omitted, command prompts are echoed (True).
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type_vb": "Null",
            "doc": "On error."
        },
    }

}

