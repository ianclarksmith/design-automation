insert_surface_knot = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "InsertSurfaceKnot",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "insert_surface_knot",

    "doc_html": """
        Inserts a knot into a surface object.
    """,

    "syntax_html": {
        0: ("strObject", "arrParameter", "intDirection", "blnSymmetrical"),
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
        An array containing a U,V parameter on the surface.
            """
        },
        2: {
            "name": "intDirection",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The direction for knot insertion, either 0 = U, 1 = V, or 2 = both.
            """
        },
        3: {
            "name": "blnSymmetrical",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Symmetrical",
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

