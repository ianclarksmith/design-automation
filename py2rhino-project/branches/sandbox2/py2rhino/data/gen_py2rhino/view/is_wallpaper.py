is_wallpaper = {
    "input_folder_name": "View_Methods",
    "input_file_name": "IsWallpaper",
    "output_package_name": "view",
    "output_module_name": "is_wallpaper",

    "doc_html": """
        Verifies that the specified view contains a wallpaper bitmap.
    """,

    "syntax_html": """
        Rhino.IsWallpaper (strView)
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 531,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

