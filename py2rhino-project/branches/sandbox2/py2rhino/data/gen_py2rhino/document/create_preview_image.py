create_preview_image = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "CreatePreviewImage",
    "output_package_name": "document",
    "output_module_name": "create_preview_image",

    "doc_html": """
        Creates a bitmap preview image of the current model.
    """,

    "syntax_html": {
        0: ("strFile", "strView", "arrSize", "intFlags", "blnWireframe"),
    },

    "params_html": {
        0: {
            "name": "strFile",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "File",
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
            "name": "strView",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title of the view.  If omitted, the current active view is used.
            """
        },
        2: {
            "name": "arrSize",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Size",
            "doc": """
        An array of two integers that specify the width and height of the bitmap in pixels.
            """
        },
        3: {
            "name": "intFlags",
            "opt_or_req": "Optional",
            "type": "Integer",
            "name_prefix": "int",
            "name_main": "Flags",
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
            "name": "blnWireframe",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Wireframe",
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

