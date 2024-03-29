help = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "Help",
    "output_package_name": "application",
    "output_module_name": "help",

    "doc_html": """
        Displays a topic in Rhino's Help file.
    """,

    "syntax_html": {
        0: ("intTopic"),
    },

    "params_html": {
        0: {
            "name": "intTopic",
            "py_name": "topic",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Topic",
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

