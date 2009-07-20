autosave_interval = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AutosaveInterval",
    "output_package_name": "application",
    "output_module_name": "autosave_interval",

    "doc_html": """
        Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.
    """,

    "syntax_html": """
        Rhino.AutosaveInterval ([intMinutes])
    """,

    "params_html": {
        0: {
            "name": "Minutes",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The number of minutes between saves.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If an interval is not specified, the current interval in minutes if successful."
        },
        1: {
            "type": "number",
            "doc": "If an interval is specified, the previous interval in minutes if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 429,

    "params_com": {
        0: {
            "name": "vaMinutes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

