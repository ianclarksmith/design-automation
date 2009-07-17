enable_history_recording = {

    "class": "Application",
    "method": "enable_history_recording",
    "doc": """
        Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.
    """,

    "syntax": """
        Rhino.EnableHistoryRecording ([blnEnable])
    """,

    "params": {
        0: {
            "name": "enable",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The history recording state to set.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "If bEnable is not specified, then the current history recording state."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If bEnable is specified, then the previous history recording state."
        },
    }

}

