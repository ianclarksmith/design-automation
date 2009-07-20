is_curve_closable = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "is_curve_closable",

    "doc_html": """
        Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.
    """,

    "syntax_html": """
        Rhino.IsCurveClosable (strObject [, dblTolerance])
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
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 441,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

