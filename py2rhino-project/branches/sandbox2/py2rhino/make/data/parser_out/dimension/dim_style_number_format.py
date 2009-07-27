dim_style_number_format = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleNumberFormat",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_number_format",

    "doc_html": """
        Returns or changes the number display format of a dimension style.
    """,

    "syntax_html": {
        0: ("strDimStyle", "intFormat"),
    },

    "params_html": {
        0: {
            "name": "strDimStyle",
            "py_name": "dim_style",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "DimStyle",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "intFormat",
            "py_name": "format",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Format",
            "doc": """
        The new number display format.  If omitted, the current number display format is returned.  The format values are as follows:
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
            "doc": "If a format is not specified, the current number display format if successful."
        },
        1: {
            "type": "number",
            "doc": "If a format is specified, the previous number display format if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 459,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFormat",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

