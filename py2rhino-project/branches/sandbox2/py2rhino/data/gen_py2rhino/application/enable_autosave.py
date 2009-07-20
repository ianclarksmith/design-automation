enable_autosave = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "EnableAutosave",
    "output_package_name": "application",
    "output_module_name": "enable_autosave",

    "doc_html": """
        Enables or disables Rhino's automatic file saving mechanism.
    """,

    "syntax_html": """
        Rhino.EnableAutosave ([blnEnable])
    """,

    "params_html": {
        0: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The autosave state.  If omitted, automatic saving is enabled (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "The previous autosave state."
        },
    },

    "id_com": 430,

    "params_com": {
        0: {
            "name": "vaEnable",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

