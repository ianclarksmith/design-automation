enable_history_recording = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "EnableHistoryRecording",
    "output_package_name": "application",
    "output_module_name": "enable_history_recording",

    "doc_html": """
        Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.
    """,

    "syntax_html": {
        0: ("blnEnable"),
    },

    "params_html": {
        0: {
            "name": "blnEnable",
            "py_name": "enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Enable",
            "doc": """
        The history recording state to set.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If bEnable is not specified, then the current history recording state."
        },
        1: {
            "type": "boolean",
            "doc": "If bEnable is specified, then the previous history recording state."
        },
    },

    "id_com": 735,

    "params_com": {
        0: {
            "name": "vaEnable",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

