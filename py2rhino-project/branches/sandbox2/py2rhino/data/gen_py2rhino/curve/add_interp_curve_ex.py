add_interp_curve_ex = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddInterpCurveEx",
    "output_package_name": "curve",
    "output_module_name": "add_interp_curve_ex",

    "doc_html": """
        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.
    """,

    "syntax_html": """
        Rhino.AddInterpCurveEx (arrPoints [, intDegree [, intKnotStyle [, blnSharp [, arrStartTangent [, arrEndTangent]]]]])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
            """
        },
        1: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
            """
        },
        2: {
            "name": "KnotStyle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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
            "name": "Sharp",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
            """
        },
        4: {
            "name": "StartTangent",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A 3-D vector that specifies a tangency condition at the beginning of the curve.
            """
        },
        5: {
            "name": "EndTangent",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
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

