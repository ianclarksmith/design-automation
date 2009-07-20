curve_curve_intersection = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_curve_intersection",

    "doc_html": """
        Calculates the intersection of two curve objects.
    """,

    "syntax_html": """
        Rhino.CurveCurveIntersection (strObject1 [, strObject2 [, dblTolerance]])
    """,

    "params_html": {
        0: {
            "name": "Object1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "Object2",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the second curve object.  If omitted, the a self-intersection test will be performed on strObject1.
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
            "doc": "If the event type is Point (1), then the first curve parameter."
        },
        3: {
            "type": "number",
            "doc": "If the event type is Point (1), then the first curve parameter."
        },
        4: {
            "type": "number",
            "doc": "If the event type is Point (1), then the second curve parameter."
        },
        5: {
            "type": "number",
            "doc": "If the event type is Point (1), then the second curve parameter."
        },
        6: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 423,

    "params_com": {
        0: {
            "name": "vaCrvA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrvB",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

