convert_curve_to_polyline = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "convert_curve_to_polyline",

    "doc_html": """
        Converts a curve to a polyline curve.
    """,

    "syntax_html": """
        Rhino.ConvertCurveToPolyline (strObject [, dblAngleTolerance [, dblTolerance [, blnDeleteInput]]])
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
            "name": "AngleTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The maximum angle between curve tangents at line endpoints.  If omitted, the angle tolerance is set to 5.0.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the tolerance is set to 0.01.
            """
        },
        3: {
            "name": "DeleteInput",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete the curve object specified by strObject.  If omitted, strObject will not be deleted.
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

    "id_com": 377,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLineAngleTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaLineTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

