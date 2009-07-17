autosave_interval = {

    "class": "Application",
    "method": "autosave_interval",
    "doc": """
        Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.
    """,

    "syntax": """
        Rhino.AutosaveInterval ([intMinutes])
    """,

    "params": {
        0: {
            "name": "minutes",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        The number of minutes between saves.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If an interval is not specified, the current interval in minutes if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If an interval is specified, the previous interval in minutes if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

