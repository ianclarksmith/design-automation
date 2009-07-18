add_startup_script = {

    "class": "Application",
    "method": "add_startup_script",
    "doc": """
        Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    """,

    "syntax": """
        Rhino.AddStartupScript (strScriptFile [, intIndex])
    """,

    "params": {
        0: {
            "name": "script_file",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A valid path to a RhinoScript .RVB file.
            """
        },
        1: {
            "name": "index",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        A zero-based position index in the startup script list to insert the string. If omitted, the path will be appended to the end of the startup script list.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list."
        },
        1: {
            "type_vb": "Null",
            "doc": "On error."
        },
    }

}

