add_plane_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddPlaneSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_plane_surface",

    "doc_html": """
        Creates a plane surface.
    """,

    "syntax_html": {
        0: ("arrPlane", "dblDU", "dblDV"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The plane.
            """
        },
        1: {
            "name": "dblDU",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "DU",
            "doc": """
        The magnitude in the U direction.
            """
        },
        2: {
            "name": "dblDV",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "DV",
            "doc": """
        The magnitude in the V direction.
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

    "id_com": 648,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

