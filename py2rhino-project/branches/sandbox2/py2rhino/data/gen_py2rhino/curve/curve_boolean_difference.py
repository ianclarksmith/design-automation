curve_boolean_difference = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_boolean_difference",

    "doc_html": """
        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    """,

    "syntax_html": """
        Rhino.CurveBooleanDifference (strCurveA, strCurveB)
    """,

    "params_html": {
        0: {
            "name": "CurveA",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "CurveB",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the second curve object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 811,

    "params_com": {
        0: {
            "name": "vaCurveA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurveB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

