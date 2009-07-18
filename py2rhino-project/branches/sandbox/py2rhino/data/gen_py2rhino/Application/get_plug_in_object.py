get_plug_in_object = {

    "class": "Application",
    "method": "get_plug_in_object",
    "doc": """
        Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.
    """,

    "syntax": """
        Rhino.GetPlugInObject (strPlugIn)
    """,

    "params": {
        0: {
            "name": "plug_in",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        The name of a registered plug-in that supports scripting.  If the plug-in is registered but not loaded, it will be loaded.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

