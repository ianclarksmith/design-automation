dim_style_linear_precision = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimStyleLinearPrecision",
    "output_package_name": "dimension",
    "output_module_name": "dim_style_linear_precision",

    "doc_html": """
        Returns or changes the linear display precision of a dimension style.
    """,

    "syntax_html": {
        0: ("strDimStyle", "intPrecision"),
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
            "name": "intPrecision",
            "py_name": "precision",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Precision",
            "doc": """
        The new linear precision value.  If omitted, the current linear precision is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a precision is not specified, the current linear precision if successful."
        },
        1: {
            "type": "number",
            "doc": "If ar precision is specified, the previous linear precision if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 463,

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

