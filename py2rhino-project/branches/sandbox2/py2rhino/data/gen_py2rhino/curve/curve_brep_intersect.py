curve_brep_intersect = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_brep_intersect",

    "doc_html": """
        Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.
    """,

    "syntax_html": """
        Rhino.CurveBrepIntersect (strCurve, strBrep [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The curve object's identifier.
            """
        },
        1: {
            "name": "Brep",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The brep object's identifier.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created intersection curve and point objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 545,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBrep",
            "opt_or_req": "Required",
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

