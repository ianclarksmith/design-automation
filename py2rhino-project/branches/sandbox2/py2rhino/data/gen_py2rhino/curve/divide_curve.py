divide_curve = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "divide_curve",

    "doc_html": """
        Divides a curve object into a specified number of segments.
    """,

    "syntax_html": """
        Rhino.DivideCurve (strObject, lngSegments [, blnCreate [, blnPoints]])
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
            "name": "Segments",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The number of segments.
            """
        },
        2: {
            "name": "Create",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Create the division points. If omitted or False, points are not created.
            """
        },
        3: {
            "name": "Points",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnPoints is not specified or True, then an array containing 3-D division points if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnPoints is False, then an array containing division curve parameters if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 78,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCreate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPoints",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

