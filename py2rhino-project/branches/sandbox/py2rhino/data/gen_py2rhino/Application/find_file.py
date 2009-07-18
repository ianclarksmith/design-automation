find_file = {

    "class": "Application",
    "method": "find_file",
    "doc": """
        Searches for a file using Rhino's search path. Rhino will look for a file in the following locations:
		1. The current document's folder.
		2. Folder's specified in Options dialog, File tab.
		3. Rhino's System folders.
    """,

    "syntax": """
        Rhino.FindFile (strFilename)
    """,

    "params": {
        0: {
            "name": "filename",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A valid filename.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "String",
            "doc": "A qualified path to the specified filename if successful."
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

