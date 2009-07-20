add_plane_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddPlaneSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_plane_surface",

    "doc_html": """
        Creates a plane surface.
    """,

    "syntax_html": """
        Rhino.AddPlaneSurface (arrPlane, dblDU, dblDV)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane.
            """
        },
        1: {
            "name": "DU",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The magnitude in the U direction.
            """
        },
        2: {
            "name": "DV",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
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
