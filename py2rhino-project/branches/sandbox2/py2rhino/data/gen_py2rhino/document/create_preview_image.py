create_preview_image = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "create_preview_image",

    "doc_html": """
        Creates a bitmap preview image of the current model.
    """,

    "syntax_html": """
        Rhino.CreatePreviewImage (strFile [, strView [, arrSize [, intFlags [, blnWireframe]]]])
    """,

    "params_html": {
        0: {
            "name": "File",
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
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title of the view.  If omitted, the current active view is used.
            """
        },
        2: {
            "name": "Size",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two integers that specify the width and height of the bitmap in pixels.
            """
        },
        3: {
            "name": "Flags",
            "opt_or_req": "Optional",
            "type": "Integer",
            "type_string": "int",
            "doc": """
        The bitmap creation flags. This parameter can be a combination of the following:
		Value
		Description
		1
		Honor object highlighting.  The default is to ignore highlighting (False).
		2
		Draw construction plane.  The default is not to draw the construction plane (False).
		4
            """
        },
        4: {
            "name": "Wireframe",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If specified and True, then a wireframe preview image, instead of a rendered image, will be created. Note, if this option is specified and True, then the ghosted shading flag is ignored.  The default value is False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
    },

    "id_com": 388,

    "params_com": {
        0: {
            "name": "vaFileName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSize",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaWireframe",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

