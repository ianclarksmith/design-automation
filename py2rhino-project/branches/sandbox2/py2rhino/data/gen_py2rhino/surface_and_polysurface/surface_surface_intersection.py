surface_surface_intersection = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceSurfaceIntersection",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_surface_intersection",

    "doc_html": """
        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.
    """,

    "syntax_html": {
        0: ("strSurfaceA", "strSurfaceB", "dblTolerance", "blnCreate"),
    },

    "params_html": {
        0: {
            "name": "strSurfaceA",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "SurfaceA",
            "doc": """
        The identifier of the first surface object.
            """
        },
        1: {
            "name": "strSurfaceB",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "SurfaceB",
            "doc": """
        The identifier of the second surface object.
            """
        },
        2: {
            "name": "dblTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            """
        },
        3: {
            "name": "blnCreate",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Create",
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

