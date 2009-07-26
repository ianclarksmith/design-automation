split_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "SplitCurve",
    "output_package_name": "curve",
    "output_module_name": "split_curve",

    "doc_html": """
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    """,

    "syntax_html": {
        0: ("strObject", "dblParameter", "blnDelete"),
        1: ("strObject", "arrParameters", "blnDelete"),
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
            "name": "arrParameters",
            "py_name": "parameters",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Parameters",
            "doc": """
        An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
            """
        },
        2: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete the input curve. The default is to delete the input curve (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the two newly created curve objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 504,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

