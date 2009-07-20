curve_curvature = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_curvature",

    "doc_html": """
        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.
    """,

    "syntax_html": """
        Rhino.CurveCurvature (strObject, dblParameter)
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of curvature information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "Radius of curvature"
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 379,

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

