curve_fillet_points = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveFilletPoints",
    "output_package_name": "curve",
    "output_module_name": "curve_fillet_points",

    "doc_html": """
        Find points at which to cut a pair of curves so that a fillet of a specified radius fits.  A fillet point is a pair of points (arrPoint0, arrPoint1) such that there is a circle of radius dblRadius tangent to curve strCurve0 at arrPoint0 and tangent to curve strCurve1 at arrPoint1.
		Of all possible fillet points, this function returns the one which is the closest to the base point arrBasePoint0, arrBasePoint1.  Distance from the base point is measured by the sum of arc lengths along the two curves.
    """,

    "syntax_html": {
        0: ("strCurve0", "strCurve1", "dblRadius", "arrBasePoint0", "arrBasePoint1"),
    },

    "params_html": {
        0: {
            "name": "strCurve0",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve0",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "strCurve1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve1",
            "doc": """
        The identifier of the second curve object.
            """
        },
        2: {
            "name": "dblRadius",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
            "doc": """
        The fillet radius. If omitted, a radius of 1.0 is specified.
            """
        },
        3: {
            "name": "arrBasePoint0",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "BasePoint0",
            "doc": """
        The base point on the first curve. If omitted, the starting point of the curve is used.
            """
        },
        4: {
            "name": "arrBasePoint1",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "BasePoint1",
            "doc": """
        The base point on the second curve. If omitted, the starting point of the curve is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnPoints is True, then an array of point and vector values if successful.  The array elements are as follows:"
        },
        1: {
            "type": "string",
            "doc": "If blnPoints is False, then the identifier of the fillet curve if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 572,

    "params_com": {
        0: {
            "name": "vaCrv0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrv1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRadius",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPt0",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaPt1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

