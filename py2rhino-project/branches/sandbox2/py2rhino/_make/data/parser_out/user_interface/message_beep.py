message_beep = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "MessageBeep",
    "output_package_name": "user_interface",
    "output_module_name": "message_beep",

    "doc_html": """
        Plays a system waveform sound.
    """,

    "syntax_html": {
        0: ("intBeep"),
    },

    "params_html": {
        0: {
            "name": "intBeep",
            "py_name": "beep",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Beep",
            "doc": """
        A sound type.  If omitted, a simple beep (0) is played:
		Value
		Description
		0
		Simple beep.
		1
		System asterisk.
		2
		System exclamation.
		3
		System hand.
		4
		System question.
		5
            """
        },
    },

    "returns_html": {
    },

    "id_com": 149,

    "params_com": {
        0: {
            "name": "vaType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

