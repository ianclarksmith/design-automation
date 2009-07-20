curve_arc_length_point = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveArcLengthPoint",
    "output_package_name": "curve",
    "output_module_name": "curve_arc_length_point",

    "doc_html": """
        Returns the point on the curve that is a specified arc length from the start of the curve.
    """,

    "syntax_html": """
        Rhino.CurveArcLengthPoint (strObject, dblLength [, blnFromStart])
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
            "name": "Length",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The arc length from the start of the curve to evaluate.
            """
        },
        2: {
            "name": "FromStart",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If not specified or True, then the arc length point is calculated from the start of the curve. If False, the arc length point is calculated from the end of the curve.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 658,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLength",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaStart",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

