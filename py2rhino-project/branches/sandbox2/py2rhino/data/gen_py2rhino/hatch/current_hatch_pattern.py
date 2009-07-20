current_hatch_pattern = {
    "module_name": "hatch",
    "class_name": "Hatch",
    "method_name": "current_hatch_pattern",

    "doc_html": """
        Returns or sets the current hatch pattern file.
    """,

    "syntax_html": """
        Rhino.CurrentHatchPattern ([strHatch])
    """,

    "params_html": {
        0: {
            "name": "Hatch",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

