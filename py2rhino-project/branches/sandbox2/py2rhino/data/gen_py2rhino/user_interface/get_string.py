get_string = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetString",
    "output_package_name": "user_interface",
    "output_module_name": "get_string",

    "doc_html": """
        Pauses for user input of string value.
    """,

    "syntax_html": {
        0: ("strMessage", "strString", "arrStrings"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "strString",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "String",
            "doc": """
        A default value.
            """
        },
        2: {
            "name": "arrStrings",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Strings",
            "doc": """
        A array of strings to be displayed as click-able command options. Note, strings cannot begin with a numeric character.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The string either input or selected by the user if successful.  If the user presses the Enter key without typing in a string, an empty string "" is returned."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 62,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDefault",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaStrings",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

