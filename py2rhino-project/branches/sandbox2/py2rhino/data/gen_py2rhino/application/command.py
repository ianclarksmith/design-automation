command = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "Command",
    "output_package_name": "application",
    "output_module_name": "command",

    "doc_html": """
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

    "syntax_html": {
        0: ("strCommand", "blnEcho"),
    },

    "params_html": {
        0: {
            "name": "strCommand",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Command",
            "doc": """
        A Rhino command including any arguments.
            """
        },
        1: {
            "name": "blnEcho",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Echo",
            "doc": """
        The command echo mode.  If omitted, command prompts are echoed (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 1,

    "params_com": {
        0: {
            "name": "vaCmd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

