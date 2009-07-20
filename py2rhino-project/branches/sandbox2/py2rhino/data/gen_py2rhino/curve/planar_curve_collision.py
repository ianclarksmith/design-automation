planar_curve_collision = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "planar_curve_collision",

    "doc_html": """
        Determines if two coplanar curves intersect.
    """,

    "syntax_html": """
        Rhino.PlanarCurveCollision (strCurve1, strCurve2 [, arrPlane [, dblTolerance]])
    """,

    "params_html": {
        0: {
            "name": "Curve1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object identifier of the first planar curve.
            """
        },
        1: {
            "name": "Curve2",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object identifier of the second planar curve.
            """
        },
        2: {
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
		Element
		Type
		Description
		0
		Array
		Required.  The construction plane's origin (3-D point).
		1
		Array
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Array
		Required.  The construction plane's Y axis direction (3-D vector).
		3
		Array
            """
        },
        3: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The tolerance.  If omitted, the current document absolute tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 481,

    "params_com": {
        0: {
            "name": "vaCrv1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrv2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

