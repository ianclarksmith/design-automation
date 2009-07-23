curve_perp_frame = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurvePerpFrame",
    "output_package_name": "curve",
    "output_module_name": "curve_perp_frame",

    "doc_html": """
        Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.
    """,

    "syntax_html": {
        0: ("strObject", "dblParameter"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "dblParameter",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Parameter",
            "doc": """
        The parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane at the specified parameter if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 676,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

