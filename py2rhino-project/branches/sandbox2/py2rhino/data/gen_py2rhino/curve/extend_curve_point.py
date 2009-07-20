extend_curve_point = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "extend_curve_point",

    "doc_html": """
        Extends a non-closed curve object by smooth extension to a point.
    """,

    "syntax_html": """
        Rhino.ExtendCurvePoint (strObject, intSide, arrPoint)
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
            "name": "Side",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
            """
        },
        2: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the extended object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 437,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSize",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

