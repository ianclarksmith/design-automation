get_linetype = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_linetype",

    "doc_html": """
        Displays a dialog box prompting the user to select a linetype.
    """,

    "syntax_html": """
        Rhino.GetLinetype ([strLinetype])
    """,

    "params_html": {
        0: {
            "name": "Linetype",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the linetype to select.  If omitted, the current linetype will be selected.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the selected linetype if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 673,

    "params_com": {
        0: {
            "name": "vaLinetype",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

