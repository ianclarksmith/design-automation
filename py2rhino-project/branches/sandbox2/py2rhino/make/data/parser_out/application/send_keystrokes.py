send_keystrokes = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "SendKeystrokes",
    "output_package_name": "application",
    "output_module_name": "send_keystrokes",

    "doc_html": """
        Sends a string of printable characters, including spaces, to Rhino's command line.
    """,

    "syntax_html": {
        0: ("strKeys", "blnAddReturn"),
    },

    "params_html": {
        0: {
            "name": "strKeys",
            "py_name": "keys",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Keys",
            "doc": """
        A string to characters to send to the command line.
            """
        },
        1: {
            "name": "blnAddReturn",
            "py_name": "add_return",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "bln",
            "name_main": "AddReturn",
            "doc": """
        Append a return character to the end of the string. The default is to append a return character (True).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 496,

    "params_com": {
        0: {
            "name": "vaStr",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReturn",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

