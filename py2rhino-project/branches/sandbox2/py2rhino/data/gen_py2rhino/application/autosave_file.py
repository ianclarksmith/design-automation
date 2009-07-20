autosave_file = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AutosaveFile",
    "output_package_name": "application",
    "output_module_name": "autosave_file",

    "doc_html": """
        Returns or changes the file name used by Rhino's automatic file saving mechanism.
    """,

    "syntax_html": """
        Rhino.AutosaveFile ([strFile])
    """,

    "params_html": {
        0: {
            "name": "File",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new autosave file.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If an autosave file is not specified, the name of the current autosave file if successful."
        },
        1: {
            "type": "string",
            "doc": "If an autosave file is specified, the name of the previous autosave file if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 428,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

