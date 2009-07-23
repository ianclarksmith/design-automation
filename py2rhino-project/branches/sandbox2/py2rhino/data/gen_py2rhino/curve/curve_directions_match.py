curve_directions_match = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveDirectionsMatch",
    "output_package_name": "curve",
    "output_module_name": "curve_directions_match",

    "doc_html": """
        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.
    """,

    "syntax_html": {
        0: ("strCurve1", "strCurve2"),
    },

    "params_html": {
        0: {
            "name": "strCurve1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve1",
            "doc": """
        The identifier of the first curve to compare.
            """
        },
        1: {
            "name": "strCurve2",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve2",
            "doc": """
        The identifier of the second curve to compare.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the curve directions match, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 543,

    "params_com": {
        0: {
            "name": "vaCrv1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrv2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

