curve_frame = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_frame",

    "doc_html": """
        Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.
    """,

    "syntax_html": """
        Rhino.CurveFrame (strObject, dblParameter)
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
            "doc": "The plane at the specified parameter if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 675,

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

