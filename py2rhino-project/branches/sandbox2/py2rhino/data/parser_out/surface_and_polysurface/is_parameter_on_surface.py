is_parameter_on_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IsParameterOnSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "is_parameter_on_surface",

    "doc_html": """
        Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.
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
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 879,

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

