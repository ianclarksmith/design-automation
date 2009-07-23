is_plane_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsPlaneSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_plane_surface",

    "doc_html": """
        Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object to verify.
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

    "id_com": 638,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

