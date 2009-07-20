brep_closest_point = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "brep_closest_point",

    "doc_html": """
        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.
    """,

    "syntax_html": """
        Rhino.BrepClosestPoint (strObject, arrPoint)
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
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The test, or sampling, point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of closest point information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 514,

    "params_com": {
        0: {
            "name": "vaBrep",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

