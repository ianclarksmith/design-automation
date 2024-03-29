surface_sphere = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceSphere",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_sphere",

    "doc_html": """
        Returns the definition of a sphere surface.
    """,

    "syntax_html": {
        0: ("strSurface"),
    },

    "params_html": {
        0: {
            "name": "strSurface",
            "py_name": "surface",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Surface",
            "doc": """
        The surface object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the definition of the sphere if successful.  The elements of the array are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere."
        },
        2: {
            "type": "number",
            "doc": "The radius of the sphere."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 887,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

