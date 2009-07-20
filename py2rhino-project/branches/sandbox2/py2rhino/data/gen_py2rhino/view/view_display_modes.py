view_display_modes = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewDisplayModes",
    "output_package_name": "view",
    "output_module_name": "view_display_modes",

    "doc_html": """
        Returns a list of view display modes, including those listed in the Advanced Display Modes section of Rhino's Options dialog box.
    """,

    "syntax_html": """
        Rhino.ViewDisplayModes ([blnReturnNames])
    """,

    "params_html": {
        0: {
            "name": "ReturnName",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), then the names of the display modes are returned. If False, then the identifiers of the display modes are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A array of strings identifying the display mode names or identifiers if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 908,

    "params_com": {
        0: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

