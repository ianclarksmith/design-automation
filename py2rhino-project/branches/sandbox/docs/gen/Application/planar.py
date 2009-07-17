planar = {

    "class": "Application",
    "method": "planar",
    "doc": """
        Enables or disables Rhino's planar modeling aid.
    """,

    "syntax": """
        Rhino.Planar ([blnEnable])
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
            "doc": "If blnEnable is not specified, then the current planar status if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is specified, then the previous planar status if successful."
        },
    }

}

