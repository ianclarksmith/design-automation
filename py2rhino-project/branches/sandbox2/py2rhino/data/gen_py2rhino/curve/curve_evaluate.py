curve_evaluate = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_evaluate",

    "doc_html": """
        A general purpose curve evaluator.
    """,

    "syntax_html": """
        Rhino.CurveEvaluate (strObject, dblParameter, intDerivative)
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
        The evaluation parameter.
            """
        },
        2: {
            "name": "Derivative",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The number of derivatives to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of length (intDerivative+1) if successful.  The array elements are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The 3-D point"
        },
        2: {
            "type": "array",
            "doc": "The first derivative"
        },
        3: {
            "type": "array",
            "doc": "The second derivative"
        },
        4: {
            "type": "array",
            "doc": "etc..."
        },
        5: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 489,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDevCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

