is_hatch_pattern_reference = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "IsHatchPatternReference",
    "output_package_name": "hatch",
    "output_module_name": "is_hatch_pattern_reference",

    "doc_html": """
        Verifies that a hatch pattern is from a reference file.
    """,

    "syntax_html": """
        Rhino.IsHatchPatternReference (strHatch)
    """,

    "params_html": {
        0: {
            "name": "Hatch",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

    "id_com": 834,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
