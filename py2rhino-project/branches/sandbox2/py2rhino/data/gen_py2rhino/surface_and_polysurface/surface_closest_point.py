surface_closest_point = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_closest_point",

    "doc_html": """
        Returns the UV parameter of the point on a surface that is closest to a test point.
    """,

    "syntax_html": """
        Rhino.SurfaceClosestPoint (strObject, arrPoint)
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
            "doc": "An array containing the U,V parameters of the closest point on the surface if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 215,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

