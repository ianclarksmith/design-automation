divide_curve_equidistant = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "DivideCurveEquidistant",
    "output_package_name": "curve",
    "output_module_name": "divide_curve_equidistant",

    "doc_html": """
        Divides a curve such that the linear distance between the points is equal.
		Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.
    """,

    "syntax_html": """
        Rhino.DivideCurveEquidistant (strObject, dblDistance [, blnCreate [, blnPoints]])
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
            "name": "Distance",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The linear distance between division points.
            """
        },
        2: {
            "name": "Create",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Create the division points. If omitted or False, points are not created.
            """
        },
        3: {
            "name": "Points",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnPoints is not specified or True, then an array containing 3-D division points if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnPoints is False, then an array containing division curve parameters if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 913,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLength",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCreate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPoints",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

