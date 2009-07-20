curve_directions_match = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_directions_match",

    "doc_html": """
        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.
    """,

    "syntax_html": """
        Rhino.CurveDirectionsMatch (strCurve1, strCurve2)
    """,

    "params_html": {
        0: {
            "name": "Curve1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first curve to compare.
            """
        },
        1: {
            "name": "Curve2",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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

