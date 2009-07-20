evaluate_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "EvaluateSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "evaluate_surface",

    "doc_html": """
        Evaluates a surface at a U,V parameter.
    """,

    "syntax_html": """
        Rhino.EvaluateSurface (strObject, arrParameter)
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
            "type_string": "arr",
            "doc": """
        An array containing the U,V parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 205,

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

