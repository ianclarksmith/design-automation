ellipse_center_point = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "ellipse_center_point",

    "doc_html": """
        Returns the center point of an elliptical-shaped curve object.
    """,

    "syntax_html": """
        Rhino.EllipseCenterPoint (strObject)
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D center point of the ellipse if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 524,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

