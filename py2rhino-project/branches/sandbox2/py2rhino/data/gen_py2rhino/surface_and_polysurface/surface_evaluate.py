surface_evaluate = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceEvaluate",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_evaluate",

    "doc_html": """
        A general purpose surface evaluator.
    """,

    "syntax_html": {
        0: ("strObject", "arrParameter", "intDerivative"),
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
        2: {
            "name": "intDerivative",
            "py_name": "derivative",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Derivative",
            "doc": """
        The number of derivatives to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of length (intDerivative+1)*(intDerivative+2)/2 if successful.  The array elements are as follows:"
        },
        1: {
            "type": "array",
            "doc": "The 3-D point."
        },
        2: {
            "type": "array",
            "doc": "The first derivative."
        },
        3: {
            "type": "array",
            "doc": "The first derivative."
        },
        4: {
            "type": "array",
            "doc": "The second derivative."
        },
        5: {
            "type": "array",
            "doc": "The second derivative."
        },
        6: {
            "type": "array",
            "doc": "The second derivative."
        },
        7: {
            "type": "array",
            "doc": "etc..."
        },
        8: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 583,

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
            "name": "vaDerCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

