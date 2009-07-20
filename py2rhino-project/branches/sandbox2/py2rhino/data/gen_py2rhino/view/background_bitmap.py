background_bitmap = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "background_bitmap",

    "doc_html": """
        Returns or sets the background bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string, or "", as the filename to display.
    """,

    "syntax_html": """
        Rhino.BackgroundBitmap ([strView [, strFileName [, arrPoint [, dblWidth]]]])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
		
		Optional.  String.  The name of the bitmap file to set as the background bitmap.  The supported bitmap file formats are as follows:
		Type
		Description
		bmp
		Windows Bitmap
		tga
		Truevision Targa
		jpg, jpeg
		JPEG Compliant
		pcx
		Zsoft Paintbrush
		png
		Portable Network Graphics
		tif, tiff
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point the lower left corner of the background bitmap. If omitted, the background bitmap's lower left corner will be located at the world origin, or (0,0,0).
            """
        },
        2: {
            "name": "Width",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The width of the background bitmap. If omitted, the actual width of the bitmap will be used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFileName is not specified,  then the current background bitmap filename if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFileName is specified,  then the previous background bitmap filename if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 780,

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
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaWidth",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

