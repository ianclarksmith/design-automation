hatch_pattern = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "HatchPattern",
    "output_package_name": "hatch",
    "output_module_name": "hatch_pattern",

    "doc_html": """
        Returns or changes a hatch object's hatch pattern.
    """,

    "syntax_html": {
        0: ("strObject", "strHatch"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a hatch object.
            """
        },
        1: {
            "name": "strHatch",
            "py_name": "hatch",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Hatch",
            "doc": """
        The name of an existing hatch pattern to replace the current hatch pattern.
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

    "id_com": 837,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaHatch",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

