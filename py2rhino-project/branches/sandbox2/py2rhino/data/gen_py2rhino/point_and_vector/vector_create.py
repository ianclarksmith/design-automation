vector_create = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "vector_create",

    "doc_html": """
        Creates a vector from two 3-D points.
    """,

    "syntax_html": """
        Rhino.VectorCreate (arrPoint1, arrPoint2)
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D vector if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 614,

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
    },

    "returns_com": "tagVARIANT",

}

