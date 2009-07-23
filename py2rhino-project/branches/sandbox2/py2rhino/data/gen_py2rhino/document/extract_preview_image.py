extract_preview_image = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "ExtractPreviewImage",
    "output_package_name": "document",
    "output_module_name": "extract_preview_image",

    "doc_html": """
        Extracts the bitmap preview image from the specified model (.3dm).
    """,

    "syntax_html": {
        0: ("strFileName", "strModelName"),
    },

    "params_html": {
        0: {
            "name": "strFileName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
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
            "name": "strModelName",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "ModelName",
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

