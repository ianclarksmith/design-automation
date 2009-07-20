point_compare = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "point_compare",

    "doc_html": """
        Compares two 3-D points.
    """,

    "syntax_html": """
        Rhino.PointCompare (arrPoint1, arrPoint2 [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Point1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first 3-D point to compare.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second 3-D point to compare.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The tolerance to use for the comparison. If omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 667,

    "params_com": {
        0: {
            "name": "vaPt0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt1",
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

