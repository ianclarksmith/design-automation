get_boolean = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetBoolean",
    "output_package_name": "user_interface",
    "output_module_name": "get_boolean",

    "doc_html": """
        Pauses for user input of one or more boolean values. Boolean values are displayed as click-able command-line option toggles.
    """,

    "syntax_html": """
        Rhino.GetBoolean (strMessage, arrItems, arrDefaults)
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "Items",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of strings that describe the boolean items that will appear as command-line option toggles. Each boolean item consists of three strings.
		Element
		Description
		0
		A description of the boolean value.
		1
		A string identifying the False value.
		2
            """
        },
        2: {
            "name": "Defaults",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_bln",
            "doc": """
        A array of boolean values to be used as default, or starting values.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of boolean values that represent the boolean items, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 622,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaItems",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDefaults",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

