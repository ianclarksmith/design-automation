default_renderer = {

    "class": "Application",
    "method": "default_renderer",
    "doc": """
        Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.
    """,

    "syntax": """
        Rhino.DefaultRenderer ([strRenderer])
    """,

    "params": {
        0: {
            "name": "renderer",
            "optional": True,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of a render plug-in to set as default.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "If a render plug-in is not specified, the name of the current render plug-in if successful."
        },
        1: {
            "type_vb": "String",
            "doc": "If a render plug-in is specified, the name of the previous current render plug-in if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

