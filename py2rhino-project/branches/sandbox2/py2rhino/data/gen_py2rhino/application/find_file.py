find_file = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "FindFile",
    "output_package_name": "application",
    "output_module_name": "find_file",

    "doc_html": """
        Searches for a file using Rhino's search path. Rhino will look for a file in the following locations:
		1. The current document's folder.
		2. Folder's specified in Options dialog, File tab.
		3. Rhino's System folders.
    """,

    "syntax_html": {
        0: ("strFilename"),
    },

    "params_html": {
        0: {
            "name": "strFilename",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Filename",
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

