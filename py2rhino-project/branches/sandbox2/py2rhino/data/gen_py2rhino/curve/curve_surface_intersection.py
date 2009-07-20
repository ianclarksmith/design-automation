curve_surface_intersection = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_surface_intersection",

    "doc_html": """
        Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.
    """,

    "syntax_html": """
        Rhino.CurveSurfaceIntersection (strCurve, strSurface [, dblTolerance [, dblAngleTolerance]])
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a curve object.
            """
        },
        1: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a surface object.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            """
        },
        3: {
            "name": "AngleTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle tolerance in degrees.  The angle tolerance is used to determine when the curve is tangent to the surface.  If omitted, the document's current angle tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:"
        },
        1: {
            "type": "number",
            "doc": "The intersection event type, either Point (1) or Overlap (2)."
        },
        2: {
            "type": "number",
            "doc": "If the event type is Point (1), then the curve parameter."
        },
        3: {
            "type": "number",
            "doc": "If the event type is Point (1), then the curve parameter."
        },
        4: {
            "type": "number",
            "doc": "If the event type is Point (1), then the U surface parameter."
        },
        5: {
            "type": "number",
            "doc": "If the event type is Point (1), then the V surface parameter."
        },
        6: {
            "type": "number",
            "doc": "If the event type is Point (1), then the U surface parameter."
        },
        7: {
            "type": "number",
            "doc": "If the event type is Point (1), then the V surface parameter."
        },
        8: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 424,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSrf",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaAngleTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

