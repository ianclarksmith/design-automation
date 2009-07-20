surface_knot_count = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceKnotCount",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_knot_count",

    "doc_html": """
        Returns the knot count of a surface object.
    """,

    "syntax_html": """
        Rhino.SurfaceKnotCount (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The number of knots in the U and V directions if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 431,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

