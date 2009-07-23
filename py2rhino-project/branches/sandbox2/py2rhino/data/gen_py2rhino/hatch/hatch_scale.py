hatch_scale = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "HatchScale",
    "output_package_name": "hatch",
    "output_module_name": "hatch_scale",

    "doc_html": """
        Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane.
    """,

    "syntax_html": {
        0: ("strObject", "dblScale"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a hatch object.
            """
        },
        1: {
            "name": "dblScale",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The scale factor.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a scale factor is not specified, the current scale factor if successful."
        },
        1: {
            "type": "number",
            "doc": "If a scale factor is specified, the previous scale factor if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 838,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

