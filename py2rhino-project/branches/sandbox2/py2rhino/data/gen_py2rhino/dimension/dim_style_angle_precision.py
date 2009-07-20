dim_style_angle_precision = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleAnglePrecision",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_angle_precision",

    "doc_html": """
        Returns or changes the angle display precision of a dimension style.
    """,

    "syntax_html": """
        Rhino.DimStyleAnglePrecision (strDimStyle [, intPrecision])
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
            "name": "Precision",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new angle precision value.  If omitted, the current angle precision is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a precision is not specified, the current angle precision if successful."
        },
        1: {
            "type": "number",
            "doc": "If a precision is specified, the previous angle precision if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 464,

    "params_com": {
        0: {
            "name": "vaStyle",
            "opt_or_req": "Required",
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

