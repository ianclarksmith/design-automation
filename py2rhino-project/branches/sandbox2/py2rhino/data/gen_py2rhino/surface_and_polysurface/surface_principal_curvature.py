surface_principal_curvature = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfacePrincipalCurvature",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_principal_curvature",

    "doc_html": """
        Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The curve's identifier.
            """
        },
        1: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A point on the curve to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of two strings that identify the Maximum and Minimum principal curvature curves, respectively, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 717,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

