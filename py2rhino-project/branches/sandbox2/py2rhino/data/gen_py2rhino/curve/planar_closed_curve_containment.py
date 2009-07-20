planar_closed_curve_containment = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "PlanarClosedCurveContainment",
    "output_package_name": "curve",
    "output_module_name": "planar_closed_curve_containment",

    "doc_html": """
        Determines the relationship between the regions bounded by two coplanar simple closed curves.
    """,

    "syntax_html": """
        Rhino.PlanarClosedCurveContainment (strCurve1, strCurve2 [, arrPlane [, dblTolerance]])
    """,

    "params_html": {
        0: {
            "name": "Curve1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object identifier of the first planar, closed curve.
            """
        },
        1: {
            "name": "Curve2",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object identifier of the second planar, closed curve.
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
            "type": "number",
            "doc": "A number identifying the relationship if successful.  The possible values are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 480,

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

