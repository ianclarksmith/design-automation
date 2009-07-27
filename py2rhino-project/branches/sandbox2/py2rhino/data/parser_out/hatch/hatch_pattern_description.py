hatch_pattern_description = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "HatchPatternDescription",
    "output_package_name": "hatch",
    "output_module_name": "hatch_pattern_description",

    "doc_html": """
        Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions for descriptions are optional.
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
            "type": "string",
            "doc": "If hatch pattern's description if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 829,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

