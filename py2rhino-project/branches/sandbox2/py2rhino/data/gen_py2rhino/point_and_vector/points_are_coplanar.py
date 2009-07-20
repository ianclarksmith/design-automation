points_are_coplanar = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "points_are_coplanar",

    "doc_html": """
        Verifies that an array of 3-D points are co-planar.
    """,

    "syntax_html": """
        Rhino.PointsAreCoplanar (arrPoints [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.
            """
        },
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A tolerance to use when verifying. The default is to use Rhino's internal zero tolerance (1.0e-12).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating either coplanar or not coplanar, respectively, if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 593,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

