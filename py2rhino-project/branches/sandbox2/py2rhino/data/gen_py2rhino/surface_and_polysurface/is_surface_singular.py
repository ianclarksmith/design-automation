is_surface_singular = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "is_surface_singular",

    "doc_html": """
        Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.
    """,

    "syntax_html": """
        Rhino.IsSurfaceSingular (strObject)
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
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction, either 0 = south, 1 = east, 2 = north, or 3 = west.
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

    "id_com": 214,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

