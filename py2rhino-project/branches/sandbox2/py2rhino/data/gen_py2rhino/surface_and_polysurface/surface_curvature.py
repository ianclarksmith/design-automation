surface_curvature = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceCurvature",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_curvature",

    "doc_html": """
        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.
    """,

    "syntax_html": """
        Rhino.SurfaceCurvature (strObject, arrParameter)
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

