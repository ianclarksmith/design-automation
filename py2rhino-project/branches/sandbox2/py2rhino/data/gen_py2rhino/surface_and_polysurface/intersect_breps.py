intersect_breps = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "intersect_breps",

    "doc_html": """
        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.
    """,

    "syntax_html": """
        Rhino.IntersectBreps (strBrep1, strBrep2 [, dblTolerance])
    """,

    "params_html": {
        0: {
            "name": "Brep1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The first brep object's identifier.
            """
        },
        1: {
            "name": "Brep2",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The second  brep object's identifier.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created intersection curve and point objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 544,

    "params_com": {
        0: {
            "name": "vaBrep0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBrep1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

