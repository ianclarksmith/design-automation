wallpaper_hidden = {
    "input_folder_name": "View_Methods",
    "input_file_name": "WallpaperHidden",
    "output_package_name": "view",
    "output_module_name": "wallpaper_hidden",

    "doc_html": """
        Returns or sets the visibility of the wallpaper bitmap of the specified view.
    """,

    "syntax_html": {
        0: ("strView", "blnHidden"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "blnHidden",
            "py_name": "hidden",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Hidden",
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

