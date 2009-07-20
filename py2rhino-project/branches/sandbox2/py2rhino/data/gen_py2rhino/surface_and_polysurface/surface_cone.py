surface_cone = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceCone",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_cone",

    "doc_html": """
        Returns the definition of a cone surface.
    """,

    "syntax_html": """
        Rhino.SurfaceCone (strSurface)
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the definition of the cone if successful.  The elements of the array are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis."
        },
        2: {
            "type": "number",
            "doc": "The height of the cone."
        },
        3: {
            "type": "number",
            "doc": "The radius of the cone."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 889,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

