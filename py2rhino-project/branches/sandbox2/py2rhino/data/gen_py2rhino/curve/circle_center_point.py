circle_center_point = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "circle_center_point",

    "doc_html": """
        Returns the center point of a circle curve object.
    """,

    "syntax_html": """
        Rhino.CircleCenterPoint (strObject [, intIndex])
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
            "name": "Index",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D center point of the circle if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 90,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

