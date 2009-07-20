edit_box = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "edit_box",

    "doc_html": """
        Displays a dialog box prompting the user to enter a string value.  The string value may span multiple lines.
    """,

    "syntax_html": """
        Rhino.EditBox ([strString [, strMessage [, strTitle]]])
    """,

    "params_html": {
        0: {
            "name": "String",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A default string value.
            """
        },
        1: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        2: {
            "name": "Title",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A dialog box  title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "Multiple lines that are separated by carriage return-linefeed combinations if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 54,

    "params_com": {
        0: {
            "name": "vaString",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrompt",
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

