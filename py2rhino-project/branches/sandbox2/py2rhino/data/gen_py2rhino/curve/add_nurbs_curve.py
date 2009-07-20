add_nurbs_curve = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "add_nurbs_curve",

    "doc_html": """
        Adds a NURBS curve object to the document.
    """,

    "syntax_html": """
        Rhino.AddNurbsCurve (arrPoints, arrKnots, intDegree [, arrWeights])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D control points.
            """
        },
        1: {
            "name": "Knots",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The knot values for the curve.  The number of elements in arrKnots must equal the number of elements in arrPoints plus intDegree minus one (1).
            """
        },
        2: {
            "name": "Degree",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The degree of the curve.  The degree must be greater than or equal to one (1).
            """
        },
        3: {
            "name": "Weights",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The weight values for the curve.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 309,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKnots",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDegree",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaWeights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

