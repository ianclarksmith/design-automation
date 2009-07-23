render_antialias = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderAntialias",
    "output_package_name": "document",
    "output_module_name": "render_antialias",

    "doc_html": """
        Returns or sets render antialiasing style.  Antialiasing is a process where more than one ray is shot per pixel in an attempt to better resolve the value of the
		pixel.  Increasing the antialiasing level can add considerable time to the overall rendering.  See Rhino's DocumentProperties command (Rhino Render window) for details.
    """,

    "syntax_html": {
        0: ("intStyle"),
    },

    "params_html": {
        0: {
            "name": "intStyle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Style",
            "doc": """
        The render antialiasing style.
		Value
		Description
		0
		None
		1
		Normal and slower
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intStyle is not specified, the current render antialiasing style if successful."
        },
        1: {
            "type": "number",
            "doc": "If intStyle  is not specified, the previous render antialiasing style if successful."
        },
        2: {
            "type": "number",
            "doc": "Is not successful, or on error."
        },
    },

    "id_com": 333,

    "params_com": {
        0: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

