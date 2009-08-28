wallpaper = {
    "input_folder_name": "View_Methods",
    "input_file_name": "Wallpaper",
    "output_package_name": "view",
    "output_module_name": "wallpaper",

    "doc_html": """
        Returns or sets the wallpaper bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.
    """,

    "syntax_html": {
        0: ("strView", "strFileName"),
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
            "name": "strFileName",
            "py_name": "file_name",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
            "doc": """
        The name of the bitmap file to set as the wallpaper.  The supported bitmap file formats are as follows:
		.bmp
		Windows Bitmap
		.tga
		Truevision Targa
		.jpg, .jpeg
		JPEG Compliant
		.pcx
		Zsoft Paintbrush
		.png
		Portable Network Graphics
		.tif, .tiff
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFileName is not specified,  then the current wallpaper bitmap filename if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFileName is specified,  then the previous wallpaper bitmap filename if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 532,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFileName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaHidden",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaGrayscale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

