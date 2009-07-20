simplify_array = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "simplify_array",

    "doc_html": """
        Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.
    """,

    "syntax_html": """
        Rhino.SimplifyArray (arrPoints)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A one-dimensional array containing real numbers, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 597,

    "params_com": {
        0: {
            "name": "vaArray",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

