snap = {

    "class": "Application",
    "method": "snap",
    "doc": """
        Enables or disables Rhino's grid snap modeling aid.
    """,

    "syntax": """
        Rhino.Snap ([blnEnable])
    """,

    "params": {
        0: {
            "name": "enable",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The new enabled status, either True or False
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is not specified, then the current grid snap status if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is specified, then the previous grid snap status if successful."
        },
    }

}

