surface_curvature_analysis = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceCurvatureAnalysis",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_curvature_analysis",

    "doc_html": """
        Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of curvature information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "array",
            "doc": "An array containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status."
        },
        2: {
            "type": "array",
            "doc": "An array containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison."
        },
        3: {
            "type": "array",
            "doc": "An array containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison."
        },
        4: {
            "type": "array",
            "doc": "An array containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison."
        },
        5: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 632,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

