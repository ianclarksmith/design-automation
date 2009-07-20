distance = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "distance",

    "doc_html": """
        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.
    """,

    "syntax_html": """
        Rhino.Distance (arrPoint1, arrPoint2)
    """,

    "params_html": {
        0: {
            "name": "Point1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first 3-D point.
            """
        },
        1: {
            "name": "Point2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second 3-D point.
            """
        },
        2: {
            "name": "PointArray",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If arrPoint1 and arrPoint2 are specified, then the distance is successful."
        },
        1: {
            "type": "array",
            "doc": "If arrPoint1 and arrPointArray are specified, then an array of distances if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 118,

    "params_com": {
        0: {
            "name": "vaFrom",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTo",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

