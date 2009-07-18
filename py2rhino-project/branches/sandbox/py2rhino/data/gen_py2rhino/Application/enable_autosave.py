enable_autosave = {

    "class": "Application",
    "method": "enable_autosave",
    "doc": """
        Enables or disables Rhino's automatic file saving mechanism.
    """,

    "syntax": """
        Rhino.EnableAutosave ([blnEnable])
    """,

    "params": {
        0: {
            "name": "enable",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The autosave state.  If omitted, automatic saving is enabled (True).
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "The previous autosave state."
        },
    }

}

