help = {

    "class": "Application",
    "method": "help",
    "doc": """
        Displays a topic in Rhino's Help file.
    """,

    "syntax": """
        Rhino.Help ([intTopic])
    """,

    "params": {
        0: {
            "name": "topic",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        A help topic.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "True or False indicating success or failure."
        },
    }

}

