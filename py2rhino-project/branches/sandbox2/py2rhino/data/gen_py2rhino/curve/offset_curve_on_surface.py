offset_curve_on_surface = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "OffsetCurveOnSurface",
    "output_package_name": "curve",
    "output_module_name": "offset_curve_on_surface",

    "doc_html": """
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    """,

    "syntax_html": """
        Rhino.OffsetCurveOnSurface (strCurve, strSurface, dblDistance)
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The curve object's identifier. Note, the curve must lie on the surface.
            """
        },
        1: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
		dblDistance
		Requried.  Number.  The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
		arrParameter
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the new curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 906,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSurface",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDistance",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

