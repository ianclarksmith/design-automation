dim_style_number_format = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "dim_style_number_format",

    "doc_html": """
        Returns or changes the number display format of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleNumberFormat (strDimStyle [, intFormat])
    """,

    "params_html": {
        0: {
            "name": "DimStyle",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing dimension style.
            """
        },
        1: {
            "name": "Format",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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

