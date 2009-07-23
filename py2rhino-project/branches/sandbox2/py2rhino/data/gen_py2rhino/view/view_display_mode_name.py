view_display_mode_name = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewDisplayModeName",
    "output_package_name": "view",
    "output_module_name": "view_display_mode_name",

    "doc_html": """
        Returns the name of a display mode given a display mode's identifier.
    """,

    "syntax_html": {
        0: ("strMode"),
    },

    "params_html": {
        0: {
            "name": "strMode",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mode",
            "doc": """
        The identifier of the display mode obtained from the ViewDisplayModes method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the display mode if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 909,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

