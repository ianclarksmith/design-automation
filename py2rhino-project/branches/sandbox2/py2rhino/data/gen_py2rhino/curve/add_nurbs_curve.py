add_nurbs_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddNurbsCurve",
    "output_package_name": "curve",
    "output_module_name": "add_nurbs_curve",

    "doc_html": """
        Adds a NURBS curve object to the document.
    """,

    "syntax_html": {
        0: ("arrPoints", "arrKnots", "intDegree", "arrWeights"),
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
        An array of 3-D control points.
            """
        },
        1: {
            "name": "arrKnots",
            "py_name": "knots",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Knots",
            "doc": """
        The knot values for the curve.  The number of elements in arrKnots must equal the number of elements in arrPoints plus intDegree minus one (1).
            """
        },
        2: {
            "name": "intDegree",
            "py_name": "degree",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Degree",
            "doc": """
        The degree of the curve.  The degree must be greater than or equal to one (1).
            """
        },
        3: {
            "name": "arrWeights",
            "py_name": "weights",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Weights",
            "doc": """
        The weight values for the curve.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
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

    "id_com": 309,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKnots",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDegree",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaWeights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

