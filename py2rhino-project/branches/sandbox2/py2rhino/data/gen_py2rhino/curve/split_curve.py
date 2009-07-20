split_curve = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "split_curve",

    "doc_html": """
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    """,

    "syntax_html": """
        Rhino.SplitCurve (strObject, dblParameter [, blnDelete])
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
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The parameter, to split the curve at, that is in the interval returned by CurveDomain.
            """
        },
        2: {
            "name": "Parameters",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
            """
        },
        3: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

