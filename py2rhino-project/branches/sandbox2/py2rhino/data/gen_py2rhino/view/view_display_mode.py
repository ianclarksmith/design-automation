view_display_mode = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewDisplayMode",
    "output_package_name": "view",
    "output_module_name": "view_display_mode",

    "doc_html": """
        Returns or sets a view's display mode.  A view's display mode can be either wireframe, shaded, or render preview.
    """,

    "syntax_html": """
        Rhino.ViewDisplayMode ([strView [, intMode]])
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
            "name": "Mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The display mode.  The display modes are as follows:
		Value
		Description
		0
		Wireframe.
		1
		Shaded.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intMode is not specified, the current display mode for the specified view if successful."
        },
        1: {
            "type": "number",
            "doc": "If intMode is specified, the previous display mode for the specified view if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 290,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

