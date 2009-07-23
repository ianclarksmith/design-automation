add_interp_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddInterpCurve",
    "output_package_name": "curve",
    "output_module_name": "add_interp_curve",

    "doc_html": """
        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.
    """,

    "syntax_html": {
        0: ("arrPoints", "intDegree", "intKnotStyle", "arrStartTan", "arrEndTan"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array containing 3-D points to interpolate.  For periodic curves, if the final point is a duplicate of the initial point, it is ignored. Note, the number of control points must be >= (intDegree+1).
            """
        },
        1: {
            "name": "intDegree",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Degree",
            "doc": """
        The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.  For intKnotStyle = 4 or 5, the degree must be odd.
            """
        },
        2: {
            "name": "intKnotStyle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "KnotStyle",
            "doc": """
        The knot style to use, and whether the curve should be periodic.  If omitted, uniform knots (0) are created.
		Value
		Description
		0
		Uniform knots.  Parameter spacing between consecutive knots is 1.0.
		1
		Chord length spacing.  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
		2
		Sqrt (chord length).  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
		3
		Periodic with uniform spacing.
		4
		Periodic with chord length spacing.  Requires an odd degree value.
		5
            """
        },
        3: {
            "name": "arrStartTan",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartTan",
            "doc": """
        A 3-D vector that specifies a tangency condition at the beginning of the curve. If the curve is to periodic, this argument must be omitted.
            """
        },
        4: {
            "name": "arrEndTan",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndTan",
            "doc": """
        A 3-D vector that specifies a tangency condition at the end of the curve. If the curve is to periodic, this argument must be omitted.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 268,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaKnot",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCV1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaCVn1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

