unit_distance_display_mode = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitDistanceDisplayMode",
    "output_package_name": "document",
    "output_module_name": "unit_distance_display_mode",

    "doc_html": """
        Returns or sets the document's distance display mode parameter.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": """
        Rhino.UnitDistanceDisplayMode ([intMode])
    """,

    "params_html": {
        0: {
            "name": "Mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The distance display mode.  The available distance display modes are as follows:
		Value
		Description
		0
		Decimal
		1
		Fractional
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intMode is not specified, the current distance display mode if successful."
        },
        1: {
            "type": "number",
            "doc": "If intMode is specified, the previous distance display mode if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 327,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

