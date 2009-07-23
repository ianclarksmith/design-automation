remove_surface_knot = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "RemoveSurfaceKnot",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "remove_surface_knot",

    "doc_html": """
        Deletes a knot-line from a surface object.
    """,

    "syntax_html": {
        0: ("strObject", "arrParameter", "intDirection"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the surface object.
            """
        },
        1: {
            "name": "dblParameter",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "dbl",
            "name_main": "Parameter",
            "doc": """
        An array containing a U,V parameter on the surface.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
            """
        },
        2: {
            "name": "intDirection",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
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

