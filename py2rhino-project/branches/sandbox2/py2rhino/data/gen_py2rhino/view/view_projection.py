view_projection = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewProjection",
    "output_package_name": "view",
    "output_module_name": "view_projection",

    "doc_html": """
        Returns or sets a view's projection mode.  A view's projection mode can be either parallel or perspective.
    """,

    "syntax_html": {
        0: ("strView", "intMode"),
    },

    "params_html": {
        0: {
            "name": "strView",
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
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Mode",
            "doc": """
        The projection mode.  The projection modes are as follows:
		Value
		Description
		1
		Parallel
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intMode is not specified, the current projection mode for the specified view if successful."
        },
        1: {
            "type": "number",
            "doc": "If intMode is specified, the previous projection mode for the specified view if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 266,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

