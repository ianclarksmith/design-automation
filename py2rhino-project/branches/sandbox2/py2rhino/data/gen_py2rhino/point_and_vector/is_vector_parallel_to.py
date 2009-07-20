is_vector_parallel_to = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "is_vector_parallel_to",

    "doc_html": """
        Compares two vectors to see if they are parallel.
    """,

    "syntax_html": """
        Rhino.IsVectorParallelTo (arrVector1, arrVector2)
    """,

    "params_html": {
        0: {
            "name": "Vector1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D vector.
            """
        },
        1: {
            "name": "Vector2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D vector to compare to.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The result of the comparison if successful. The possible results are as follows:"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 660,

    "params_com": {
        0: {
            "name": "vaVec0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaVec1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

