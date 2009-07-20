extract_preview_image = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "extract_preview_image",

    "doc_html": """
        Extracts the bitmap preview image from the specified model (.3dm).
    """,

    "syntax_html": """
        Rhino.ExtractPreviewImage (strFileName [, strModelName])
    """,

    "params_html": {
        0: {
            "name": "FileName",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the bitmap file to create.  The extension of the filename controls the format of the bitmap file created.
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
            "name": "ModelName",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The model (.3dm) from which to extract the preview image.  If omitted, the currently loaded model is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
    },

    "id_com": 389,

    "params_com": {
        0: {
            "name": "vaFileName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaModelName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

