wallpaper_gray_scale = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "wallpaper_gray_scale",

    "doc_html": """
        Returns or sets the grayscale display option of the wallpaper bitmap of the specified view.
    """,

    "syntax_html": """
        Rhino.WallpaperGrayScale ([strView [, blnGrayScale]])
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
            "name": "GrayScale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

