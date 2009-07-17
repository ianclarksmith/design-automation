delete_search_path = {

    "class": "Application",
    "method": "delete_search_path",
    "doc": """
        Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    """,

    "syntax": """
        Rhino.DeleteSearchPath (strFolder)
    """,

    "params": {
        0: {
            "name": "folder",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A valid folder, or path, to remove.
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

