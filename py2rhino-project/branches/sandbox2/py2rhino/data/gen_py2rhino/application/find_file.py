find_file = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "find_file",

    "doc_html": """
        Searches for a file using Rhino's search path. Rhino will look for a file in the following locations:
		1. The current document's folder.
		2. Folder's specified in Options dialog, File tab.
		3. Rhino's System folders.
    """,

    "syntax_html": """
        Rhino.FindFile (strFilename)
    """,

    "params_html": {
        0: {
            "name": "Filename",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A valid filename.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "A qualified path to the specified filename if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 81,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

