is_hatch_pattern = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "IsHatchPattern",
    "output_package_name": "hatch",
    "output_module_name": "is_hatch_pattern",

    "doc_html": """
        Verifies the existence of a hatch pattern in the document.
    """,

    "syntax_html": """
        Rhino.IsHatchPattern (strHatch)
    """,

    "params_html": {
        0: {
            "name": "Hatch",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a hatch pattern.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 832,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

