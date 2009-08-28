surface_seam = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceSeam",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_seam",

    "doc_html": """
        Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.
    """,

    "syntax_html": {
        0: ("strObject", "intDirection", "dblParameter"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "intDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The parameter direction, where 0 = U and 1 = V.
            """
        },
        2: {
            "name": "dblParameter",
            "py_name": "parameter",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Parameter",
            "doc": """
        The parameter at which to place the seam.
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

    "id_com": 804,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

