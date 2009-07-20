fit_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "FitCurve",
    "output_package_name": "curve",
    "output_module_name": "fit_curve",

    "doc_html": """
        Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.
    """,

    "syntax_html": """
        Rhino.FitCurve (strObject [, intDegree [, dblTolerance [, dblAngleTolerance]]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The curve degree, which must be greater than 1. The default is 3.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
            """
        },
        3: {
            "name": "AngleTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The kink smoothing tolerance in degrees.  If dblAngleTolerance is 0.0, all kinks are smoothed.  If dblAngleTolerance is > 0.0, kinks smaller than dblAngleTolerance are smoothed.  If dblAngleTolerance is not specified or < 0.0, the document angle tolerance is used for the kink smoothing.
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

    "id_com": 813,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaAngTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

