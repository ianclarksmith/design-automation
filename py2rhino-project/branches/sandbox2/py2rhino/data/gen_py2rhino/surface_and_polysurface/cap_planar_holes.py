cap_planar_holes = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "cap_planar_holes",

    "doc_html": """
        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.CapPlanarHoles (strSurface)
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface or polysurface to cap.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 701,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

