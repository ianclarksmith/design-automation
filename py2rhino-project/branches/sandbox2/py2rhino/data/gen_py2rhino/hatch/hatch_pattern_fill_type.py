hatch_pattern_fill_type = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "HatchPatternFillType",
    "output_package_name": "hatch",
    "output_module_name": "hatch_pattern_fill_type",

    "doc_html": """
        Returns the fill type of a hatch pattern. Hatch patterns have one of the following fill types:
		Value
		Description
		0
		Solid, uses object color.
		1
		Lines, uses pattern file definition.
		2
		Gradient, uses fill color definition.
    """,

    "syntax_html": {
        0: ("strHatch"),
    },

    "params_html": {
        0: {
            "name": "strHatch",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Hatch",
            "doc": """
        The name of an existing hatch pattern.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If hatch pattern's fill type if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 831,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

