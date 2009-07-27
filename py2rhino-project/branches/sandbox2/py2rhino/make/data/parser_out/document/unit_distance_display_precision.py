unit_distance_display_precision = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitDistanceDisplayPrecision",
    "output_package_name": "document",
    "output_module_name": "unit_distance_display_precision",

    "doc_html": """
        Returns or sets the document's distance display precision parameter.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": {
        0: ("intPrecision"),
    },

    "params_html": {
        0: {
            "name": "intPrecision",
            "py_name": "precision",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Precision",
            "doc": """
        The distance display precision.  If the current distance display mode is Decimal, then intPrecision is the number of decimal places.  If the current distance display mode is Fractional (including Feet and Inches), then the denominator = (1/2)^intPrecision.  Use UnitDistanceDisplayMode to get the current distance display mode.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intPrecision is not specified, the current distance display precision if successful."
        },
        1: {
            "type": "number",
            "doc": "If intPrecision is specified, the previous distance display precision if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 328,

    "params_com": {
        0: {
            "name": "vaPrecision",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

