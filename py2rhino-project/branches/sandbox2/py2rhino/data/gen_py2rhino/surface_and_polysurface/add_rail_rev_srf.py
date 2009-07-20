add_rail_rev_srf = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_rail_rev_srf",

    "doc_html": """
        Create a surface by revolving a profile curve along a rail curve.
    """,

    "syntax_html": """
        Rhino.AddRailRevSrf (strProfile, strRail, arrAxis)
    """,

    "params_html": {
        0: {
            "name": "Profile",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the profile curve.
            """
        },
        1: {
            "name": "Rail",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the rail curve.
            """
        },
        2: {
            "name": "Axis",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
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

    "id_com": 536,

    "params_com": {
        0: {
            "name": "vaProfile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRail",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAxis",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

