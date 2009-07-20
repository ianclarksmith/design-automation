plane_from_points = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "plane_from_points",

    "doc_html": """
        Creates a plane from three non-colinear points.
    """,

    "syntax_html": """
        Rhino.PlaneFromPoints (arrOrigin, arrPointX, arrPointY)
    """,

    "params_html": {
        0: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first point, or origin, of the plane.
            """
        },
        1: {
            "name": "PointX",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A point on the plane's X axis.
            """
        },
        2: {
            "name": "PointY",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A point on the plane's Y axis.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 649,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

