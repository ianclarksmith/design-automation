add_rev_srf = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddRevSrf",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_rev_srf",

    "doc_html": """
        Create a surface by revolving a curve around an axis.
    """,

    "syntax_html": {
        0: ("strCurve", "arrAxis", "dblStartAngle", "dblEndAngle"),
    },

    "params_html": {
        0: {
            "name": "strProfile",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Profile",
            "doc": """
        The identifier of the curve to revolve.
            """
        },
        1: {
            "name": "arrAxis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Axis",
            "doc": """
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
            """
        },
        2: {
            "name": "dblStartAngle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "StartAngle",
            "doc": """
        The starting angle. If omitted, an angle of 0.0 is used.
            """
        },
        3: {
            "name": "dblEndAngle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "EndAngle",
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

