text_out = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "text_out",

    "doc_html": """
        Displays a text output window.
    """,

    "syntax_html": """
        Rhino.TextOut (strText [, strTitle]])
    """,

    "params_html": {
        0: {
            "name": "Text",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A text string to display.
            """
        },
        1: {
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
            "type": "null",
            "doc": "If successful or on failure."
        },
    },

    "id_com": 755,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

