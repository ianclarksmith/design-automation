help = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "help",

    "doc_html": """
        Displays a topic in Rhino's Help file.
    """,

    "syntax_html": """
        Rhino.Help ([intTopic])
    """,

    "params_html": {
        0: {
            "name": "Topic",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        A help topic.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
    },

    "id_com": 22,

    "params_com": {
        0: {
            "name": "vaTopic",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

