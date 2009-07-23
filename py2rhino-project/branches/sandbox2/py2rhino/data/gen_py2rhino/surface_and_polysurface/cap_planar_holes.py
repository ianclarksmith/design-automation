cap_planar_holes = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "CapPlanarHoles",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "cap_planar_holes",

    "doc_html": """
        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strSurface"),
    },

    "params_html": {
        0: {
            "name": "strSurface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
            "doc": """
        The identifier of the surface or polysurface to cap.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 701,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

