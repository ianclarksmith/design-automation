project_osnaps = {

    "class": "Application",
    "method": "project_osnaps",
    "doc": """
        Enables or disables object snap projection.
    """,

    "syntax": """
        Rhino.ProjectOsnaps ([blnEnable])
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
            "doc": "If blnEnable is not specified, then the current object snap projection status if successful."
        },
        1: {
            "type_vb": "Boolean",
            "doc": "If blnEnable is specified, then the previous object snap projection status if successful."
        },
    }

}

