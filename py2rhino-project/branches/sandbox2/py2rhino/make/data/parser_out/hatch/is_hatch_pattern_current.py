is_hatch_pattern_current = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "IsHatchPatternCurrent",
    "output_package_name": "hatch",
    "output_module_name": "is_hatch_pattern_current",

    "doc_html": """
        Verifies that a hatch pattern is the current hatch pattern.
    """,

    "syntax_html": {
        0: ("strHatch"),
    },

    "params_html": {
        0: {
            "name": "strHatch",
            "py_name": "hatch",
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
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 833,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

