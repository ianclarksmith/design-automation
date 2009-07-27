view_display_mode_ex = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewDisplayModeEx",
    "output_package_name": "view",
    "output_module_name": "view_display_mode_ex",

    "doc_html": """
        Returns or sets a view's display mode.  Unlike the ViewDisplayMode method, which only allows you to set a view to wireframe, shaded, or render preview, this method allows you to set a view to any display mode including those listed in the Advanced Display Modes section of Rhino's Options dialog box.
    """,

    "syntax_html": {
        0: ("strView", "strMode", "blnReturnNames"),
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
            "name": "strMode",
            "py_name": "mode",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mode",
            "doc": """
        The name or identifier of the display mode obtained from the ViewDisplayModes method.
            """
        },
        2: {
            "name": "blnReturnNames",
            "py_name": "return_names",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnNames",
            "doc": """
        If True (default), then the name the display mode is returned. If False, then the identifier of the display mode is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If strMode is not specified, the current display mode for the specified view if successful."
        },
        1: {
            "type": "number",
            "doc": "If strMode is specified, the previous display mode for the specified view if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 910,

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
        2: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

