surface_area_centroid = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_area_centroid",

    "doc_html": """
        Calculates the area centroid of a surface or polysurface object.
    """,

    "syntax_html": """
        Rhino.SurfaceAreaCentroid (strObject)
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
            "doc": "An array of area centroid information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 384,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

