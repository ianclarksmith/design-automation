evaluate_curve = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "evaluate_curve",

    "doc_html": """
        Evaluates a curve at a parameter.
    """,

    "syntax_html": """
        Rhino.EvaluateCurve (strObject, dblParameter [, intIndex)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The parameter to evaluate.
            """
        },
        2: {
            "name": "Index",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 100,

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
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

