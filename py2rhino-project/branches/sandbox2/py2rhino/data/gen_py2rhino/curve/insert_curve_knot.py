insert_curve_knot = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "insert_curve_knot",

    "doc_html": """
        Inserts a knot into a curve object.
    """,

    "syntax_html": """
        Rhino.InsertCurveKnot (strObject, dblParameter [, blnSymmetrical)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve object.
            """
        },
        1: {
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The parameter on the curve.
            """
        },
        2: {
            "name": "Symmetrical",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If blnSymmetrical = True, then knots are added on both sides of the center of the curve. The default value is False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 515,

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
        2: {
            "name": "vaSym",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

