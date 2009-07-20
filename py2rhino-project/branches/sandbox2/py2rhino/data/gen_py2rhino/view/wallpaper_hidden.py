wallpaper_hidden = {
    "input_folder_name": "View_Methods",
    "input_file_name": "WallpaperHidden",
    "output_package_name": "view",
    "output_module_name": "wallpaper_hidden",

    "doc_html": """
        Returns or sets the visibility of the wallpaper bitmap of the specified view.
    """,

    "syntax_html": """
        Rhino.WallpaperHidden ([strView [, blnHidden]])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "Hidden",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Hide the wallpaper bitmap (True) or show the wallpaper bitmap (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnHidden is not specified,  then the current wallpaper visibility if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnHidden is specified,  then the previous wallpaper visibility if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 533,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaHidden",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

