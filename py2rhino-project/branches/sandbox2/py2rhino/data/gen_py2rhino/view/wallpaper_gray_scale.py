wallpaper_gray_scale = {
    "input_folder_name": "View_Methods",
    "input_file_name": "WallpaperGrayScale",
    "output_package_name": "view",
    "output_module_name": "wallpaper_gray_scale",

    "doc_html": """
        Returns or sets the grayscale display option of the wallpaper bitmap of the specified view.
    """,

    "syntax_html": {
        0: ("strView", "blnGrayScale"),
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
            "name": "blnGrayScale",
            "py_name": "gray_scale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "GrayScale",
            "doc": """
        Display the wallpaper bitmap in grayscale (True) or color (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnGrayScale is not specified,  then the current grayscale display option if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnGrayScale is specified,  then the previous grayscale display option if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 534,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaGrayscale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

