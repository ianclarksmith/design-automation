osnap_dialog = {

    "class": "Application",
    "method": "osnap_dialog",
    "doc": """
        Shows or hides Rhino's dockable object snap bar.
    """,

    "syntax": """
        Rhino.OsnapDialog ([blnVisible])
    """,

    "params": {
        0: {
            "name": "visible",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The new visibility state, either True or False.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "If blnVisible is not specified, then the current visibility state if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnVisible is specified, then the previous visibility state if successful."
        },
    }

}

