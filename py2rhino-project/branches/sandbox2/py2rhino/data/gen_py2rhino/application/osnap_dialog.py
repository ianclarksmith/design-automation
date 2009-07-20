osnap_dialog = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "osnap_dialog",

    "doc_html": """
        Shows or hides Rhino's dockable object snap bar.
    """,

    "syntax_html": """
        Rhino.OsnapDialog ([blnVisible])
    """,

    "params_html": {
        0: {
            "name": "Visible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

