delete_startup_script = {

    "class": "Application",
    "method": "delete_startup_script",
    "doc": """
        Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    """,

    "syntax": """
        Rhino.DeleteStartupScript (strScriptFile)
    """,

    "params": {
        0: {
            "name": "script_file",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        An existing script file path to remove.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type_vb": "Null",
            "doc": "On error."
        },
    }

}

