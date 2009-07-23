add_interp_curve_ex = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddInterpCurveEx",
    "output_package_name": "curve",
    "output_module_name": "add_interp_curve_ex",

    "doc_html": """
        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.
    """,

    "syntax_html": {
        0: ("arrPoints", "intDegree", "intKnotStyle", "blnSharp", "arrStartTangent", "arrEndTangent"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
            """
        },
        1: {
            "name": "intDegree",
            "py_name": "degree",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Degree",
            "doc": """
        The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
            """
        },
        2: {
            "name": "intKnotStyle",
            "py_name": "knot_style",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "KnotStyle",
            "doc": """
        The knot style to use. If omitted, a knot style = 0 is used. The knot style determines how an interpolated curve will be parameterized.
		Value
		Description
		0
		Uniform.  The knot spacing is always 1 and is not based on the physical spacing of points.
		1
		Chord. The spacing between the points is used for the knot spacing
		2
            """
        },
        3: {
            "name": "blnSharp",
            "py_name": "sharp",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Sharp",
            "doc": """
        If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
            """
        },
        4: {
            "name": "arrStartTangent",
            "py_name": "start_tangent",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartTangent",
            "doc": """
        A 3-D vector that specifies a tangency condition at the beginning of the curve.
            """
        },
        5: {
            "name": "arrEndTangent",
            "py_name": "end_tangent",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndTangent",
            "doc": """
        A 3-D vector that specifies a tangency condition at the end of the curve.
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

    "id_com": 520,

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
            "name": "vaKnotSpacing",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaSharp",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaStartTangent",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaEndTangent",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

