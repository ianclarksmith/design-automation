add_srf_pt = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSrfPt",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_srf_pt",

    "doc_html": """
        Creates a new surface from either 3 or 4 corner points.
    """,

    "syntax_html": {
        0: ("arrPoints"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of either 3 or 4 corner points.
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

    "id_com": 204,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

