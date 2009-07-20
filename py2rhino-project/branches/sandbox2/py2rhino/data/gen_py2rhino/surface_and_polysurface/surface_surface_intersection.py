surface_surface_intersection = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "surface_surface_intersection",

    "doc_html": """
        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.
    """,

    "syntax_html": """
        Rhino.SurfaceSurfaceIntersection (strSurfaceA, strSurfaceB [, dblTolerance [, blnCreate]])
    """,

    "params_html": {
        0: {
            "name": "SurfaceA",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first surface object.
            """
        },
        1: {
            "name": "SurfaceB",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the second surface object.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            """
        },
        3: {
            "name": "Create",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Create the intersection curves and points.  If omitted, intersection geometry will not be created.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnCreate is not specified or is equal to False, an array numbers identifying the intersection event type if successful.  The array will contain one or more of the following intersection event types:"
        },
        1: {
            "type": "array",
            "doc": "If blnCreate is specified and is equal to True, a two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:"
        },
        2: {
            "type": "number",
            "doc": "The intersection event type.  See the above table for details."
        },
        3: {
            "type": "string",
            "doc": "The identifier of the intersection curve or point object that was created."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 484,

    "params_com": {
        0: {
            "name": "vaSrfA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSrfB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCreate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

