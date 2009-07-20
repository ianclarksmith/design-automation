working_folder = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "working_folder",

    "doc_html": """
        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.
    """,

    "syntax_html": """
        Rhino.WorkingFolder ([strFolder])
    """,

    "params_html": {
        0: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "bln",
            "doc": """
        The new working folder.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFolder is not specified, then the current working folder if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFolder is specified, then the previous working folder if successful."
        },
    },

    "id_com": 439,

    "params_com": {
        0: {
            "name": "vaFolder",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

