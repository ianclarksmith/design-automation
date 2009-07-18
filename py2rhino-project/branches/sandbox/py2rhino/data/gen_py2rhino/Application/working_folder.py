working_folder = {

    "class": "Application",
    "method": "working_folder",
    "doc": """
        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.
    """,

    "syntax": """
        Rhino.WorkingFolder ([strFolder])
    """,

    "params": {
        0: {
            "name": "enable",
            "optional": True,
            "type_vb": "string",
            "type_string": "bln",
            "doc": """
        The new working folder.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If strFolder is not specified, then the current working folder if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If strFolder is specified, then the previous working folder if successful."
        },
    }

}

