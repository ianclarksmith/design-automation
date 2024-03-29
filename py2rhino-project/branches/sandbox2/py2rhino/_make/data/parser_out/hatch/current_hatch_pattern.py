current_hatch_pattern = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "CurrentHatchPattern",
    "output_package_name": "hatch",
    "output_module_name": "current_hatch_pattern",

    "doc_html": """
        Returns or sets the current hatch pattern file.
    """,

    "syntax_html": {
        0: ("strHatch"),
    },

    "params_html": {
        0: {
            "name": "strHatch",
            "py_name": "hatch",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Hatch",
            "doc": """
        The name of an existing hatch pattern to make current.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a hatch pattern name is not specified, the current hatch pattern if successful."
        },
        1: {
            "type": "string",
            "doc": "If a hatch pattern name is specified, the previous current hatch pattern if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 827,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

