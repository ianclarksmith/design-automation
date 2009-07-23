short_path = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ShortPath",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "short_path",

    "doc_html": """
        Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strSurface", "arrStart", "arrEnd"),
    },

    "params_html": {
        0: {
            "name": "strSurface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
            "doc": """
        The identifier of the surface object that pulls.
            """
        },
        1: {
            "name": "arrStart",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Start",
            "doc": """
        A 3-D surface point identifying the starting point of the short curve.
            """
        },
        2: {
            "name": "arrEnd",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "End",
            "doc": """
        A 3-D surface point identifying the ending point of the short curve.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new curve object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 702,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

