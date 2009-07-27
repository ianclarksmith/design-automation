offset_curve_on_surface = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "OffsetCurveOnSurface",
    "output_package_name": "curve",
    "output_module_name": "offset_curve_on_surface",

    "doc_html": """
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    """,

    "syntax_html": {
        0: ("strCurve", "strSurface", "dblDistance"),
        1: ("strCurve", "strSurface", "arrParameter"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "py_name": "curve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The curve object's identifier. Note, the curve must lie on the surface.
            """
        },
        1: {
            "name": "strSurface",
            "py_name": "surface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
            "doc": """
        The surface object's identifier.
            """
        },
        2: {
            "name": "dblDistance",
            "py_name": "distance",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
            """
        },
        3: {
            "name": "arrParameter",
            "py_name": "parameter",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Parameter",
            "doc": """
        An array containing the surface U,V parameter that the curve will be offset through.
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

