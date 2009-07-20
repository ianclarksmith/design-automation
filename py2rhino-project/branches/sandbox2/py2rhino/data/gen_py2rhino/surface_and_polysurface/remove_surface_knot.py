remove_surface_knot = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "remove_surface_knot",

    "doc_html": """
        Deletes a knot-line from a surface object.
    """,

    "syntax_html": """
        Rhino.RemoveSurfaceKnot (strObject, arrParameter, intDirection)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface object.
            """
        },
        1: {
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "dbl",
            "doc": """
        An array containing a U,V parameter on the surface.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
            """
        },
        2: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction for knot insertion, either 0 = U, or 1 = V.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 917,

    "params_com": {
        0: {
            "name": "vaSurface",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaKnot",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

