is_poly_surface_planar = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "is_poly_surface_planar",

    "doc_html": """
        Verifies a polysurface object is planar.
    """,

    "syntax_html": """
        Rhino.IsPolySurfacePlanar (strObject)
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
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 209,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

