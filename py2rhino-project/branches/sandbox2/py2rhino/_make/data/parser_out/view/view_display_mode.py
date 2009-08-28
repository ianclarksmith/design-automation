view_display_mode = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewDisplayMode",
    "output_package_name": "view",
    "output_module_name": "view_display_mode",

    "doc_html": """
        Returns or sets a view's display mode.  A view's display mode can be either wireframe, shaded, or render preview.
    """,

    "syntax_html": {
        0: ("strView", "intMode"),
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
            "name": "intMode",
            "py_name": "mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Mode",
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

