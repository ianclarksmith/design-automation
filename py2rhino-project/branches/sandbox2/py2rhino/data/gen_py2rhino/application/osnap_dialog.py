osnap_dialog = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "OsnapDialog",
    "output_package_name": "application",
    "output_module_name": "osnap_dialog",

    "doc_html": """
        Shows or hides Rhino's dockable object snap bar.
    """,

    "syntax_html": {
        0: ("blnVisible"),
    },

    "params_html": {
        0: {
            "name": "blnVisible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Visible",
            "doc": """
        The new visibility state, either True or False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnVisible is not specified, then the current visibility state if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnVisible is specified, then the previous visibility state if successful."
        },
    },

    "id_com": 349,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

