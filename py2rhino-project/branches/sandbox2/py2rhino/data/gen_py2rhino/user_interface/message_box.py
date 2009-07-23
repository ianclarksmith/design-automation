message_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "MessageBox",
    "output_package_name": "user_interface",
    "output_module_name": "message_box",

    "doc_html": """
        Displays a Windows message box. A message box contains an application-defined message and title, plus any combination of predefined icons and push buttons.
    """,

    "syntax_html": {
        0: ("strMessage", "intButtons", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "intButtons",
            "py_name": "buttons",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Buttons",
            "doc": """
        The buttons and icon to display.  This parameter can be a combination of the following flags.  If omitted, an OK button and no icon is displayed.
		Value
		Description
		0
		Display OK button only.
		1
		Display OK and Cancel buttons.
		2
		Display Abort, Retry, and Ignore buttons.
		3
		Display Yes, No, and Cancel buttons.
		4
		Display Yes and No buttons.
		5
		Display Retry and Cancel buttons.
		16
		Display Critical Message icon.
		32
		Display Warning Query icon.
		48
		Display Warning Message icon.
		64
		Display Information Message icon.
		0
		First button is the default.
		256
		Second button is the default.
		512
		Third button is the default.
		768
		Fourth button is the default.
		0
		Application modal. The user must respond to the message box before continuing work in the current application.
		4096
            """
        },
        2: {
            "name": "strTitle",
            "py_name": "title",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Title",
            "doc": """
        A dialog box title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "An number indicating which button was clicked:"
        },
    },

    "id_com": 150,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCaption",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

