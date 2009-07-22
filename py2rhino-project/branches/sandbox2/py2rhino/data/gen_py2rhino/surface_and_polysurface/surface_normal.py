surface_normal = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceNormal",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_normal",

    "doc_html": """
        Returns a 3-D vector that is the normal to a surface at a parameter.
    """,

    "syntax_html": """
        Rhino.SurfaceNormal (strObject, arrParameter)
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
        1: {
            "name": "Parameter",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array containing the UV parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D vector if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 362,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

