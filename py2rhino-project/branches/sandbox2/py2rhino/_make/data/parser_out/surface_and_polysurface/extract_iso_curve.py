extract_iso_curve = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtractIsoCurve",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extract_iso_curve",

    "doc_html": """
        Extracts isoparametric curves from a surface.
    """,

    "syntax_html": {
        0: ("strObject", "arrParameter", "intDir"),
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
        An array containing the U,V parameter of the surface to evaluate.
            """
        },
        2: {
            "name": "intDir",
            "py_name": "dir",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Dir",
            "doc": """
        The direction, either 0 = U, 1 = V, or 2 = Both.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 488,

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
        2: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

