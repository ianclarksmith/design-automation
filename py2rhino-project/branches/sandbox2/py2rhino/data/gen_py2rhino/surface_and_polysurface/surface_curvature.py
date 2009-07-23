surface_curvature = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceCurvature",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_curvature",

    "doc_html": """
        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.
    """,

    "syntax_html": {
        0: ("strObject", "arrParameter"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "arrParameter",
            "py_name": "parameter",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Parameter",
            "doc": """
        An array containing the U,V parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of curvature information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "Maximum principal curvature."
        },
        2: {
            "type": "number",
            "doc": "Minimum principal curvature."
        },
        3: {
            "type": "number",
            "doc": "Gaussian curvature."
        },
        4: {
            "type": "number",
            "doc": "Mean curvature."
        },
        5: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 378,

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

