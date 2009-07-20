string_box = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "string_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a string value.
    """,

    "syntax_html": """
        Rhino.StringBox ([strMessage [, strString [, strTitle]]])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "String",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A default string value.
            """
        },
        2: {
            "name": "Title",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A dialog box title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The string value if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 60,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaString",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

