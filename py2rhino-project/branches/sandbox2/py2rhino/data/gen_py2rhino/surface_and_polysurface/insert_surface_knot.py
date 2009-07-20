insert_surface_knot = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "insert_surface_knot",

    "doc_html": """
        Inserts a knot into a surface object.
    """,

    "syntax_html": """
        Rhino.InsertSurfaceKnot (strObject, arrParameter, intDirection [, blnSymmetrical)
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
        An array containing a U,V parameter on the surface.
            """
        },
        2: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction for knot insertion, either 0 = U, 1 = V, or 2 = both.
            """
        },
        3: {
            "name": "Symmetrical",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If blnSymmetrical = True, then knots are added on both sides of the center of the surface.  The default value is False.
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

    "id_com": 516,

    "params_com": {
        0: {
            "name": "vaSrf",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaSym",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

