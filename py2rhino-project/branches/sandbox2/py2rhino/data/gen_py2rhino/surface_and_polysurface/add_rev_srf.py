add_rev_srf = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_rev_srf",

    "doc_html": """
        Create a surface by revolving a curve around an axis.
    """,

    "syntax_html": """
        Rhino.AddRevSrf (strCurve, arrAxis [, dblStartAngle [, dblEndAngle]])
    """,

    "params_html": {
        0: {
            "name": "Profile",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve to revolve.
            """
        },
        1: {
            "name": "Axis",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
            """
        },
        2: {
            "name": "StartAngle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The starting angle. If omitted, an angle of 0.0 is used.
            """
        },
        3: {
            "name": "EndAngle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The ending angle. If omitted, an angle of 360.0 is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 535,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAxis",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSA",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaEA",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

