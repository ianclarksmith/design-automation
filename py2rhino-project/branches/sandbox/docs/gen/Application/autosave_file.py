autosave_file = {

    "class": "Application",
    "method": "autosave_file",
    "doc": """
        Returns or changes the file name used by Rhino's automatic file saving mechanism.
    """,

    "syntax": """
        Rhino.AutosaveFile ([strFile])
    """,

    "params": {
        0: {
            "name": "file",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of the new autosave file.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If an autosave file is not specified, the name of the current autosave file if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If an autosave file is specified, the name of the previous autosave file if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

