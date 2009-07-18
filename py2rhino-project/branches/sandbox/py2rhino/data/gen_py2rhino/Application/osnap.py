osnap = {

    "class": "Application",
    "method": "osnap",
    "doc": """
        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.
    """,

    "syntax": """
        Rhino.Osnap ([blnEnable])
    """,

    "params": {
        0: {
            "name": "enable",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The new enabled status, either True or False.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is not specified, then the current object snap status if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is specified, then the previous object snap status if successful."
        },
    }

}

