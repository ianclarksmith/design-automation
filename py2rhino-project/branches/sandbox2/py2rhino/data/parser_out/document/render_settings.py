render_settings = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderSettings",
    "output_package_name": "document",
    "output_module_name": "render_settings",

    "doc_html": """
        Returns or sets render settings.  See Rhino's DocumentProperties command (Rhino Render window) for details.
    """,

    "syntax_html": {
        0: ("intSettings"),
    },

    "params_html": {
        0: {
            "name": "intSettings",
            "py_name": "settings",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Settings",
            "doc": """
        The render setting or settings to modify.  Render settings can be any combination of the following flags:
		Value
		Description
		0
		None.
		1
		Create shadows.
		2
		Use lights on layers that are off.
		4
		Render curves and isocurves.
		8
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intSettings is not specified, the current render settings if successful."
        },
        1: {
            "type": "number",
            "doc": "If intSettings is not specified, the previous render settings if successful."
        },
        2: {
            "type": "number",
            "doc": "Is not successful, or on error."
        },
    },

    "id_com": 334,

    "params_com": {
        0: {
            "name": "vaSetting",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

