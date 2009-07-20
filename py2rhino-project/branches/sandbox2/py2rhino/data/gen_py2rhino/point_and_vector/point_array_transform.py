point_array_transform = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "point_array_transform",

    "doc_html": """
        Transforms an array of 3-D points.
    """,

    "syntax_html": """
        Rhino.PointArrayTransform (arrPoints, arrXform)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points to transform.
            """
        },
        1: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A valid 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 802,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

