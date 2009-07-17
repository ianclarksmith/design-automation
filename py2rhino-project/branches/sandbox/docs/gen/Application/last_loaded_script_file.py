last_loaded_script_file = {

    "class": "Application",
    "method": "last_loaded_script_file",
    "doc": """
        Return the full path to the last RhinoScript file that was loaded using the LoadScript command..
    """,

    "syntax": """
        Rhino.LastLoadedScriptFile ()
    """,

    "params": {
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "The last loaded script file if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

