curve_area_centroid = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "curve_area_centroid",

    "doc_html": """
        Returns that area centroid of closed, planar curves. The results are based on the current drawing units.
    """,

    "syntax_html": """
        Rhino.CurveAreaCentroid (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a closed, planar curve object.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings containing the identifiers of one or more closed, planar curve objects.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of area centroid information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 677,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

