ortho = {

    "class": "Application",
    "method": "ortho",
    "doc": """
        Enables or disables Rhino's ortho modeling aid.
    """,

    "syntax": """
        Rhino.Ortho ([blnEnable])
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
            "doc": "If blnEnable is not specified, then the current ortho status if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is specified, then the previous ortho status if successful."
        },
    }

}

