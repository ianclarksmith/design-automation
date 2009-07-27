working_folder = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "WorkingFolder",
    "output_package_name": "application",
    "output_module_name": "working_folder",

    "doc_html": """
        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.
    """,

    "syntax_html": {
        0: ("strFolder"),
    },

    "params_html": {
        0: {
            "name": "blnEnable",
            "py_name": "enable",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "bln",
            "name_main": "Enable",
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

