curve_discontinuity = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveDiscontinuity",
    "output_package_name": "curve",
    "output_module_name": "curve_discontinuity",

    "doc_html": """
        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.
    """,

    "syntax_html": """
        Rhino.CurveDiscontinuity (strObject [, intType])
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
            "name": "Style",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The type of continuity to test for.  The types of continuity are as follows:
		Value
		Description
		1
		C0 - Continuous function
		2
		C1 - Continuous first derivative
		3
		C2 - Continuous first and second derivative
		4
		G1 - Continuous unit tangent
		5
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points where the curve is discontinuous if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 579,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaType",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

