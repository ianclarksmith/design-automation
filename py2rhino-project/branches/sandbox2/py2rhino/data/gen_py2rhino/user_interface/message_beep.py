message_beep = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "message_beep",

    "doc_html": """
        Plays a system waveform sound.
    """,

    "syntax_html": """
        Rhino.MessageBeep ([intBeep])
    """,

    "params_html": {
        0: {
            "name": "Beep",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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

