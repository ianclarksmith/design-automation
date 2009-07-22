surface_evaluate = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceEvaluate",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_evaluate",

    "doc_html": """
        A general purpose surface evaluator.
    """,

    "syntax_html": """
        Rhino.SurfaceEvaluate (strObject, arrParameter, intDerivative)
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
        2: {
            "name": "Derivative",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
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

