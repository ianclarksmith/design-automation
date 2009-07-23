add_planar_srf = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddPlanarSrf",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_planar_srf",

    "doc_html": """
        Creates one or more surfaces from planar curves.
    """,

    "syntax_html": {
        0: ("arrObjects"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of curve object identifiers.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the new objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 371,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

