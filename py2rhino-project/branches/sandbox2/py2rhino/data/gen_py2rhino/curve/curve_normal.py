curve_normal = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_normal",

    "doc_html": """
        Returns the normal direction of the plane in which a planar curve object lies.
    """,

    "syntax_html": """
        Rhino.CurveNormal (strObject)
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
            "doc": "The 3-D normal vector if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 521,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

