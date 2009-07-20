surface_torus = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_torus",

    "doc_html": """
        Returns the definition of a torus surface.
    """,

    "syntax_html": """
        Rhino.SurfaceTorus (strSurface)
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the definition of the torus if successful.  The elements of the array are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The base plane of the torus."
        },
        2: {
            "type": "number",
            "doc": "The major radius of the torus."
        },
        3: {
            "type": "number",
            "doc": "The minor radius of the torus."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 890,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

