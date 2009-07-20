curve_plane = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_plane",

    "doc_html": """
        Returns the plane in which a planar curve lies. Note, this function works only on planar curves.
    """,

    "syntax_html": """
        Rhino.CurvePlane (strCurve)
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a planar curve object
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane in which the curve lies if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 609,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

