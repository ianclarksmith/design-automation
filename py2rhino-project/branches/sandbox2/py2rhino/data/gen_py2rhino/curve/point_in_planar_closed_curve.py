point_in_planar_closed_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "PointInPlanarClosedCurve",
    "output_package_name": "curve",
    "output_module_name": "point_in_planar_closed_curve",

    "doc_html": """
        Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.
    """,

    "syntax_html": {
        0: ("arrPoint", "strCurve", "arrPlane", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point to test.
            """
        },
        1: {
            "name": "strCurve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The object identifier of the planar, closed curve.
            """
        },
        2: {
            "name": "arrPlane",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
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
            "name": "dblTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The tolerance.  If omitted, the current document absolute tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "A number identifying the result if successful.  The possible values are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 482,

    "params_com": {
        0: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrv",
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

