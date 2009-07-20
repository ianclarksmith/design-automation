surface_cylinder = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceCylinder",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_cylinder",

    "doc_html": """
        Returns the definition of a cylinder surface.
    """,

    "syntax_html": """
        Rhino.SurfaceCylinder (strSurface)
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
            "doc": "An array containing the definition of the cylinder if successful.  The elements of the array are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The base plane of the cylinder."
        },
        2: {
            "type": "number",
            "doc": "The height of the cylinder."
        },
        3: {
            "type": "number",
            "doc": "The radius of the cylinder."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 888,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

